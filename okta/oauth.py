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
OAuth 2.0 token management for the Okta Python SDK.

Handles token acquisition, caching, renewal, and DPoP (RFC 9449) integration.
This module is generated from a Mustache template but contains significant
hand-written logic for DPoP support.  Safe to edit for DPoP-related changes.
"""

import asyncio
import json
import logging
import time
from typing import Any, Dict, Optional, Tuple

from okta.constants import LOGGER_NAME, MAX_DPOP_NONCE_RETRIES, MAX_DPOP_BACKOFF_DELAY

# Try to import DPoP — may fail if crypto libraries not installed.
# None on success means the import succeeded; a non-None string means it failed.
_dpop_import_error: Optional[str] = None
DPoPProofGenerator = None
try:
    from okta.dpop import DPoPProofGenerator
except ImportError as e:
    _dpop_import_error = str(e)

from okta.errors.dpop_errors import get_dpop_error_message, is_dpop_error  # noqa: E402
from okta.errors.okta_api_error import OktaAPIError  # noqa: E402
from okta.http_client import HTTPClient  # noqa: E402
from okta.jwt import JWT  # noqa: E402

logger = logging.getLogger(LOGGER_NAME)


class OAuth:
    """
    This class contains the OAuth actions for the Okta Client.
    """

    OAUTH_ENDPOINT = "/oauth2/v1/token"

    # One-shot flag: ensures the get_access_token() deprecation warning is
    # emitted at most once per process to avoid log noise.
    _access_token_dpop_warned: bool = False

    def __init__(self, request_executor: Any, config: Dict[str, Any]) -> None:
        self._request_executor = request_executor
        self._config = config
        self._access_token: Optional[str] = None
        self._token_type: str = "Bearer"
        self._access_token_expiry_time: Optional[int] = None

        # Thread safety: Protect token state from concurrent access
        self._token_lock = asyncio.Lock()

        # Initialize DPoP if enabled
        self._dpop_enabled: bool = config["client"].get("dpopEnabled", False)
        self._dpop_generator: Optional[Any] = None

        if self._dpop_enabled:
            if DPoPProofGenerator is None:
                logger.error(
                    "DPoP enabled but crypto libraries unavailable: %s",
                    _dpop_import_error,
                )
                error = (
                    ImportError(_dpop_import_error)
                    if _dpop_import_error
                    else ImportError("DPoP import failed")
                )
                raise ValueError(
                    "DPoP requires 'pycryptodomex' and 'jwcrypto' libraries. "
                    "Install with: pip install pycryptodomex>=3.23.0 jwcrypto>=1.5.6"
                ) from error

            try:
                self._dpop_generator = DPoPProofGenerator(config["client"])
                logger.debug("DPoP authentication enabled")
            except Exception as e:
                logger.error("Failed to initialize DPoP generator: %s", e)
                raise ValueError(f"DPoP initialization failed: {e}") from e

    def get_JWT(self) -> str:
        """
        Generates JWT using client configuration

        Returns:
            str: Generated JSON Web Token
        """
        org_url = self._config["client"]["orgUrl"]
        client_id = self._config["client"]["clientId"]
        private_key = self._config["client"]["privateKey"]
        # check if kid is provided in config - set if so
        kid = self._config["client"].get("kid")

        return JWT.create_token(org_url, client_id, private_key, kid)

    @staticmethod
    def _parse_json_response(
        res_body: Optional[str], res_details: Optional[Any]
    ) -> Optional[Dict[str, Any]]:
        """
        Parse response body if JSON content type.

        Args:
            res_body: Response body string
            res_details: Response details object with content_type

        Returns:
            Parsed JSON dict or None if not JSON or parse error
        """
        if res_body and res_details and res_details.content_type == "application/json":
            try:
                parsed = json.loads(res_body)
                if not isinstance(parsed, dict):
                    logger.warning(
                        "Expected dict response, got %s. "
                        "This may indicate an unexpected API response format.",
                        type(parsed).__name__,
                    )
                    return None
                return parsed
            except (json.JSONDecodeError, ValueError, TypeError) as e:
                logger.error("JSON decode error: %s", e)
                return None
        return None

    async def get_access_token(self) -> Tuple[Optional[str], Optional[Exception]]:
        """
        Retrieves or generates the OAuth access token for the Okta Client.

        BACKWARD COMPATIBILITY NOTE:
        ---------------------------
        This method returns a 2-tuple (token, error) for backward compatibility.
        For DPoP support, use get_oauth_token() instead, which returns a 3-tuple
        (token, token_type, error) where token_type is either "Bearer" or "DPoP".

        This wrapper exists to maintain compatibility with existing code that expects:
            token, error = await oauth.get_access_token()

        New code should use:
            token, token_type, error = await oauth.get_oauth_token()

        Returns:
            tuple: (access_token, error) - Legacy 2-tuple for backward compatibility
        """
        access_token, token_type, error = await self.get_oauth_token()
        if self._dpop_enabled and token_type == "DPoP":
            if not OAuth._access_token_dpop_warned:
                OAuth._access_token_dpop_warned = True
                logger.warning(
                    "get_access_token() discards token_type. "
                    "Use get_oauth_token() for DPoP support."
                )
        return (access_token, error)

    async def get_oauth_token(self) -> Tuple[Optional[str], str, Optional[Exception]]:
        """
        Retrieves or generates the OAuth access token for the Okta Client.
        Supports both Bearer and DPoP token types.

        Returns:
            tuple: (access_token, token_type, error) — token_type is "DPoP" when
                   DPoP is enabled and the server supports it.
        """
        # Acquire lock to prevent race conditions in token state management
        async with self._token_lock:
            # Check token expiry after acquiring lock (double-check pattern)
            current_time = int(time.time())
            if self._access_token and self._access_token_expiry_time is not None:
                renewal_offset = (
                    self._config["client"]["oauthTokenRenewalOffset"] * 60
                )  # Convert minutes to seconds
                if current_time + renewal_offset >= self._access_token_expiry_time:
                    self.clear_access_token()

            # Return cached token if available
            if self._access_token:
                return (self._access_token, self._token_type, None)

            # --- Generate new token ---
            jwt_assertion = self.get_JWT()
            parameters = {
                "grant_type": "client_credentials",
                "scope": " ".join(self._config["client"]["scopes"]),
                "client_assertion_type": (
                    "urn:ietf:params:oauth:client-assertion-type:jwt-bearer"
                ),
                "client_assertion": jwt_assertion,
            }

            org_url = self._config["client"]["orgUrl"]
            url = f"{org_url}{OAuth.OAUTH_ENDPOINT}"

            # Prepare headers
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded",
            }

            # Add DPoP header if enabled (first attempt without nonce)
            if self._dpop_enabled:
                dpop_proof = self._dpop_generator.generate_proof_jwt(
                    http_method="POST", http_url=url,
                )
                headers["DPoP"] = dpop_proof
                logger.debug("Added DPoP proof to token request")

            # Make initial request
            oauth_req, err = await self._request_executor.create_request(
                "POST", url, form=parameters, headers=headers, oauth=True,
            )
            if err:
                return (None, "Bearer", err)

            _, res_details, res_body, err = (
                await self._request_executor.fire_request(oauth_req)
            )

            # Parse response body once (avoid double-parsing)
            parsed_response = self._parse_json_response(res_body, res_details)

            # Handle DPoP-specific errors (RFC 9449 Section 7)
            # Only check for DPoP errors when DPoP is enabled — non-DPoP
            # servers will never return DPoP error codes.
            if (
                self._dpop_enabled
                and res_details
                and res_details.status == 400
                and isinstance(parsed_response, dict)
            ):
                error_code = parsed_response.get("error", "")

                if is_dpop_error(error_code):
                    if error_code == "use_dpop_nonce":
                        # Extract nonce from response header
                        dpop_nonce = res_details.headers.get("dpop-nonce")
                        if dpop_nonce and self._dpop_enabled:
                            # Retry with server-provided nonce (extracted method)
                            result = await self._retry_token_with_dpop_nonce(
                                dpop_nonce, url, parameters,
                            )
                            parsed_response, res_details, res_body, err = result
                            if err:
                                return (None, "Bearer", err)
                            # Fall through to token extraction below
                    else:
                        # Non-retryable DPoP error — provide helpful message
                        error_msg = get_dpop_error_message(error_code)
                        error_description = parsed_response.get(
                            "error_description", ""
                        )
                        if error_description:
                            error_msg += f"\n\nServer error: {error_description}"

                        logger.error(
                            "DPoP Error (%s): %s",
                            error_code, error_msg,
                        )
                        return (
                            None,
                            "Bearer",
                            OktaAPIError(
                                url, res_details,
                                {
                                    "errorCode": error_code,
                                    "errorSummary": error_msg,
                                    "errorLink": "",
                                    "errorId": "",
                                    "errorCauses": [],
                                },
                            ),
                        )

            # Handle general HTTP errors
            if err:
                return (None, "Bearer", err)

            # Check parsed response for errors
            if parsed_response:
                if "error" in parsed_response or "errorCode" in parsed_response:
                    error_body = {
                        "errorCode": (
                            parsed_response.get("error")
                            or parsed_response.get("errorCode", "unknown_error")
                        ),
                        "errorSummary": (
                            parsed_response.get("error_description")
                            or parsed_response.get("errorSummary")
                            or str(parsed_response)
                        ),
                        "errorLink": parsed_response.get("errorLink", ""),
                        "errorId": parsed_response.get("errorId", ""),
                        "errorCauses": parsed_response.get("errorCauses", []),
                    }
                    return (
                        None, "Bearer",
                        OktaAPIError(url, res_details, error_body),
                    )
                # Success — parsed_response contains the token data
            else:
                # Edge case: non-JSON response
                parsed_response, err = HTTPClient.check_response_for_error(
                    url, res_details, res_body,
                )
                if err:
                    return (None, "Bearer", err)

            # Extract and store token
            access_token = parsed_response.get("access_token")
            if not access_token:
                return (
                    None,
                    "Bearer",
                    Exception(
                        "OAuth token response missing 'access_token' field. "
                        "Response keys: " + str(list(parsed_response.keys()))
                    ),
                )
            token_type = parsed_response.get("token_type", "Bearer")
            expires_in = parsed_response.get("expires_in", 3600)

            self._access_token = access_token
            self._token_type = token_type
            self._access_token_expiry_time = int(time.time()) + expires_in

            # Store nonce from successful response if present
            if (
                self._dpop_enabled
                and res_details
                and "dpop-nonce" in res_details.headers
            ):
                self._dpop_generator.set_nonce(
                    res_details.headers["dpop-nonce"]
                )
                logger.debug("Stored nonce from successful token response")

            # Log appropriate message based on token type
            if self._dpop_enabled and token_type == "Bearer":
                logger.warning(
                    "DPoP was enabled but server returned Bearer token. "
                    "Ensure DPoP is enabled for this application in "
                    "Okta admin console."
                )
            else:
                logger.debug("Obtained %s access token", token_type)

            return (access_token, token_type, None)

    async def _retry_token_with_dpop_nonce(
        self,
        initial_nonce: str,
        url: str,
        parameters: dict,
    ) -> Tuple[
        Optional[Dict[str, Any]], Optional[Any], Optional[str], Optional[Exception]
    ]:
        """
        Retry token request with server-provided DPoP nonce (RFC 9449 Section 8).

        The ``use_dpop_nonce`` error is expected on the first DPoP request to a
        server.  This method retries with exponential backoff (0.1 s, 0.2 s, ...
        capped at ``MAX_DPOP_BACKOFF_DELAY``).

        IMPORTANT -- JWT regeneration on each retry:
            Okta's authorization server consumes the client assertion JWT's
            ``jti`` (unique ID) on **every** request, including requests that
            return ``400 use_dpop_nonce``.  Reusing the same JWT on a retry
            would cause ``401 invalid_client -- The client_assertion token has
            already been used``.  Therefore each retry generates a fresh JWT
            via ``self.get_JWT()``.

        Args:
            initial_nonce: Nonce from the server's ``dpop-nonce`` header.
            url: Full token endpoint URL.
            parameters: OAuth token request form parameters (mutated in-place
                with fresh ``client_assertion`` on each retry).

        Returns:
            4-tuple of ``(parsed_response, res_details, res_body, error)``:

            - *parsed_response* (dict or None): Parsed JSON token response on
              success, or ``None`` on failure.
            - *res_details* (aiohttp.ClientResponse or None): HTTP response
              metadata.  ``None`` only on the defensive-fallback path.
            - *res_body* (str or None): Raw response body string.
            - *error* (Exception or None): If not ``None``, the caller should
              return it immediately; *parsed_response* is meaningless.
        """
        dpop_nonce = initial_nonce

        for retry_attempt in range(MAX_DPOP_NONCE_RETRIES):
            logger.debug(
                "DPoP nonce challenge retry (attempt %d/%d)",
                retry_attempt + 1, MAX_DPOP_NONCE_RETRIES,
            )

            # Store nonce for future requests
            self._dpop_generator.set_nonce(dpop_nonce)

            # Exponential backoff on every retry: 0.1 s, 0.2 s, …
            backoff_delay = min(
                0.1 * (2 ** retry_attempt),
                MAX_DPOP_BACKOFF_DELAY,
            )
            logger.debug("Backing off for %.2fs before nonce retry", backoff_delay)
            await asyncio.sleep(backoff_delay)

            # Generate fresh client assertion JWT — Okta consumes the jti on
            # every request (even 400 responses), so we MUST use a new one.
            parameters["client_assertion"] = self.get_JWT()

            # Generate new DPoP proof with nonce
            dpop_proof = self._dpop_generator.generate_proof_jwt(
                http_method="POST",
                http_url=url,
                nonce=dpop_nonce,
            )

            # Build fresh headers to avoid mutating the caller's dict
            retry_headers = {
                "Accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded",
                "DPoP": dpop_proof,
            }

            # Retry request
            oauth_req, err = await self._request_executor.create_request(
                "POST", url, form=parameters, headers=retry_headers, oauth=True,
            )
            if err:
                return (None, None, None, err)

            _, res_details, res_body, err = (
                await self._request_executor.fire_request(oauth_req)
            )
            parsed_response = self._parse_json_response(res_body, res_details)

            # Check for another nonce challenge
            is_nonce_challenge = (
                res_details
                and res_details.status == 400
                and isinstance(parsed_response, dict)
                and parsed_response.get("error") == "use_dpop_nonce"
            )

            if is_nonce_challenge:
                new_nonce = res_details.headers.get("dpop-nonce")
                has_retries_left = retry_attempt < MAX_DPOP_NONCE_RETRIES - 1
                if new_nonce and new_nonce != dpop_nonce and has_retries_left:
                    logger.debug("Server provided new nonce, will retry")
                    dpop_nonce = new_nonce
                    continue

                # Max retries exhausted or same nonce returned again
                error_msg = (
                    f"DPoP nonce challenge failed after "
                    f"{MAX_DPOP_NONCE_RETRIES} retries. "
                    "Server may be rejecting nonce or rotating too "
                    "frequently."
                )
                logger.error(error_msg)
                return (
                    None, res_details, res_body,
                    OktaAPIError(
                        url, res_details,
                        {
                            "errorCode": "dpop_nonce_exhausted",
                            "errorSummary": error_msg,
                            "errorLink": "",
                            "errorId": "",
                            "errorCauses": [],
                        },
                    ),
                )

            # Retry succeeded (or a different error) — let caller handle
            return (parsed_response, res_details, res_body, err)

        # Defensive fallback (loop should always return)
        return (None, None, None, Exception(
            "DPoP nonce retry loop exited unexpectedly"
        ))

    def clear_access_token(self) -> None:
        """
        Clear currently used OAuth access token, probably expired.
        Also resets the token type to the default ("Bearer").

        Thread Safety:
            This method is **not** async and does **not** acquire
            ``_token_lock``.  It is safe to call from within
            ``get_oauth_token()`` (which already holds the lock) and from
            synchronous teardown paths.  External callers that may race
            with ``get_oauth_token()`` should ensure serialization, for
            example by awaiting ``get_oauth_token()`` first.
        """
        self._access_token = None
        self._token_type = "Bearer"  # Reset to default
        self._access_token_expiry_time = None
        # Clear auth header and cached token via public methods (no encapsulation breach)
        self._request_executor.clear_authorization_header()
        self._request_executor.clear_cached_token()

    def get_current_token(self) -> Tuple[Optional[str], str]:
        """
        Get current access token and token type without triggering refresh.

        Returns:
            Tuple of (access_token, token_type). token_type defaults to "Bearer".
        """
        return self._access_token, self._token_type

    def get_dpop_generator(self) -> Optional[Any]:
        """Get DPoP generator instance."""
        return self._dpop_generator

    def is_dpop_enabled(self) -> bool:
        """Check if DPoP is enabled for this OAuth client."""
        return self._dpop_enabled
