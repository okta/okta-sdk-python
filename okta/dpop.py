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

import base64
import hashlib
import json
import logging
import threading
import time
import uuid
from typing import Optional
from urllib.parse import urlparse, urlunparse

from Cryptodome.PublicKey import RSA
from jwcrypto.jwk import JWK
from jwt import encode as jwt_encode

logger = logging.getLogger("okta-sdk-python")


class DPoPProofGenerator:
    """
    Generates DPoP proof JWTs per RFC 9449.

    This class manages ephemeral RSA key pairs and generates DPoP proof JWTs
    for OAuth token requests and API requests. It handles key rotation,
    nonce management, and ensures RFC 9449 compliance.

    Key Features:
    - Generates ephemeral RSA 2048-bit key pairs
    - Creates DPoP proof JWTs with proper claims (jti, htm, htu, iat, ath, nonce)
    - Manages server-provided nonces
    - Supports automatic key rotation
    - Thread-safe for concurrent requests

    Security Notes:
    - Private keys are kept in memory only
    - Only public key components are exported (kty, n, e)
    - Keys are rotated periodically for better security
    """

    def __init__(self, config: dict):
        """
        Initialize DPoP proof generator.

        Args:
            config: Configuration dictionary containing:
                - dpopKeyRotationInterval: Key rotation interval in seconds (default: 86400 / 24 hours)
        """
        self._rsa_key: Optional[RSA.RsaKey] = None
        self._public_jwk: Optional[dict] = None
        self._key_created_at: Optional[float] = None
        self._rotation_interval: int = config.get('dpopKeyRotationInterval', 86400)  # 24h default
        self._nonce: Optional[str] = None
        self._lock = threading.Lock()  # Thread-safe lock for key operations
        self._active_requests = 0  # Track active requests for safe key rotation

        # Generate initial keys
        self._rotate_keys_internal()

        logger.info(f"DPoP proof generator initialized with {self._rotation_interval}s key rotation interval")

    def _rotate_keys_internal(self) -> None:
        """
        Internal method to rotate keys (not thread-safe, use rotate_keys()).

        Generates a new RSA 2048-bit key pair and exports the public key as JWK.
        """
        logger.info("Generating new RSA 2048-bit key pair for DPoP")
    self._rsa_key = RSA.generate(3072)
        self._public_jwk = self._export_public_jwk()
        self._key_created_at = time.time()
        logger.debug(f"DPoP keys generated at {self._key_created_at}")

    def rotate_keys(self) -> None:
        """
        Safely rotate RSA key pair.

        FIX #5: Waits for active requests to complete before rotating keys
        to prevent signature mismatch errors.

        This method is thread-safe and will block until all active requests
        using the current key have completed.
        """
        with self._lock:
            # Wait for all active requests to complete
            while self._active_requests > 0:
                logger.debug(f"Waiting for {self._active_requests} active requests before key rotation")
                time.sleep(0.1)

            # Now safe to rotate
            self._rotate_keys_internal()

            # Clear nonce as it was tied to old key
            self._nonce = None
            logger.info("DPoP keys rotated successfully, nonce cleared")

    def generate_proof_jwt(
        self,
        http_method: str,
        http_url: str,
        access_token: Optional[str] = None,
        nonce: Optional[str] = None
    ) -> str:
        """
        Generate DPoP proof JWT per RFC 9449.

        FIX #1: Strips query parameters and fragments from http_url per RFC 9449 Section 4.2.

        Args:
            http_method: HTTP method (GET, POST, etc.)
            http_url: Full HTTP URL (query and fragment will be stripped)
            access_token: Access token for 'ath' claim (optional, for API requests)
            nonce: Server-provided nonce (optional, overrides stored nonce)

        Returns:
            DPoP proof JWT as string

        Raises:
            ValueError: If required parameters are missing or invalid

        Example:
            >>> generator = DPoPProofGenerator({'dpopKeyRotationInterval': 86400})
            >>> proof = generator.generate_proof_jwt(
            ...     'GET',
            ...     'https://example.okta.com/api/v1/users?limit=10',
            ...     access_token='eyJhbG...'
            ... )
        """
        # FIX #5: Increment active request counter (thread-safe)
        with self._lock:
            self._active_requests += 1

        try:
            # Check if auto-rotation is needed (but don't rotate during active request)
            if self._should_rotate_keys():
                logger.warning(
                    f"DPoP keys are {time.time() - self._key_created_at:.0f}s old, "
                    f"rotation recommended (interval: {self._rotation_interval}s)"
                )

            # FIX #1: RFC 9449 Section 4.2 - htu must NOT include query and fragment
            parsed_url = urlparse(http_url)
            clean_url = urlunparse((
                parsed_url.scheme,
                parsed_url.netloc,
                parsed_url.path,
                '',  # params (empty)
                '',  # query (empty)
                ''   # fragment (empty)
            ))

            if parsed_url.query or parsed_url.fragment:
                logger.debug(
                    f"Stripped query/fragment from URL for DPoP htu claim: "
                    f"{http_url} -> {clean_url}"
                )

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
            effective_nonce = nonce or self._nonce
            if effective_nonce:
                claims['nonce'] = effective_nonce
                logger.debug(f"Added nonce to DPoP proof: {effective_nonce[:8]}...")

            # Add access token hash claim for API requests
            if access_token:
                claims['ath'] = self._compute_access_token_hash(access_token)
                logger.debug("Added access token hash (ath) to DPoP proof")

            # Build headers with public JWK
            headers = {
                'typ': 'dpop+jwt',
                'alg': 'RS256',
                'jwk': self._public_jwk
            }

            # Sign JWT with private key
            token = jwt_encode(
                claims,
                self._rsa_key.export_key(),
                algorithm='RS256',
                headers=headers
            )

            logger.debug(
                f"Generated DPoP proof JWT: jti={jti}, htm={claims['htm']}, "
                f"htu={claims['htu'][:50]}..., ath={'yes' if access_token else 'no'}, "
                f"nonce={'yes' if effective_nonce else 'no'}"
            )

            return token

        finally:
            # FIX #5: Decrement active request counter (thread-safe)
            with self._lock:
                self._active_requests -= 1

    def _should_rotate_keys(self) -> bool:
        """
        Check if keys should be rotated based on age.

        Returns:
            True if keys are older than rotation interval, False otherwise
        """
        if not self._key_created_at:
            return True
        age = time.time() - self._key_created_at
        return age >= self._rotation_interval

    def _compute_access_token_hash(self, access_token: str) -> str:
        """
        Compute SHA-256 hash of access token for 'ath' claim.

        Per RFC 9449 Section 4.1: The value MUST be the result of a base64url
        encoding the SHA-256 hash of the ASCII encoding of the associated
        access token's value.

        Args:
            access_token: The access token to hash

        Returns:
            Base64url-encoded SHA-256 hash (without padding)
        """
        # SHA-256 hash of ASCII-encoded access token
        hash_bytes = hashlib.sha256(access_token.encode('ascii')).digest()

        # Base64url encode (no padding per RFC 7515 Section 2)
        ath = base64.urlsafe_b64encode(hash_bytes).rstrip(b'=').decode('ascii')

        logger.debug(f"Computed access token hash: {ath[:16]}...")
        return ath

    def _export_public_jwk(self) -> dict:
        """
        Export ONLY public key components as JWK per RFC 7517.

        FIX #2: MUST NOT include private key components (d, p, q, dp, dq, qi).
        Per RFC 9449 Section 4.1, the jwk header MUST represent the public key
        and MUST NOT contain a private key.

        Returns:
            dict: JWK with only public components (kty, n, e)

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

        # Keep only required components: kty, n, e
        # Remove any optional fields (kid, use, key_ops, alg, etc.)
        cleaned_jwk = {
            'kty': public_jwk['kty'],  # Key type: "RSA"
            'n': public_jwk['n'],      # Modulus (public)
            'e': public_jwk['e']       # Exponent (public)
        }

        # FIX #2: Verify no private components leaked
        assert 'd' not in cleaned_jwk, "Private key 'd' must not be in JWK"
        assert 'p' not in cleaned_jwk, "Private prime 'p' must not be in JWK"
        assert 'q' not in cleaned_jwk, "Private prime 'q' must not be in JWK"
        assert 'dp' not in cleaned_jwk, "Private 'dp' must not be in JWK"
        assert 'dq' not in cleaned_jwk, "Private 'dq' must not be in JWK"
        assert 'qi' not in cleaned_jwk, "Private 'qi' must not be in JWK"

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
        self._nonce = nonce
        logger.debug(f"Stored DPoP nonce: {nonce[:8] if nonce else 'None'}...")

    def get_nonce(self) -> Optional[str]:
        """
        Get stored nonce.

        Returns:
            Current nonce value or None if not set
        """
        return self._nonce

    def get_public_jwk(self) -> dict:
        """
        Get public key in JWK format.

        Returns:
            Copy of the public JWK (kty, n, e)
        """
        return self._public_jwk.copy() if self._public_jwk else {}

    def get_key_age(self) -> float:
        """
        Get age of current key pair in seconds.

        Returns:
            Age in seconds, or 0 if keys not yet generated
        """
        if not self._key_created_at:
            return 0.0
        return time.time() - self._key_created_at

    def get_active_requests(self) -> int:
        """
        Get number of active requests using current key.

        Returns:
            Number of active requests
        """
        with self._lock:
            return self._active_requests
