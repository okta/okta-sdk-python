# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

"""
DPoP-specific error messages and handling.

This module provides user-friendly error messages for DPoP-related errors
returned by the Okta authorization server.

Reference: RFC 9449 Section 7 (Error Handling)
"""

# Well-formed DPoP error prefixes per RFC 9449 conventions.
# Module-level constant to avoid re-creating on every is_dpop_error() call.
_DPOP_ERROR_PREFIXES = ("invalid_dpop_", "use_dpop_", "dpop_")

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
        '1. Create a new OktaClient instance to obtain a fresh DPoP-bound token. '
        '2. Ensure you are using the same Client instance for all requests in a session. '
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
        error_code.lower(),
        f'DPoP error: {error_code}. Check Okta logs for details. '
        f'See RFC 9449 for DPoP specification: https://datatracker.ietf.org/doc/html/rfc9449'
    )


def is_dpop_error(error_code: str) -> bool:
    """
    Check if error code is DPoP-related.

    Matches known DPoP error codes and well-formed DPoP error prefixes
    (e.g., 'invalid_dpop_*', 'use_dpop_*') to avoid false positives from
    unrelated errors that happen to contain the substring 'dpop'.

    Args:
        error_code: Error code from OAuth error response

    Returns:
        True if error is DPoP-related
    """
    if not error_code:
        return False

    error_lower = error_code.lower()

    # Known DPoP error codes (exact match)
    if error_lower in DPOP_ERROR_MESSAGES:
        return True

    # Check well-formed DPoP error prefixes per RFC 9449 conventions
    return any(error_lower.startswith(prefix) for prefix in _DPOP_ERROR_PREFIXES)
