"""
DPoP-specific error messages and handling.

This module provides user-friendly error messages for DPoP-related errors
returned by the Okta authorization server.

Reference: RFC 9449 Section 7 (Error Handling)
"""

DPOP_ERROR_MESSAGES = {
    'invalid_dpop_proof': (
        'DPoP proof validation failed. The server rejected the DPoP proof JWT. '
        '\n\nACTION: '
        '1. Verify dpopEnabled=True in both SDK config AND Okta application settings. '
        '2. Check SDK logs (set logging level to DEBUG) for proof JWT details. '
        '3. Ensure system clock is synchronized (proof JWTs have timestamps). '
        '\n\nPossible causes: invalid signature, incorrect claims, or key mismatch.'
    ),
    'use_dpop_nonce': (
        'Server requires a nonce in the DPoP proof. '
        'The SDK will automatically retry with the provided nonce. '
        'This is normal for the first DPoP request to a server. '
        '\n\nACTION: No action needed - SDK handles this automatically.'
    ),
    'invalid_dpop_key_binding': (
        'Access token is not bound to the DPoP key. '
        'The access token was obtained with a different key than the one used for this request. '
        '\n\nACTION: '
        '1. Clear token cache: client._request_executor._cache.clear() '
        '2. Obtain a new token with the current key. '
        '\n\nThis may happen if keys were rotated after obtaining the token.'
    ),
    'invalid_dpop_jkt': (
        'DPoP JWK thumbprint validation failed. '
        'The JWK in the DPoP proof does not match the expected thumbprint. '
        '\n\nACTION: '
        '1. Ensure you are using the same Client instance for all requests. '
        '2. Do not manually rotate keys during active sessions. '
        '3. Check that dpopKeyRotationInterval is configured consistently. '
        '\n\nEnsure you are using the same key pair for all requests.'
    ),
    'invalid_request': (
        'Invalid request. Check your DPoP proof JWT format and claims. '
        '\n\nACTION: '
        '1. Enable DEBUG logging to inspect proof JWT claims. '
        '2. Verify all required claims are present (jti, htm, htu, iat). '
        '3. Check that HTU matches the request URL (without query/fragment). '
        '\n\nEnsure the JWT is properly signed and all required claims are present.'
    ),
}


def get_dpop_error_message(error_code: str) -> str:
    """
    Get user-friendly error message for DPoP error code.

    Args:
        error_code: Error code from OAuth error response

    Returns:
        User-friendly error message
    """
    return DPOP_ERROR_MESSAGES.get(
        error_code,
        f'DPoP error: {error_code}. Check Okta logs for details. '
        f'See RFC 9449 for DPoP specification: https://datatracker.ietf.org/doc/html/rfc9449'
    )


def is_dpop_error(error_code: str) -> bool:
    """
    Check if error code is DPoP-related.

    Args:
        error_code: Error code from OAuth error response

    Returns:
        True if error is DPoP-related
    """
    # Use more specific patterns to avoid false positives
    # Check if it's a known DPoP error or contains 'dpop' prefix
    error_lower = error_code.lower()

    # Known DPoP error codes
    if error_lower in DPOP_ERROR_MESSAGES:
        return True

    # Or contains 'dpop' keyword (more specific than just 'nonce')
    return 'dpop' in error_lower
