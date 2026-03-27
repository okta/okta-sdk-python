# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS
# IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

"""
DPoP (Demonstrating Proof-of-Possession) Implementation

This module implements RFC 9449 - OAuth 2.0 Demonstrating Proof of Possession (DPoP)
for the Okta Python SDK.

DPoP enhances OAuth 2.0 security by cryptographically binding access tokens to
client-possessed keys, preventing token theft and replay attacks.

Reference: https://datatracker.ietf.org/doc/html/rfc9449
"""

__all__ = ['DPoPProofGenerator', 'RSA_KEY_SIZE_BITS']

import ctypes
import json
import logging
import threading
import time
import uuid
from typing import Any, Dict, Optional

from Cryptodome.PublicKey import RSA
from jwcrypto.jwk import JWK
from jwt import encode as jwt_encode

# Import for access token hash computation and URL normalization
from okta.utils import compute_ath, normalize_dpop_url

logger = logging.getLogger("okta-sdk-python")

# Per RFC 9449 Section 4.3: RSA keys SHOULD be at least 2048 bits, recommended 3072
RSA_KEY_SIZE_BITS = 3072


class DPoPProofGenerator:
    """
    Generates DPoP proof JWTs per RFC 9449.

    This class manages ephemeral RSA key pairs and generates DPoP proof JWTs
    for OAuth token requests and API requests. It handles key rotation,
    nonce management, and ensures RFC 9449 compliance.

    Key Features:
    - Generates ephemeral RSA 3072-bit key pairs
    - Creates DPoP proof JWTs with proper claims (jti, htm, htu, iat, ath, nonce)
    - Manages server-provided nonces
    - Supports automatic key rotation

    Thread Safety:
    - All public methods are thread-safe using RLock (reentrant lock)
    - Multiple threads can safely call generate_proof_jwt() concurrently
    - Key rotation is blocked when active requests are in progress
    - The same thread can acquire the lock multiple times (reentrant)
    - Lock is held during entire proof generation (including RSA signing operations)
    - For high-concurrency scenarios (>100 req/sec), consider using separate client instances

    Security Notes:
    - Private keys are kept in memory only
    - Only public key components are exported (kty, n, e)
    - Keys are rotated periodically for better security
    - Nonces are validated and stored securely without logging
    """

    def __init__(self, config: Dict[str, Any]) -> None:
        """
        Initialize DPoP proof generator.

        Args:
            config: Configuration dictionary containing:
                - dpopKeyRotationInterval: Key rotation interval in seconds (default: 86400 / 24 hours)
        """
        self._lock = threading.RLock()  # Thread-safe access to shared state
        self._rsa_key: Optional[RSA.RsaKey] = None
        self._public_jwk: Optional[Dict[str, str]] = None
        self._key_created_at: Optional[float] = None
        self._rotation_interval: int = config.get('dpopKeyRotationInterval', 86400)  # 24h default
        self._nonce: Optional[str] = None
        self._active_requests: int = 0  # Track active requests to prevent rotation during use

        # Generate initial keys
        self._rotate_keys_internal()

        logger.debug(f"DPoP proof generator initialized with {self._rotation_interval}s key rotation interval")

    def _rotate_keys_internal(self) -> None:
        """
        Internal method to rotate keys.

        Generates a new RSA 3072-bit key pair and exports the public key as JWK.
        """
        logger.debug(f"Generating new RSA {RSA_KEY_SIZE_BITS}-bit key pair for DPoP")
        self._rsa_key = RSA.generate(RSA_KEY_SIZE_BITS)
        self._public_jwk = self._export_public_jwk()
        self._key_created_at = time.time()
        logger.debug(f"DPoP keys generated at {self._key_created_at}")

    def rotate_keys(self, force: bool = False) -> bool:
        """
        Safely rotate RSA key pair.

        Ensures no active requests are using the current key before rotating.
        If active requests exist, rotation is skipped for safety.

        Args:
            force: If True, skip age check and rotate immediately (for testing/manual rotation)

        Returns:
            bool: True if rotation occurred, False if skipped

        Note: Thread-safe - uses lock to ensure atomic check-and-rotate.
        """
        with self._lock:
            # Check for active requests - if any exist, skip rotation
            if self._active_requests > 0:
                logger.warning(
                    f"Skipping key rotation: {self._active_requests} active request(s) in progress"
                )
                return False

            # Check if rotation is actually needed (unless forced)
            if not force and self._key_created_at:
                age = time.time() - self._key_created_at
                if age < self._rotation_interval:
                    logger.debug(
                        f"Key rotation not needed: key age {age:.0f}s < interval {self._rotation_interval}s"
                    )
                    return False

            # Clear old key from memory (security best practice)
            # Note: Python doesn't guarantee immediate memory clearing due to
            # reference counting and garbage collection, but we make best effort
            old_key = self._rsa_key

            # Perform rotation
            self._rotate_keys_internal()

            # Clear nonce as it was tied to old key
            self._nonce = None

            # Securely clear old key from memory (defense in depth)
            if old_key:
                try:
                    # Overwrite key bytes before deletion to minimize memory exposure
                    # NOTE: This is best-effort only. Python's memory model does not
                    # guarantee secure deletion due to reference counting, garbage collection,
                    # and potential string interning. For true security, use hardware security modules.
                    old_key_bytes = old_key.export_key()
                    # Overwrite with zeros
                    ctypes.memset(id(old_key_bytes), 0, len(old_key_bytes))
                except (AttributeError, TypeError, OSError) as e:
                    # Log the failure for debugging
                    logger.debug(f"Failed to securely wipe old key: {e}")
                finally:
                    del old_key

            logger.debug("DPoP keys rotated successfully, nonce cleared")
            return True

    def generate_proof_jwt(
        self,
        http_method: str,
        http_url: str,
        access_token: Optional[str] = None,
        nonce: Optional[str] = None
    ) -> str:
        """
        Generate DPoP proof JWT per RFC 9449.

        Creates a signed JWT proving possession of the private key corresponding
        to the public key in the JWT header. The proof is bound to the specific
        HTTP request and optionally to an access token.

        RFC 9449 Section References:
        - Section 4.1: DPoP Proof JWT syntax and required claims
        - Section 4.2: URL normalization (htu claim must exclude query/fragment)
        - Section 4.3: Signature algorithm requirements (RS256)
        - Section 8: Server-provided nonces for replay protection

        Args:
            http_method: HTTP method (GET, POST, etc.) - will be uppercased for htm claim
            http_url: Full HTTP URL - query/fragment automatically stripped per RFC 9449 §4.2
            access_token: Access token for binding via 'ath' claim (optional, for API requests)
            nonce: Server-provided nonce (optional). If not provided, uses stored nonce.

        Returns:
            DPoP proof JWT as compact JWS string

        Thread Safety:
            This method is thread-safe and can be called concurrently.

        Example:
            >>> generator = DPoPProofGenerator(config)
            >>> proof = generator.generate_proof_jwt(
            ...     http_method="POST",
            ...     http_url="https://example.okta.com/oauth2/v1/token"
            ... )

        Reference:
            RFC 9449 - OAuth 2.0 Demonstrating Proof of Possession
            https://datatracker.ietf.org/doc/html/rfc9449
        """
        with self._lock:
            # Increment active request counter
            # Note: try-finally ensures counter is always decremented, even on exceptions
            # This prevents counter leaks and maintains accurate tracking for key rotation
            self._active_requests += 1

            try:
                # Check if auto-rotation is needed (but don't rotate during active request)
                if self._key_created_at and (time.time() - self._key_created_at) >= self._rotation_interval:
                    logger.warning(
                        f"DPoP keys are {time.time() - self._key_created_at:.0f}s old, "
                        f"rotation recommended (interval: {self._rotation_interval}s)"
                    )

                # Normalize URL: strip query and fragment per RFC 9449 Section 4.2
                # The htu claim MUST be the HTTP URI without query and fragment
                clean_url = normalize_dpop_url(http_url)

                # Use optional nonce (provided or stored)
                effective_nonce = nonce or self._nonce
                if effective_nonce:
                    logger.debug("Added nonce to DPoP proof")

                # Generate claims
                issued_time = int(time.time())
                jti = str(uuid.uuid4())

                claims = {
                    'jti': jti,
                    'htm': http_method.upper(),  # Ensure uppercase
                    'htu': clean_url,  # Clean URL without query/fragment
                    'iat': issued_time
                }

                # Add optional nonce claim (use provided or stored)
                if effective_nonce:
                    claims['nonce'] = effective_nonce

                # Add access token hash claim for API requests
                if access_token:
                    # Compute SHA-256 hash per RFC 9449 Section 4.1
                    claims['ath'] = compute_ath(access_token)
                    logger.debug("Added access token hash (ath) to DPoP proof")

                # Build headers with public JWK (per RFC 9449 Section 4.1)
                # JWK contains only public components: kty, e, n
                # Intentionally excludes private components: d, p, q, dp, dq, qi
                headers = {
                    'typ': 'dpop+jwt',
                    'alg': 'RS256',
                    'jwk': self._public_jwk
                }

                # Sign JWT with private key using PyJWT (same library as rest of SDK)
                token = jwt_encode(
                    claims,
                    self._rsa_key.export_key(),
                    algorithm='RS256',
                    headers=headers
                )

                # Lazy logging: only format strings if debug is enabled
                if logger.isEnabledFor(logging.DEBUG):
                    logger.debug(
                        f"Generated DPoP proof JWT (length: {len(token)} chars) - "
                        f"HTM: {claims['htm']}, HTU: {claims['htu'][:50]}..., "
                        f"ath: {'yes' if access_token else 'no'}, nonce: {'yes' if effective_nonce else 'no'}"
                    )

                return token

            finally:
                # Decrement active request counter
                self._active_requests -= 1

    def _export_public_jwk(self) -> Dict[str, str]:
        """
        Export ONLY public key components as JWK per RFC 7517.

        MUST NOT include private key components (d, p, q, dp, dq, qi).
        Per RFC 9449 Section 4.1, the jwk header MUST represent the public key
        and MUST NOT contain a private key.

        Returns:
            Dict[str, str]: JWK with only public components (kty, n, e)

        Security Note:
            This method uses jwcrypto.export_public() to ensure only public
            components are exported. The private key components (d, p, q, dp, dq, qi)
            are never included in the JWK.
        """
        # Export private key as PEM
        pem_key = self._rsa_key.export_key()

        # Create JWK from PEM
        jwk_obj = JWK.from_pem(pem_key)

        # Export as public JWK (automatically strips private components)
        public_jwk_json = jwk_obj.export_public()
        public_jwk = json.loads(public_jwk_json)

        # Verify no private components leaked BEFORE cleaning (defense in depth)
        # This check is critical for security and must not be bypassable with python -O
        private_components = {'d', 'p', 'q', 'dp', 'dq', 'qi'}
        leaked = private_components & set(public_jwk.keys())
        if leaked:
            raise ValueError(
                f"SECURITY VIOLATION: Private key components {leaked} found in exported JWK. "
                "This indicates a critical bug in JWK export logic."
            )

        # Keep only required components: kty, n, e
        # Remove any optional fields (kid, use, key_ops, alg, etc.)
        cleaned_jwk = {
            'kty': public_jwk['kty'],  # Key type: "RSA"
            'n': public_jwk['n'],      # Modulus (public)
            'e': public_jwk['e']       # Exponent (public)
        }

        logger.debug(
            f"Exported public JWK: kty={cleaned_jwk['kty']}, "
            f"n={cleaned_jwk['n'][:16]}..., e={cleaned_jwk['e']}"
        )

        return cleaned_jwk

    def set_nonce(self, nonce: str) -> None:
        """
        Store nonce from server response.

        Nonces are provided by the authorization server in the 'dpop-nonce'
        header and must be included in subsequent DPoP proofs.

        Args:
            nonce: Nonce value from dpop-nonce header
        """
        with self._lock:
            if nonce == "":
                logger.debug("Empty string nonce provided, treating as None")
                nonce = None
            elif nonce is not None:
                # Basic validation: nonce should be printable ASCII per RFC 9449 Section 8
                # RFC 9449 requires nonces to be unpredictable but doesn't mandate length
                if not nonce.isprintable():
                    logger.warning(
                        "Nonce contains non-printable characters. "
                        "This may indicate transmission corruption. "
                        "Storing anyway as server determines nonce requirements."
                    )
                elif len(nonce) < 8:
                    # Short nonces are unusual but not forbidden by RFC 9449
                    logger.debug(
                        f"Received short nonce (length={len(nonce)}). "
                        "This is unusual but permitted by RFC 9449."
                    )
            self._nonce = nonce
            # Security: Nonce values are not logged to prevent potential replay attack information leakage

    def get_nonce(self) -> Optional[str]:
        """
        Get stored nonce.

        Returns:
            Current nonce value or None if not set
        """
        with self._lock:
            return self._nonce

    def get_public_jwk(self) -> Dict[str, str]:
        """
        Get public key in JWK format.

        Returns:
            Dict[str, str]: Copy of the public JWK (kty, n, e)
        """
        with self._lock:
            return self._public_jwk.copy() if self._public_jwk else {}

    def get_key_age(self) -> float:
        """
        Get age of current key pair in seconds.

        Returns:
            Age in seconds, or 0 if keys not yet generated
        """
        with self._lock:
            if not self._key_created_at:
                return 0.0
            return time.time() - self._key_created_at
