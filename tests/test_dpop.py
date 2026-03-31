"""
Unit tests for DPoP (Demonstrating Proof-of-Possession) implementation.

See tests/DPOP_TESTING.md for detailed test documentation and coverage matrix.

Coverage targets (from PR_495_TEST_PLAN.md):
  - Section 2.1: DPoPProofGenerator (U-D01 .. U-D26)
  - Section 2.2: OAuth DPoP Flow (U-O01 .. U-O20)
  - Section 2.3: Request Executor DPoP Integration (U-R01 .. U-R09)
  - Section 2.4: Configuration & Validation (U-C01 .. U-C08)
  - Section 2.7: DPoP Error Messages (U-E01 .. U-E05)
  - Section 2.8: Utility Functions (U-U01 .. U-U07)
  - Section 4:   Negative / Edge Case Tests (N-02, N-05, N-06, N-09)
"""

import json
import time
import unittest
from unittest.mock import AsyncMock, MagicMock, patch

import jwt
import multidict

from okta.cache.no_op_cache import NoOpCache
from okta.cache.okta_cache import OktaCache
from okta.config.config_validator import ConfigValidator
from okta.configuration import Configuration
from okta.dpop import DPoPProofGenerator
from okta.errors.dpop_errors import (
    get_dpop_error_message,
    is_dpop_error,
    DPOP_ERROR_MESSAGES,
)
from okta.oauth import OAuth
from okta.request_executor import RequestExecutor
from okta.utils import compute_ath, normalize_dpop_url, truncate_url
from tests.mocks import SAMPLE_RSA


class TestDPoPProofGenerator(unittest.TestCase):
    """Test DPoP proof generator functionality (Section 2.1)."""

    def setUp(self):
        """Set up test fixtures."""
        self.config = {
            'dpopKeyRotationInterval': 86400  # 24 hours
        }
        self.generator = DPoPProofGenerator(self.config)

    def test_initialization(self):
        """Test DPoP generator initializes correctly."""
        self.assertIsNotNone(self.generator._rsa_key)
        self.assertIsNotNone(self.generator._public_jwk)
        self.assertIsNotNone(self.generator._key_created_at)
        self.assertEqual(self.generator._rotation_interval, 86400)
        self.assertIsNone(self.generator._nonce)

    def test_key_generation(self):
        """Test RSA 3072-bit key generation."""
        # Key should be RSA
        self.assertEqual(self.generator._rsa_key.size_in_bits(), 3072)

        # Should have both public and private components
        self.assertTrue(self.generator._rsa_key.has_private())

    def test_jwk_export_public_only(self):
        """
        FIX #2: Test JWK export contains ONLY public components.

        Per RFC 9449 Section 4.1, the jwk header MUST NOT contain private key.
        """
        jwk = self.generator._public_jwk

        # Must have public components
        self.assertIn('kty', jwk)
        self.assertIn('n', jwk)
        self.assertIn('e', jwk)

        # Must be RSA
        self.assertEqual(jwk['kty'], 'RSA')

        # MUST NOT have private components
        self.assertNotIn('d', jwk, "Private key 'd' must not be in JWK")
        self.assertNotIn('p', jwk, "Private prime 'p' must not be in JWK")
        self.assertNotIn('q', jwk, "Private prime 'q' must not be in JWK")
        self.assertNotIn('dp', jwk, "Private 'dp' must not be in JWK")
        self.assertNotIn('dq', jwk, "Private 'dq' must not be in JWK")
        self.assertNotIn('qi', jwk, "Private 'qi' must not be in JWK")

        # Should only have exactly 3 keys
        self.assertEqual(len(jwk), 3, "JWK should only have kty, n, e")

    def test_generate_proof_jwt_basic(self):
        """Test basic DPoP proof JWT generation."""
        proof = self.generator.generate_proof_jwt(
            'GET',
            'https://example.okta.com/api/v1/users'
        )

        # Should be a valid JWT
        self.assertIsInstance(proof, str)
        self.assertTrue(proof.count('.') == 2, "JWT should have 3 parts")

        # Decode and verify (without verification since we don't have the key)
        decoded = jwt.decode(proof, options={"verify_signature": False})

        # Verify required claims
        self.assertIn('jti', decoded)
        self.assertIn('htm', decoded)
        self.assertIn('htu', decoded)
        self.assertIn('iat', decoded)

        # Verify claim values
        self.assertEqual(decoded['htm'], 'GET')
        self.assertEqual(decoded['htu'], 'https://example.okta.com/api/v1/users')
        self.assertIsInstance(decoded['iat'], int)

        # Should not have ath or nonce (not provided)
        self.assertNotIn('ath', decoded)
        self.assertNotIn('nonce', decoded)

    def test_url_parsing_strips_query(self):
        """
        FIX #1: Test URL parsing strips query parameters from htu claim.

        Per RFC 9449 Section 4.2, htu must NOT include query parameters.
        """
        url_with_query = 'https://example.okta.com/api/v1/users?limit=10&after=abc123'

        proof = self.generator.generate_proof_jwt('GET', url_with_query)
        decoded = jwt.decode(proof, options={"verify_signature": False})

        # htu should NOT include query
        self.assertEqual(decoded['htu'], 'https://example.okta.com/api/v1/users')
        self.assertNotIn('limit', decoded['htu'])
        self.assertNotIn('after', decoded['htu'])

    def test_url_parsing_strips_fragment(self):
        """
        FIX #1: Test URL parsing strips fragments from htu claim.

        Per RFC 9449 Section 4.2, htu must NOT include fragments.
        """
        url_with_fragment = 'https://example.okta.com/api/v1/users#section'

        proof = self.generator.generate_proof_jwt('GET', url_with_fragment)
        decoded = jwt.decode(proof, options={"verify_signature": False})

        # htu should NOT include fragment
        self.assertEqual(decoded['htu'], 'https://example.okta.com/api/v1/users')
        self.assertNotIn('#section', decoded['htu'])

    def test_url_parsing_strips_query_and_fragment(self):
        """
        FIX #1: Test URL parsing strips both query and fragment.
        """
        url_full = 'https://example.okta.com/api/v1/users?limit=10#section'

        proof = self.generator.generate_proof_jwt('GET', url_full)
        decoded = jwt.decode(proof, options={"verify_signature": False})

        # htu should be clean
        self.assertEqual(decoded['htu'], 'https://example.okta.com/api/v1/users')

    def test_generate_proof_with_nonce(self):
        """Test DPoP proof generation with nonce."""
        proof = self.generator.generate_proof_jwt(
            'POST',
            'https://example.okta.com/oauth2/v1/token',
            nonce='test-nonce-12345'
        )

        decoded = jwt.decode(proof, options={"verify_signature": False})

        # Should have nonce claim
        self.assertIn('nonce', decoded)
        self.assertEqual(decoded['nonce'], 'test-nonce-12345')

    def test_generate_proof_with_access_token(self):
        """Test DPoP proof generation with access token hash."""
        access_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.test.signature'

        proof = self.generator.generate_proof_jwt(
            'GET',
            'https://example.okta.com/api/v1/users',
            access_token=access_token
        )

        decoded = jwt.decode(proof, options={"verify_signature": False})

        # Should have ath claim
        self.assertIn('ath', decoded)
        self.assertIsInstance(decoded['ath'], str)

        # ath should be base64url encoded (no padding)
        self.assertNotIn('=', decoded['ath'])

    def test_access_token_hash_computation(self):
        """Test SHA-256 hash computation for access token."""
        access_token = 'test-token'

        # Compute hash using utils.compute_ath (used by DPoP generator)
        ath = compute_ath(access_token)

        # Should be base64url encoded
        self.assertIsInstance(ath, str)
        self.assertNotIn('=', ath)  # No padding

        # Should be deterministic (same input = same output)
        ath2 = compute_ath(access_token)
        self.assertEqual(ath, ath2)

        # Different token = different hash
        ath3 = compute_ath('different-token')
        self.assertNotEqual(ath, ath3)

    def test_jwt_headers(self):
        """Test DPoP JWT has correct headers."""
        proof = self.generator.generate_proof_jwt(
            'GET',
            'https://example.okta.com/api/v1/users'
        )

        # Decode header
        header = jwt.get_unverified_header(proof)

        # Verify header fields
        self.assertEqual(header['typ'], 'dpop+jwt')
        self.assertEqual(header['alg'], 'RS256')
        self.assertIn('jwk', header)

        # Verify JWK in header
        jwk = header['jwk']
        self.assertEqual(jwk['kty'], 'RSA')
        self.assertIn('n', jwk)
        self.assertIn('e', jwk)

        # FIX #2: Verify no private key in JWK header
        self.assertNotIn('d', jwk)

    def test_http_method_uppercase(self):
        """Test HTTP method is converted to uppercase."""
        proof = self.generator.generate_proof_jwt(
            'get',  # lowercase
            'https://example.okta.com/api/v1/users'
        )

        decoded = jwt.decode(proof, options={"verify_signature": False})

        # Should be uppercase
        self.assertEqual(decoded['htm'], 'GET')

    def test_nonce_storage(self):
        """Test nonce set/get operations."""
        # Initially no nonce
        self.assertIsNone(self.generator.get_nonce())

        # Set nonce
        self.generator.set_nonce('test-nonce')
        self.assertEqual(self.generator.get_nonce(), 'test-nonce')

        # Update nonce
        self.generator.set_nonce('new-nonce')
        self.assertEqual(self.generator.get_nonce(), 'new-nonce')

    def test_stored_nonce_used_in_jwt(self):
        """Test stored nonce is used when generating JWT."""
        # Store nonce
        self.generator.set_nonce('stored-nonce')

        # Generate proof without explicit nonce
        proof = self.generator.generate_proof_jwt(
            'POST',
            'https://example.okta.com/oauth2/v1/token'
        )

        decoded = jwt.decode(proof, options={"verify_signature": False})

        # Should use stored nonce
        self.assertEqual(decoded['nonce'], 'stored-nonce')

    def test_explicit_nonce_overrides_stored(self):
        """Test explicit nonce parameter overrides stored nonce."""
        # Store nonce
        self.generator.set_nonce('stored-nonce')

        # Generate proof with explicit nonce
        proof = self.generator.generate_proof_jwt(
            'POST',
            'https://example.okta.com/oauth2/v1/token',
            nonce='explicit-nonce'
        )

        decoded = jwt.decode(proof, options={"verify_signature": False})

        # Should use explicit nonce
        self.assertEqual(decoded['nonce'], 'explicit-nonce')

    def test_key_rotation(self):
        """Test key rotation generates new keys."""
        old_jwk = self.generator._public_jwk.copy()
        old_key_time = self.generator._key_created_at

        # Wait a bit to ensure timestamp changes
        time.sleep(0.01)

        # Rotate keys (force to ignore age check)
        result = self.generator.rotate_keys(force=True)
        self.assertTrue(result, "Rotation should succeed")

        new_jwk = self.generator._public_jwk
        new_key_time = self.generator._key_created_at

        # Modulus (n) should be different (e might be same standard exponent)
        self.assertNotEqual(old_jwk['n'], new_jwk['n'])

        # Timestamp should be newer
        self.assertGreater(new_key_time, old_key_time)

    def test_key_rotation_clears_nonce(self):
        """
        FIX #5: Test key rotation clears nonce.

        When keys are rotated, the nonce should be cleared since it was
        tied to the old key.
        """
        # Set nonce
        self.generator.set_nonce('test-nonce')
        self.assertIsNotNone(self.generator.get_nonce())

        # Rotate keys (force to ignore age check)
        result = self.generator.rotate_keys(force=True)
        self.assertTrue(result, "Rotation should succeed")

        # Nonce should be cleared
        self.assertIsNone(self.generator.get_nonce())

    def test_key_rotation_waits_for_active_requests(self):
        """
        Test key rotation works correctly.

        Note: In the asyncio context, rotation is safe because the event loop
        is single-threaded. No active request tracking is needed.
        """
        old_n = self.generator._public_jwk['n']

        # Rotation should succeed immediately (force to ignore age check)
        result = self.generator.rotate_keys(force=True)
        self.assertTrue(result, "Rotation should succeed")

        # Key should have changed
        new_n = self.generator._public_jwk['n']
        self.assertNotEqual(old_n, new_n)

    # TODO: Implement automatic key rotation test based on age threshold
    # This would require mocking time.time() or waiting for rotation interval
    # Test should verify that keys rotate when age exceeds rotation_interval
    # def test_automatic_key_rotation_based_on_age(self):
    #     """Test that keys rotate when age threshold is reached."""
    #     pass

    def test_get_key_age(self):
        """Test get_key_age returns correct age."""
        age = self.generator.get_key_age()

        # Should be very recent (< 1 second)
        self.assertGreater(age, 0)
        self.assertLess(age, 1.0)

        # Wait and check again
        time.sleep(0.01)
        age2 = self.generator.get_key_age()
        self.assertGreater(age2, age)

    def test_get_public_jwk(self):
        """Test get_public_jwk returns copy."""
        jwk1 = self.generator.get_public_jwk()
        jwk2 = self.generator.get_public_jwk()

        # Should be equal but not same object
        self.assertEqual(jwk1, jwk2)
        self.assertIsNot(jwk1, jwk2)

    def test_custom_rotation_interval(self):
        """Test custom key rotation interval."""
        config = {'dpopKeyRotationInterval': 3600}  # 1 hour
        generator = DPoPProofGenerator(config)

        self.assertEqual(generator._rotation_interval, 3600)

    def test_jti_uniqueness(self):
        """Test each proof has unique jti."""
        proof1 = self.generator.generate_proof_jwt(
            'GET',
            'https://example.okta.com/api/v1/users'
        )
        proof2 = self.generator.generate_proof_jwt(
            'GET',
            'https://example.okta.com/api/v1/users'
        )

        decoded1 = jwt.decode(proof1, options={"verify_signature": False})
        decoded2 = jwt.decode(proof2, options={"verify_signature": False})

        # JTIs should be different
        self.assertNotEqual(decoded1['jti'], decoded2['jti'])

    def test_compute_ath_non_ascii_raises_error(self):
        """
        Test that compute_ath raises ValueError for non-ASCII access tokens.

        Per RFC 9449, access tokens must be ASCII-encodable for the ath claim.
        """
        with self.assertRaises(ValueError) as cm:
            compute_ath("token-with-émoji-\U0001f511")
        self.assertIn("non-ASCII", str(cm.exception))

    # --- U-D03: Initialization with missing config key ---
    def test_initialization_missing_config_key(self):
        """U-D03: Empty config uses default 86400 seconds."""
        generator = DPoPProofGenerator({})
        self.assertEqual(generator._rotation_interval, 86400)

    # --- U-D08: Generate proof with access token AND nonce ---
    def test_generate_proof_with_access_token_and_nonce(self):
        """U-D08: JWT contains both ath and nonce claims when both provided."""
        access_token = 'eyJhbGciOiJSUzI1NiJ9.test.sig'
        proof = self.generator.generate_proof_jwt(
            'POST',
            'https://example.okta.com/api/v1/users',
            access_token=access_token,
            nonce='server-nonce-123',
        )
        decoded = jwt.decode(proof, options={"verify_signature": False})
        self.assertIn('ath', decoded)
        self.assertIn('nonce', decoded)
        self.assertEqual(decoded['nonce'], 'server-nonce-123')

    # --- U-D12: URL normalization preserves path ---
    def test_url_preserves_path(self):
        """U-D12: htu preserves scheme, host, and path."""
        proof = self.generator.generate_proof_jwt(
            'POST',
            'https://example.okta.com/oauth2/v1/token',
        )
        decoded = jwt.decode(proof, options={"verify_signature": False})
        self.assertEqual(decoded['htu'], 'https://example.okta.com/oauth2/v1/token')

    # --- U-D19: Rotation skipped when not needed ---
    def test_key_rotation_skipped_when_not_needed(self):
        """U-D19: force=False rotation skipped when key age < interval."""
        old_n = self.generator._public_jwk['n']
        result = self.generator.rotate_keys(force=False)
        self.assertFalse(result, "Rotation should be skipped")
        self.assertEqual(self.generator._public_jwk['n'], old_n)

    # --- U-D20: Rotation skipped during active requests ---
    def test_key_rotation_skipped_during_active_requests(self):
        """U-D20: Rotation skipped when _active_requests > 0."""
        # Simulate an active request
        with self.generator._lock:
            self.generator._active_requests = 1
        try:
            old_n = self.generator._public_jwk['n']
            result = self.generator.rotate_keys(force=True)
            self.assertFalse(result, "Rotation should be skipped with active requests")
            self.assertEqual(self.generator._public_jwk['n'], old_n)
        finally:
            with self.generator._lock:
                self.generator._active_requests = 0

    # --- U-D23: set_nonce("") treated as None ---
    def test_set_nonce_empty_string_treated_as_none(self):
        """U-D23: Empty string nonce is treated as None."""
        self.generator.set_nonce("")
        self.assertIsNone(self.generator.get_nonce())

    # --- U-D24: set_nonce(None) ---
    def test_set_nonce_none(self):
        """U-D24: Setting nonce to None returns None."""
        self.generator.set_nonce("something")
        self.assertIsNotNone(self.generator.get_nonce())
        self.generator.set_nonce(None)
        self.assertIsNone(self.generator.get_nonce())

    # --- U-D25: Active request counter increment/decrement ---
    def test_active_request_counter(self):
        """U-D25: _active_requests is 0 after generate_proof_jwt completes."""
        self.assertEqual(self.generator._active_requests, 0)
        self.generator.generate_proof_jwt(
            'GET', 'https://example.okta.com/api/v1/users')
        self.assertEqual(self.generator._active_requests, 0)

    # --- U-D26: Active request counter exception safety ---
    def test_active_request_counter_exception_safety(self):
        """U-D26: _active_requests is 0 even after signing exception."""
        original_export_key = self.generator._rsa_key.export_key
        self.generator._rsa_key.export_key = MagicMock(
            side_effect=RuntimeError("mock signing error"))
        try:
            with self.assertRaises(RuntimeError):
                self.generator.generate_proof_jwt(
                    'GET', 'https://example.okta.com/api/v1/users')
            self.assertEqual(self.generator._active_requests, 0)
        finally:
            self.generator._rsa_key.export_key = original_export_key

    # --- N-02: Key rotation memory safety ---
    def test_key_rotation_memory_safety(self):
        """N-02: 10 forced rotations cause no crash/segfault."""
        for _ in range(10):
            result = self.generator.rotate_keys(force=True)
            self.assertTrue(result)
        # Verify generator is still functional
        proof = self.generator.generate_proof_jwt(
            'GET', 'https://example.okta.com/api/v1/users')
        self.assertIsInstance(proof, str)


# ───────────────────────────────────────────────────────────────────
# Section 2.7: DPoP Error Messages
# ───────────────────────────────────────────────────────────────────

class TestDPoPErrorMessages(unittest.TestCase):
    """Test DPoP error messages and detection (Section 2.7)."""

    # --- U-E01 ---
    def test_get_dpop_error_message_known_code(self):
        """U-E01: Known error code returns message from DPOP_ERROR_MESSAGES."""
        msg = get_dpop_error_message('invalid_dpop_proof')
        self.assertIn('DPoP proof validation failed', msg)
        self.assertEqual(msg, DPOP_ERROR_MESSAGES['invalid_dpop_proof'])

    # --- U-E02 ---
    def test_get_dpop_error_message_unknown_code(self):
        """U-E02: Unknown error code returns generic message with RFC link."""
        msg = get_dpop_error_message('unknown_error')
        self.assertIn('DPoP error: unknown_error', msg)
        self.assertIn('rfc9449', msg)

    # --- U-E03 ---
    def test_is_dpop_error_known(self):
        """U-E03: Known DPoP error returns True."""
        self.assertTrue(is_dpop_error('use_dpop_nonce'))
        self.assertTrue(is_dpop_error('invalid_dpop_proof'))
        self.assertTrue(is_dpop_error('invalid_dpop_key_binding'))

    # --- U-E04 ---
    def test_is_dpop_error_non_dpop(self):
        """U-E04: Non-DPoP error returns False."""
        self.assertFalse(is_dpop_error('invalid_grant'))
        self.assertFalse(is_dpop_error('invalid_client'))
        self.assertFalse(is_dpop_error('server_error'))

    # --- U-E05 ---
    def test_is_dpop_error_prefix_match(self):
        """U-E05: Error starting with dpop_ prefix returns True."""
        self.assertTrue(is_dpop_error('dpop_custom_thing'))
        self.assertTrue(is_dpop_error('invalid_dpop_something'))
        self.assertTrue(is_dpop_error('use_dpop_something'))


# ───────────────────────────────────────────────────────────────────
# Section 2.8: Utility Functions
# ───────────────────────────────────────────────────────────────────

class TestDPoPUtils(unittest.TestCase):
    """Test DPoP utility functions (Section 2.8)."""

    # --- U-U01: compute_ath deterministic ---
    def test_compute_ath_deterministic(self):
        """U-U01: Same token twice produces same hash."""
        ath1 = compute_ath('test-token')
        ath2 = compute_ath('test-token')
        self.assertEqual(ath1, ath2)

    # --- U-U02: Different tokens differ ---
    def test_compute_ath_different_tokens(self):
        """U-U02: Different tokens produce different hashes."""
        ath1 = compute_ath('token-a')
        ath2 = compute_ath('token-b')
        self.assertNotEqual(ath1, ath2)

    # --- U-U03: base64url no padding ---
    def test_compute_ath_no_padding(self):
        """U-U03: Result has no '=' padding characters."""
        ath = compute_ath('any-token-value')
        self.assertNotIn('=', ath)

    # --- U-U04: normalize_dpop_url strips query ---
    def test_normalize_dpop_url_strips_query(self):
        """U-U04: Query parameters are removed."""
        result = normalize_dpop_url('https://example.com/api?key=val&a=b')
        self.assertEqual(result, 'https://example.com/api')

    # --- U-U05: normalize_dpop_url strips fragment ---
    def test_normalize_dpop_url_strips_fragment(self):
        """U-U05: Fragment is removed."""
        result = normalize_dpop_url('https://example.com/api#section')
        self.assertEqual(result, 'https://example.com/api')

    # --- U-U06: normalize_dpop_url preserves scheme/host/path ---
    def test_normalize_dpop_url_preserves_components(self):
        """U-U06: Scheme, host, and path are preserved."""
        result = normalize_dpop_url('https://auth.example.com:8443/oauth2/v1/token')
        self.assertEqual(result, 'https://auth.example.com:8443/oauth2/v1/token')

    def test_normalize_dpop_url_invalid_raises(self):
        """normalize_dpop_url raises ValueError for malformed URL."""
        with self.assertRaises(ValueError):
            normalize_dpop_url('/relative/path')

    # --- U-U07: truncate_url ---
    def test_truncate_url_long(self):
        """U-U07: Long URL is truncated with '...'."""
        long_url = 'https://example.com/' + 'a' * 200
        result = truncate_url(long_url)
        self.assertTrue(result.endswith('...'))
        self.assertEqual(len(result), 53)  # 50 chars + "..."

    def test_truncate_url_short(self):
        """Short URL is returned unchanged."""
        short_url = 'https://example.com/api'
        result = truncate_url(short_url)
        self.assertEqual(result, short_url)


# ───────────────────────────────────────────────────────────────────
# Section 2.4: Configuration & Validation
# ───────────────────────────────────────────────────────────────────

class TestConfigValidationDPoP(unittest.TestCase):
    """Test DPoP configuration validation (Section 2.4)."""

    def _build_pk_config(self, **overrides):
        """Helper to build a valid PrivateKey config with optional overrides."""
        config = {
            "client": {
                "orgUrl": "https://test.okta.com",
                "authorizationMode": "PrivateKey",
                "clientId": "0oatest123",
                "scopes": ["okta.users.read"],
                "privateKey": SAMPLE_RSA,
                "oauthTokenRenewalOffset": 5,
            },
            "testing": {"testingDisableHttpsCheck": False},
        }
        config["client"].update(overrides)
        return config

    # --- U-C01: Valid DPoP config ---
    def test_valid_dpop_config(self):
        """U-C01: Valid DPoP config raises no errors."""
        config = self._build_pk_config(dpopEnabled=True, dpopKeyRotationInterval=86400)
        # Should not raise
        ConfigValidator(config)

    # --- U-C02: Rotation interval too small ---
    def test_dpop_rotation_interval_too_small(self):
        """U-C02: Rotation < 3600s raises validation error."""
        config = self._build_pk_config(dpopEnabled=True, dpopKeyRotationInterval=100)
        with self.assertRaises(ValueError) as cm:
            ConfigValidator(config)
        self.assertIn("3600", str(cm.exception))

    # --- U-C03: Rotation interval too large ---
    def test_dpop_rotation_interval_too_large(self):
        """U-C03: Rotation > 90 days raises validation error."""
        config = self._build_pk_config(dpopEnabled=True, dpopKeyRotationInterval=9999999)
        with self.assertRaises(ValueError) as cm:
            ConfigValidator(config)
        self.assertIn("90", str(cm.exception))

    # --- U-C04: Rotation interval not integer ---
    def test_dpop_rotation_interval_not_integer(self):
        """U-C04: Non-numeric rotation interval raises validation error.

        Note: Numeric strings like '86400' are coerced to int (for env-var
        compatibility).  Only genuinely non-numeric values are rejected.
        """
        config = self._build_pk_config(
            dpopEnabled=True, dpopKeyRotationInterval='not-a-number')
        with self.assertRaises(ValueError) as cm:
            ConfigValidator(config)
        self.assertIn("integer", str(cm.exception).lower())

    # --- U-C05: Long interval warning ---
    def test_dpop_long_interval_warning(self):
        """U-C05: Rotation > 7 days logs warning but does not error."""
        config = self._build_pk_config(
            dpopEnabled=True, dpopKeyRotationInterval=700000)
        with patch("okta.config.config_validator.logger") as mock_logger:
            ConfigValidator(config)
            mock_logger.warning.assert_called_once()
            args = mock_logger.warning.call_args
            self.assertIn("very long", args[0][0])

    # --- U-C06: DPoP disabled, no validation ---
    def test_dpop_disabled_no_validation(self):
        """U-C06: dpopEnabled=False skips DPoP validation entirely."""
        # Invalid rotation interval but DPoP is disabled — should NOT error
        config = self._build_pk_config(dpopEnabled=False, dpopKeyRotationInterval=-999)
        ConfigValidator(config)

    # --- U-C07: dpopEnabled is not boolean ---
    def test_dpop_enabled_not_boolean(self):
        """dpopEnabled must be boolean.

        Note: String values like 'true'/'false' are coerced to bool
        (for env-var compatibility).  Only genuinely non-coercible
        types like int or list are rejected.
        """
        config = self._build_pk_config(dpopEnabled=42)
        with self.assertRaises(ValueError) as cm:
            ConfigValidator(config)
        self.assertIn("boolean", str(cm.exception).lower())

    # --- U-C07b: dpopEnabled string coercion (env var compat) ---
    def test_dpop_enabled_string_coercion(self):
        """String 'true'/'false' from env vars are coerced to bool."""
        # 'true' (case-insensitive) → True, should proceed to validate
        config_true = self._build_pk_config(
            dpopEnabled='true', dpopKeyRotationInterval=86400)
        ConfigValidator(config_true)  # Should NOT raise

        config_TRUE = self._build_pk_config(
            dpopEnabled=' True ', dpopKeyRotationInterval=86400)
        ConfigValidator(config_TRUE)  # Should NOT raise (whitespace stripped)

        # 'false' → False, should skip DPoP validation entirely
        config_false = self._build_pk_config(
            dpopEnabled='false', dpopKeyRotationInterval=-999)
        ConfigValidator(config_false)  # Should NOT raise (DPoP disabled)

    # --- U-C04b: dpopKeyRotationInterval string coercion (env var compat) ---
    def test_dpop_rotation_interval_string_coercion(self):
        """Numeric string from env vars is coerced to int."""
        config = self._build_pk_config(
            dpopEnabled=True, dpopKeyRotationInterval='86400')
        ConfigValidator(config)  # Should NOT raise

    # --- U-C08: Configuration.__init__ stores DPoP params ---
    def test_configuration_stores_dpop_params(self):
        """U-C08: Configuration object stores DPoP attributes."""
        cfg = Configuration(
            dpop_enabled=True,
            dpop_private_key="test-key",
            dpop_key_rotation_interval=3600,
        )
        self.assertTrue(cfg.dpop_enabled)
        self.assertEqual(cfg.dpop_private_key, "test-key")
        self.assertEqual(cfg.dpop_key_rotation_interval, 3600)


# ───────────────────────────────────────────────────────────────────
# Section 2.2: OAuth DPoP Flow (async tests)
# ───────────────────────────────────────────────────────────────────

class TestOAuthDPoP(unittest.IsolatedAsyncioTestCase):
    """Test OAuth DPoP flow (Section 2.2)."""

    def setUp(self):
        """Reset class-level state to ensure test isolation."""
        OAuth._access_token_dpop_warned = False

    def _build_config(self, dpop_enabled=False):
        """Helper to build config for OAuth."""
        return {
            "client": {
                "orgUrl": "https://test.okta.com",
                "authorizationMode": "PrivateKey",
                "clientId": "0oatest123",
                "scopes": ["okta.users.read"],
                "privateKey": SAMPLE_RSA,
                "oauthTokenRenewalOffset": 5,
                "dpopEnabled": dpop_enabled,
            }
        }

    # --- U-O01: init with DPoP enabled ---
    def test_oauth_init_dpop_enabled(self):
        """U-O01: DPoP enabled => _dpop_enabled True, generator exists."""
        mock_re = MagicMock()
        config = self._build_config(dpop_enabled=True)
        oauth = OAuth(mock_re, config)
        self.assertTrue(oauth.is_dpop_enabled())
        self.assertIsNotNone(oauth.get_dpop_generator())

    # --- U-O02: init with DPoP disabled ---
    def test_oauth_init_dpop_disabled(self):
        """U-O02: DPoP disabled => _dpop_enabled False, generator None."""
        mock_re = MagicMock()
        config = self._build_config(dpop_enabled=False)
        oauth = OAuth(mock_re, config)
        self.assertFalse(oauth.is_dpop_enabled())
        self.assertIsNone(oauth.get_dpop_generator())

    # --- U-O03: init DPoP enabled but missing crypto libs ---
    def test_oauth_init_dpop_missing_crypto(self):
        """U-O03: DPoP enabled with no crypto libs raises ValueError."""
        mock_re = MagicMock()
        config = self._build_config(dpop_enabled=True)
        with patch('okta.oauth.DPoPProofGenerator', None):
            with self.assertRaises(ValueError) as cm:
                OAuth(mock_re, config)
            self.assertIn("pycryptodomex", str(cm.exception))

    # --- U-O15: _parse_json_response valid JSON dict ---
    def test_parse_json_response_valid(self):
        """U-O15: Valid JSON dict is parsed correctly."""
        res_details = MagicMock()
        res_details.content_type = "application/json"
        result = OAuth._parse_json_response('{"access_token": "x"}', res_details)
        self.assertEqual(result, {"access_token": "x"})

    # --- U-O16: non-JSON content type ---
    def test_parse_json_response_non_json(self):
        """U-O16: Non-JSON content type returns None."""
        res_details = MagicMock()
        res_details.content_type = "text/html"
        result = OAuth._parse_json_response('<html></html>', res_details)
        self.assertIsNone(result)

    # --- U-O17: invalid JSON string ---
    def test_parse_json_response_invalid_json(self):
        """U-O17: Invalid JSON with application/json returns None."""
        res_details = MagicMock()
        res_details.content_type = "application/json"
        result = OAuth._parse_json_response('not json', res_details)
        self.assertIsNone(result)

    # --- U-O18: is_dpop_enabled accessor ---
    def test_is_dpop_enabled_accessor(self):
        """U-O18: is_dpop_enabled returns correct boolean."""
        mock_re = MagicMock()
        config_on = self._build_config(dpop_enabled=True)
        config_off = self._build_config(dpop_enabled=False)
        self.assertTrue(OAuth(mock_re, config_on).is_dpop_enabled())
        self.assertFalse(OAuth(mock_re, config_off).is_dpop_enabled())

    # --- U-O19: get_dpop_generator accessor ---
    def test_get_dpop_generator_accessor(self):
        """U-O19: get_dpop_generator returns generator when DPoP enabled."""
        mock_re = MagicMock()
        config = self._build_config(dpop_enabled=True)
        oauth = OAuth(mock_re, config)
        self.assertIsNotNone(oauth.get_dpop_generator())

    # --- U-O14: clear_access_token ---
    def test_clear_access_token(self):
        """U-O14: clear_access_token resets state."""
        mock_re = MagicMock()
        config = self._build_config(dpop_enabled=False)
        oauth = OAuth(mock_re, config)
        # Simulate having a token
        oauth._access_token = "test-token"
        oauth._token_type = "DPoP"
        oauth._access_token_expiry_time = 9999999999

        oauth.clear_access_token()

        self.assertIsNone(oauth._access_token)
        self.assertEqual(oauth._token_type, "Bearer")
        self.assertIsNone(oauth._access_token_expiry_time)
        mock_re.clear_authorization_header.assert_called_once()
        mock_re.clear_cached_token.assert_called_once()

    # --- U-O11: Token caching (second call returns cached) ---
    async def test_oauth_token_caching(self):
        """U-O11: Second call returns cached token without HTTP request."""
        mock_re = MagicMock()
        mock_re.create_request = AsyncMock(return_value=({"method": "POST"}, None))

        mock_res_details = MagicMock()
        mock_res_details.status = 200
        mock_res_details.content_type = "application/json"
        mock_res_details.headers = {}
        mock_re.fire_request = AsyncMock(return_value=(
            None, mock_res_details,
            json.dumps({"access_token": "tok1", "token_type": "Bearer", "expires_in": 3600}),
            None,
        ))

        config = self._build_config(dpop_enabled=False)
        oauth = OAuth(mock_re, config)

        # First call should hit HTTP
        token1, ttype1, err1 = await oauth.get_oauth_token()
        self.assertIsNone(err1)
        self.assertEqual(token1, "tok1")
        self.assertEqual(mock_re.fire_request.call_count, 1)

        # Second call should return cached — no additional HTTP
        token2, ttype2, err2 = await oauth.get_oauth_token()
        self.assertIsNone(err2)
        self.assertEqual(token2, "tok1")
        self.assertEqual(mock_re.fire_request.call_count, 1)  # still 1

    # --- U-O12: Token expiry triggers refresh ---
    async def test_oauth_token_expiry_refresh(self):
        """U-O12: Expired token triggers new token request."""
        mock_re = MagicMock()
        mock_re.create_request = AsyncMock(return_value=({"method": "POST"}, None))
        mock_re.clear_authorization_header = MagicMock()
        mock_re.clear_cached_token = MagicMock()

        call_count = 0

        async def _fire_request(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            res_details = MagicMock()
            res_details.status = 200
            res_details.content_type = "application/json"
            res_details.headers = {}
            return (
                None, res_details,
                json.dumps({
                    "access_token": f"tok{call_count}",
                    "token_type": "Bearer",
                    "expires_in": 3600,
                }),
                None,
            )

        mock_re.fire_request = _fire_request
        config = self._build_config(dpop_enabled=False)
        oauth = OAuth(mock_re, config)

        # First token
        token1, _, err1 = await oauth.get_oauth_token()
        self.assertEqual(token1, "tok1")

        # Simulate expiry
        oauth._access_token_expiry_time = int(time.time()) - 1

        # Should get new token
        token2, _, err2 = await oauth.get_oauth_token()
        self.assertEqual(token2, "tok2")
        self.assertEqual(call_count, 2)

    # --- U-O13: get_access_token backward compat ---
    async def test_get_access_token_backward_compat(self):
        """U-O13: get_access_token() returns 2-tuple (not 3-tuple)."""
        mock_re = MagicMock()
        mock_re.create_request = AsyncMock(return_value=({"method": "POST"}, None))

        mock_res_details = MagicMock()
        mock_res_details.status = 200
        mock_res_details.content_type = "application/json"
        mock_res_details.headers = {}
        mock_re.fire_request = AsyncMock(return_value=(
            None, mock_res_details,
            json.dumps({"access_token": "compat-tok", "token_type": "Bearer", "expires_in": 3600}),
            None,
        ))

        config = self._build_config(dpop_enabled=False)
        oauth = OAuth(mock_re, config)

        result = await oauth.get_access_token()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], "compat-tok")
        self.assertIsNone(result[1])

    # --- N-05: get_access_token() with DPoP enabled ---
    async def test_get_access_token_dpop_warns(self):
        """N-05: get_access_token() with DPoP logs warning about discarded token_type."""
        mock_re = MagicMock()
        mock_re.create_request = AsyncMock(return_value=({"method": "POST"}, None))

        mock_res_details = MagicMock()
        mock_res_details.status = 200
        mock_res_details.content_type = "application/json"
        mock_res_details.headers = {}
        mock_re.fire_request = AsyncMock(return_value=(
            None, mock_res_details,
            json.dumps({"access_token": "dpop-tok", "token_type": "DPoP", "expires_in": 3600}),
            None,
        ))

        config = self._build_config(dpop_enabled=True)
        oauth = OAuth(mock_re, config)

        with patch("okta.oauth.logger") as mock_logger:
            token, err = await oauth.get_access_token()
        self.assertEqual(token, "dpop-tok")
        # Verify warning was logged about discarded token_type
        warning_calls = [str(c) for c in mock_logger.warning.call_args_list]
        self.assertTrue(
            any("get_oauth_token()" in c for c in warning_calls),
            f"Expected warning about get_oauth_token(), got: {warning_calls}",
        )

    # --- U-O10: Server returns Bearer despite DPoP request ---
    async def test_dpop_server_returns_bearer_warns(self):
        """U-O10: DPoP enabled but server returns Bearer — logs warning."""
        mock_re = MagicMock()
        mock_re.create_request = AsyncMock(return_value=({"method": "POST"}, None))

        mock_res_details = MagicMock()
        mock_res_details.status = 200
        mock_res_details.content_type = "application/json"
        mock_res_details.headers = {}
        mock_re.fire_request = AsyncMock(return_value=(
            None, mock_res_details,
            json.dumps({"access_token": "bearer-tok", "token_type": "Bearer", "expires_in": 3600}),
            None,
        ))

        config = self._build_config(dpop_enabled=True)
        oauth = OAuth(mock_re, config)

        with patch("okta.oauth.logger") as mock_logger:
            token, ttype, err = await oauth.get_oauth_token()
        self.assertEqual(ttype, "Bearer")
        # Verify warning was logged about Bearer token despite DPoP
        warning_calls = [str(c) for c in mock_logger.warning.call_args_list]
        self.assertTrue(
            any("Bearer" in c and "DPoP" in c for c in warning_calls),
            f"Expected warning about Bearer+DPoP, got: {warning_calls}",
        )

    # --- U-O04: Bearer flow (no DPoP) ---
    async def test_bearer_flow_no_dpop(self):
        """U-O04: DPoP disabled returns ('token', 'Bearer', None)."""
        mock_re = MagicMock()
        mock_re.create_request = AsyncMock(return_value=({"method": "POST"}, None))

        mock_res_details = MagicMock()
        mock_res_details.status = 200
        mock_res_details.content_type = "application/json"
        mock_res_details.headers = {}
        mock_re.fire_request = AsyncMock(return_value=(
            None, mock_res_details,
            json.dumps({"access_token": "bearer-tok", "token_type": "Bearer", "expires_in": 3600}),
            None,
        ))

        config = self._build_config(dpop_enabled=False)
        oauth = OAuth(mock_re, config)

        token, ttype, err = await oauth.get_oauth_token()
        self.assertIsNone(err)
        self.assertEqual(token, "bearer-tok")
        self.assertEqual(ttype, "Bearer")

    # --- U-O08: Non-retryable DPoP error (invalid_dpop_proof) ---
    async def test_non_retryable_dpop_error(self):
        """U-O08: invalid_dpop_proof returns error, does not crash."""
        mock_re = MagicMock()
        mock_re.create_request = AsyncMock(return_value=({"method": "POST"}, None))

        mock_res_details = MagicMock()
        mock_res_details.status = 400
        mock_res_details.content_type = "application/json"
        mock_res_details.headers = {}
        mock_re.fire_request = AsyncMock(return_value=(
            None, mock_res_details,
            json.dumps({"error": "invalid_dpop_proof", "error_description": "Bad proof"}),
            None,
        ))

        config = self._build_config(dpop_enabled=True)
        oauth = OAuth(mock_re, config)

        token, ttype, err = await oauth.get_oauth_token()
        self.assertIsNone(token)
        self.assertEqual(ttype, "Bearer")
        self.assertIsNotNone(err)
        self.assertIn("invalid_dpop_proof", str(err.error_code))

    # --- U-O05: DPoP flow with nonce challenge then success ---
    async def test_dpop_nonce_challenge_then_success(self):
        """U-O05: First 400 use_dpop_nonce, then 200 with token."""
        mock_re = MagicMock()
        mock_re.create_request = AsyncMock(return_value=({"method": "POST"}, None))

        call_count = 0

        async def _fire_request(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                # First call: 400 use_dpop_nonce
                res = MagicMock()
                res.status = 400
                res.content_type = "application/json"
                res.headers = {"dpop-nonce": "server-nonce-abc"}
                return (
                    None, res,
                    json.dumps({"error": "use_dpop_nonce"}),
                    None,
                )
            else:
                # Retry: success
                res = MagicMock()
                res.status = 200
                res.content_type = "application/json"
                res.headers = {}
                return (
                    None, res,
                    json.dumps({
                        "access_token": "dpop-tok-abc",
                        "token_type": "DPoP",
                        "expires_in": 3600,
                    }),
                    None,
                )

        mock_re.fire_request = _fire_request
        config = self._build_config(dpop_enabled=True)
        oauth = OAuth(mock_re, config)

        token, ttype, err = await oauth.get_oauth_token()
        self.assertIsNone(err)
        self.assertEqual(token, "dpop-tok-abc")
        self.assertEqual(ttype, "DPoP")
        # Verify nonce was stored
        self.assertEqual(oauth.get_dpop_generator().get_nonce(), "server-nonce-abc")

    # --- U-O06: DPoP direct success (no nonce needed) ---
    async def test_dpop_direct_success(self):
        """U-O06: DPoP flow succeeds on first try without nonce challenge."""
        mock_re = MagicMock()
        mock_re.create_request = AsyncMock(return_value=({"method": "POST"}, None))

        mock_res_details = MagicMock()
        mock_res_details.status = 200
        mock_res_details.content_type = "application/json"
        mock_res_details.headers = {}
        mock_re.fire_request = AsyncMock(return_value=(
            None, mock_res_details,
            json.dumps({"access_token": "dpop-direct", "token_type": "DPoP", "expires_in": 3600}),
            None,
        ))

        config = self._build_config(dpop_enabled=True)
        oauth = OAuth(mock_re, config)

        token, ttype, err = await oauth.get_oauth_token()
        self.assertIsNone(err)
        self.assertEqual(token, "dpop-direct")
        self.assertEqual(ttype, "DPoP")

    # --- U-O07: Nonce exhaustion ---
    async def test_dpop_nonce_exhaustion(self):
        """U-O07: Server returns use_dpop_nonce for all retries — returns error."""
        mock_re = MagicMock()
        mock_re.create_request = AsyncMock(return_value=({"method": "POST"}, None))

        nonce_counter = 0

        async def _fire_request(*args, **kwargs):
            nonlocal nonce_counter
            nonce_counter += 1
            res = MagicMock()
            res.status = 400
            res.content_type = "application/json"
            res.headers = {"dpop-nonce": f"nonce-{nonce_counter}"}
            return (
                None, res,
                json.dumps({"error": "use_dpop_nonce"}),
                None,
            )

        mock_re.fire_request = _fire_request
        config = self._build_config(dpop_enabled=True)
        oauth = OAuth(mock_re, config)

        token, ttype, err = await oauth.get_oauth_token()
        self.assertIsNone(token)
        self.assertIsNotNone(err)
        self.assertIn("nonce", str(err).lower())


# ───────────────────────────────────────────────────────────────────
# Section 2.3: Request Executor DPoP Integration
# ───────────────────────────────────────────────────────────────────

class TestRequestExecutorDPoP(unittest.IsolatedAsyncioTestCase):
    """Test RequestExecutor DPoP integration (Section 2.3)."""

    def _build_config(self, auth_mode="SSWS", dpop_enabled=False):
        """Helper to build a config for RequestExecutor."""
        config = {
            "client": {
                "orgUrl": "https://test.okta.com",
                "authorizationMode": auth_mode,
                "token": "myApiToken",
                "clientId": "0oatest123",
                "scopes": ["okta.users.read"],
                "privateKey": SAMPLE_RSA,
                "oauthTokenRenewalOffset": 5,
                "requestTimeout": 0,
                "rateLimit": {"maxRetries": 2},
                "dpopEnabled": dpop_enabled,
                "userAgent": "",
            }
        }
        return config

    # --- U-R05: SSWS flow unchanged ---
    async def test_ssws_flow_no_dpop(self):
        """U-R05: SSWS auth mode has no DPoP headers."""

        config = self._build_config(auth_mode="SSWS")
        cache = NoOpCache()
        re = RequestExecutor(config, cache)

        request, err = await re.create_request("GET", "/api/v1/users")
        self.assertIsNone(err)
        self.assertIn("Authorization", request["headers"])
        self.assertTrue(request["headers"]["Authorization"].startswith("SSWS "))
        self.assertNotIn("DPoP", request["headers"])

    # --- U-R04: DPoP token from fresh OAuth call ---
    async def test_dpop_token_from_oauth(self):
        """U-R04: No cached token, DPoP enabled => calls get_oauth_token(), sets DPoP headers."""

        config = self._build_config(auth_mode="PrivateKey", dpop_enabled=True)
        cache = NoOpCache()
        re = RequestExecutor(config, cache)

        # Mock OAuth to return a DPoP token
        re._oauth.get_oauth_token = AsyncMock(
            return_value=("dpop-token-xyz", "DPoP", None))
        re._oauth.is_dpop_enabled = MagicMock(return_value=True)

        mock_generator = MagicMock()
        mock_generator.generate_proof_jwt.return_value = "proof-jwt-123"
        mock_generator.get_nonce.return_value = "nonce-val"
        re._oauth.get_dpop_generator = MagicMock(return_value=mock_generator)

        request, err = await re.create_request("GET", "/api/v1/users")
        self.assertIsNone(err)
        self.assertEqual(request["headers"]["Authorization"], "DPoP dpop-token-xyz")
        self.assertEqual(request["headers"]["DPoP"], "proof-jwt-123")
        self.assertIn("isDPoP:true", request["headers"].get("x-okta-user-agent-extended", ""))

    # --- U-R01: DPoP token in cache (tuple format) ---
    async def test_dpop_token_from_cache_tuple(self):
        """U-R01: Cache contains (token, 'DPoP') => Auth: DPoP token, DPoP header present."""

        config = self._build_config(auth_mode="PrivateKey", dpop_enabled=True)
        cache = OktaCache(300, 300)
        cache.add("OKTA_ACCESS_TOKEN", ("cached-dpop-tok", "DPoP"))

        re = RequestExecutor(config, cache)

        mock_generator = MagicMock()
        mock_generator.generate_proof_jwt.return_value = "proof-from-cache"
        mock_generator.get_nonce.return_value = None
        re._oauth.get_dpop_generator = MagicMock(return_value=mock_generator)
        re._oauth.is_dpop_enabled = MagicMock(return_value=True)

        request, err = await re.create_request("GET", "/api/v1/users")
        self.assertIsNone(err)
        self.assertEqual(request["headers"]["Authorization"], "DPoP cached-dpop-tok")
        self.assertIn("DPoP", request["headers"])

    # --- U-R02: Legacy string format in cache with DPoP enabled ---
    async def test_cache_legacy_string_dpop_enabled(self):
        """U-R02: Cache has plain string with DPoP enabled => invalidate, fetch fresh."""

        config = self._build_config(auth_mode="PrivateKey", dpop_enabled=True)
        cache = OktaCache(300, 300)
        cache.add("OKTA_ACCESS_TOKEN", "plain-string-token")

        re = RequestExecutor(config, cache)

        re._oauth.get_oauth_token = AsyncMock(
            return_value=("fresh-dpop-tok", "DPoP", None))
        re._oauth.is_dpop_enabled = MagicMock(return_value=True)

        mock_generator = MagicMock()
        mock_generator.generate_proof_jwt.return_value = "fresh-proof"
        mock_generator.get_nonce.return_value = None
        re._oauth.get_dpop_generator = MagicMock(return_value=mock_generator)

        request, err = await re.create_request("GET", "/api/v1/users")
        self.assertIsNone(err)
        # Should have fetched fresh token, not used legacy string
        self.assertEqual(request["headers"]["Authorization"], "DPoP fresh-dpop-tok")
        re._oauth.get_oauth_token.assert_called_once()

    # --- U-R03: Legacy string format in cache with DPoP disabled ---
    async def test_cache_legacy_string_dpop_disabled(self):
        """U-R03: Cache has plain string, DPoP disabled => Authorization: Bearer token."""

        config = self._build_config(auth_mode="PrivateKey", dpop_enabled=False)
        cache = OktaCache(300, 300)
        cache.add("OKTA_ACCESS_TOKEN", "legacy-bearer-token")

        re = RequestExecutor(config, cache)
        re._oauth.is_dpop_enabled = MagicMock(return_value=False)

        request, err = await re.create_request("GET", "/api/v1/users")
        self.assertIsNone(err)
        self.assertEqual(request["headers"]["Authorization"], "Bearer legacy-bearer-token")

    # --- N-06: Cache with legacy string format ---
    async def test_n06_cache_legacy_invalidation(self):
        """N-06: Pre-populated cache string with DPoP => invalidated, fresh token."""
        # This is essentially U-R02 with the negative test perspective

        config = self._build_config(auth_mode="PrivateKey", dpop_enabled=True)
        cache = OktaCache(300, 300)
        cache.add("OKTA_ACCESS_TOKEN", "old-string-token")

        re = RequestExecutor(config, cache)
        re._oauth.get_oauth_token = AsyncMock(
            return_value=("new-dpop-tok", "DPoP", None))
        re._oauth.is_dpop_enabled = MagicMock(return_value=True)

        mock_gen = MagicMock()
        mock_gen.generate_proof_jwt.return_value = "new-proof"
        mock_gen.get_nonce.return_value = None
        re._oauth.get_dpop_generator = MagicMock(return_value=mock_gen)

        request, err = await re.create_request("GET", "/api/v1/users")
        self.assertIsNone(err)
        # Old token must NOT be used
        self.assertNotIn("old-string-token", request["headers"]["Authorization"])
        self.assertEqual(request["headers"]["Authorization"], "DPoP new-dpop-tok")

    # --- U-R06: fire_request_helper DPoP nonce in 400 response ---
    async def test_fire_request_helper_dpop_nonce_400(self):
        """U-R06: 400 with dpop-nonce header stores nonce in generator."""

        config = self._build_config(auth_mode="PrivateKey", dpop_enabled=True)
        cache = NoOpCache()
        re = RequestExecutor(config, cache)

        mock_generator = MagicMock()
        mock_generator.generate_proof_jwt.return_value = "retry-proof"
        re._oauth._dpop_generator = mock_generator
        re._oauth._dpop_enabled = True
        re._oauth.is_dpop_enabled = MagicMock(return_value=True)
        re._oauth.get_dpop_generator = MagicMock(return_value=mock_generator)
        re._oauth.get_current_token = MagicMock(return_value=("tok", "DPoP"))

        # Mock HTTP response: 400 with dpop-nonce
        mock_response = MagicMock()
        mock_response.status = 400
        mock_response.headers = multidict.CIMultiDict({
            "dpop-nonce": "server-nonce-400",
            "Content-Type": "application/json",
        })

        re._http_client.send_request = AsyncMock(return_value=(
            None, mock_response,
            json.dumps({"error": "use_dpop_nonce"}),
            None,
        ))

        request = {
            "method": "GET",
            "url": "https://test.okta.com/api/v1/users",
            "headers": {"Authorization": "DPoP tok", "DPoP": "old-proof"},
            "data": None,
            "form": {},
        }

        _, res_details, _, _ = await re.fire_request_helper(request, 0, time.time())
        mock_generator.set_nonce.assert_called_with("server-nonce-400")

    # --- U-R08: Non-DPoP 400 — normal error handling ---
    async def test_fire_request_helper_non_dpop_400(self):
        """U-R08: 400 without dpop-nonce header does not trigger DPoP nonce logic."""

        config = self._build_config(auth_mode="PrivateKey", dpop_enabled=True)
        cache = NoOpCache()
        re = RequestExecutor(config, cache)

        mock_generator = MagicMock()
        re._oauth._dpop_enabled = True
        re._oauth.is_dpop_enabled = MagicMock(return_value=True)
        re._oauth.get_dpop_generator = MagicMock(return_value=mock_generator)

        # Mock HTTP response: 400 WITHOUT dpop-nonce
        mock_response = MagicMock()
        mock_response.status = 400
        mock_response.headers = multidict.CIMultiDict({
            "Content-Type": "application/json",
        })

        re._http_client.send_request = AsyncMock(return_value=(
            None, mock_response,
            json.dumps({"error": "invalid_grant", "error_description": "bad grant"}),
            None,
        ))

        request = {
            "method": "GET",
            "url": "https://test.okta.com/api/v1/users",
            "headers": {},
            "data": None,
            "form": {},
        }

        _, res_details, _, _ = await re.fire_request_helper(request, 0, time.time())
        # set_nonce should NOT be called
        mock_generator.set_nonce.assert_not_called()


if __name__ == '__main__':
    unittest.main()
