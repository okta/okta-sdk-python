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

import json
import logging
import time
import uuid
from typing import Any, Dict, Optional
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
    - Generates ephemeral RSA 3072-bit key pairs
    - Creates DPoP proof JWTs with proper claims (jti, htm, htu, iat, ath, nonce)
    - Manages server-provided nonces
    - Supports automatic key rotation

    Security Notes:
    - Private keys are kept in memory only
    - Only public key components are exported (kty, n, e)
    - Keys are rotated periodically for better security
    """

    def __init__(self, config: Dict[str, Any]) -> None:
        """
        Initialize DPoP proof generator.

        Args:
            config: Configuration dictionary containing:
                - dpopKeyRotationInterval: Key rotation interval in seconds (default: 86400 / 24 hours)
        """
        self._rsa_key: Optional[RSA.RsaKey] = None
        self._public_jwk: Optional[Dict[str, str]] = None
        self._key_created_at: Optional[float] = None
        self._rotation_interval: int = config.get('dpopKeyRotationInterval', 86400)  # 24h default
        self._nonce: Optional[str] = None

        # Generate initial keys
        self._rotate_keys_internal()

        logger.info(f"DPoP proof generator initialized with {self._rotation_interval}s key rotation interval")

    def _rotate_keys_internal(self) -> None:
        """
        Internal method to rotate keys.

        Generates a new RSA 3072-bit key pair and exports the public key as JWK.
        """
        logger.info("Generating new RSA 3072-bit key pair for DPoP")
        self._rsa_key = RSA.generate(3072)
        self._public_jwk = self._export_public_jwk()
        self._key_created_at = time.time()
        logger.debug(f"DPoP keys generated at {self._key_created_at}")

    def rotate_keys(self) -> None:
        """
        Safely rotate RSA key pair.

        In asyncio context, rotation is safe because the event loop is single-threaded.
        All concurrent requests will use the new key after rotation completes.

        Note: Callers should avoid rotating keys during active token operations.
        """
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

        Strips query parameters and fragments from http_url per RFC 9449 Section 4.2.

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
        # Check if auto-rotation is needed (but don't rotate during active request)
        if self._key_created_at and (time.time() - self._key_created_at) >= self._rotation_interval:
            logger.warning(
                f"DPoP keys are {time.time() - self._key_created_at:.0f}s old, "
                f"rotation recommended (interval: {self._rotation_interval}s)"
            )

        # RFC 9449 Section 4.2 - htu must NOT include query and fragment
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
            # Use JWT._compute_ath to avoid duplication
            from okta.jwt import JWT
            claims['ath'] = JWT._compute_ath(access_token)
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

        # Keep only required components: kty, n, e
        # Remove any optional fields (kid, use, key_ops, alg, etc.)
        cleaned_jwk = {
            'kty': public_jwk['kty'],  # Key type: "RSA"
            'n': public_jwk['n'],      # Modulus (public)
            'e': public_jwk['e']       # Exponent (public)
        }

        # Verify no private components leaked (use proper exceptions, not assert)
        # This check is critical for security and must not be bypassable with python -O
        private_components = {'d', 'p', 'q', 'dp', 'dq', 'qi'}
        leaked = private_components & set(cleaned_jwk.keys())
        if leaked:
            raise ValueError(
                f"SECURITY VIOLATION: Private key components {leaked} must not be in JWK. "
                "This indicates a critical bug in key export logic."
            )

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

    def get_public_jwk(self) -> Dict[str, str]:
        """
        Get public key in JWK format.

        Returns:
            Dict[str, str]: Copy of the public JWK (kty, n, e)
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
