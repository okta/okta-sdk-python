"""
FIX #8: DPoP-specific error messages and handling.

This module provides user-friendly error messages for DPoP-related errors
returned by the Okta authorization server.

Reference: RFC 9449 Section 7 (Error Handling)
"""

DPOP_ERROR_MESSAGES = {
    'invalid_dpop_proof': (
        'DPoP proof validation failed. The server rejected the DPoP proof JWT. '
        'Possible causes: invalid signature, incorrect claims, or key mismatch. '
        'Check that your DPoP keys are correctly generated and the proof JWT '
        'includes all required claims (jti, htm, htu, iat).'
    ),
    'use_dpop_nonce': (
        'Server requires a nonce in the DPoP proof. '
        'The SDK will automatically retry with the provided nonce. '
        'This is normal for the first DPoP request to a server.'
    ),
    'invalid_dpop_key_binding': (
        'Access token is not bound to the DPoP key. '
        'The access token was obtained with a different key than the one used for this request. '
        'This may happen if keys were rotated after obtaining the token. '
        'Try clearing the token cache and obtaining a new token.'
    ),
    'invalid_dpop_jkt': (
        'DPoP JWK thumbprint validation failed. '
        'The JWK in the DPoP proof does not match the expected thumbprint. '
        'Ensure you are using the same key pair for all requests.'
    ),
    'invalid_request': (
        'Invalid request. Check your DPoP proof JWT format and claims. '
        'Ensure the JWT is properly signed and all required claims are present.'
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
    dpop_keywords = ['dpop', 'nonce', 'jkt', 'key_binding']
    error_lower = error_code.lower()
    return any(keyword in error_lower for keyword in dpop_keywords)
