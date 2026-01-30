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
Pagination utilities for Okta SDK.

Provides helper functions and classes to handle cursor-based pagination
in Okta API responses.
"""

from typing import Optional, Dict, Any
from urllib.parse import urlparse, parse_qs


class PaginationHelper:
    """
    Helper class for working with Okta API pagination.

    Okta uses cursor-based pagination with the 'after' parameter.
    The next page cursor is provided in the Link response header.
    """

    @staticmethod
    def extract_next_cursor(headers: Dict[str, Any]) -> Optional[str]:
        """
        Extract the 'after' cursor from the Link response header for pagination.

        The Link header format from Okta API:
            <https://domain.okta.com/api/v1/users?after=CURSOR>; rel="next"

        Args:
            headers: HTTP response headers dict

        Returns:
            The cursor string for the next page, or None if no more pages exist

        Example:
            >>> headers = {'Link': '<https://dev.okta.com/api/v1/users?after=abc123>; rel="next"'}
            >>> PaginationHelper.extract_next_cursor(headers)
            'abc123'
        """
        try:
            # Try both capitalized and lowercase 'link' headers
            link_header = headers.get("Link") or headers.get("link")

            if not link_header:
                return None

            # Parse the Link header to find the 'next' link
            # Format: <URL>; rel="next", <URL>; rel="self"
            links = link_header.split(",")

            for link in links:
                # Check if this is the 'next' link
                if 'rel="next"' in link or "rel='next'" in link:
                    # Extract URL from <URL>
                    url_part = link.split(";")[0].strip()
                    url = url_part.strip("<>").strip()

                    # Extract 'after' parameter from URL
                    parsed = urlparse(url)
                    query_params = parse_qs(parsed.query)

                    if "after" in query_params:
                        # Return the first value if it's a list
                        after_value = query_params["after"]
                        if isinstance(after_value, list) and len(after_value) > 0:
                            return after_value[0]
                        return str(after_value)

            return None

        except Exception:
            # Silently return None on parsing errors
            return None

    @staticmethod
    def has_next_page(headers: Dict[str, Any]) -> bool:
        """
        Check if there is a next page available.

        Args:
            headers: HTTP response headers dict

        Returns:
            True if a next page exists, False otherwise
        """
        return PaginationHelper.extract_next_cursor(headers) is not None

    @staticmethod
    def extract_pagination_info(headers: Dict[str, Any]) -> Dict[str, Optional[str]]:
        """
        Extract all pagination-related information from Link header.

        Args:
            headers: HTTP response headers dict

        Returns:
            Dict with 'next', 'prev', 'self' cursors if available

        Example:
            >>> headers = {'Link': '<https://dev.okta.com/api/v1/users?after=abc>; rel="next"'}
            >>> PaginationHelper.extract_pagination_info(headers)
            {'next': 'abc', 'prev': None, 'self': None}
        """
        info = {"next": None, "prev": None, "self": None}

        try:
            link_header = headers.get("Link") or headers.get("link")

            if not link_header:
                return info

            links = link_header.split(",")

            for link in links:
                # Extract rel type
                rel_type = None
                if 'rel="next"' in link:
                    rel_type = "next"
                elif 'rel="prev"' in link or 'rel="previous"' in link:
                    rel_type = "prev"
                elif 'rel="self"' in link:
                    rel_type = "self"

                if rel_type:
                    # Extract URL
                    url_part = link.split(";")[0].strip()
                    url = url_part.strip("<>").strip()

                    # Extract cursor parameter (usually 'after' or 'before')
                    parsed = urlparse(url)
                    query_params = parse_qs(parsed.query)

                    cursor = None
                    if "after" in query_params:
                        cursor = (
                            query_params["after"][0]
                            if isinstance(query_params["after"], list)
                            else query_params["after"]
                        )
                    elif "before" in query_params:
                        cursor = (
                            query_params["before"][0]
                            if isinstance(query_params["before"], list)
                            else query_params["before"]
                        )

                    info[rel_type] = cursor

            return info

        except Exception:
            return info


async def paginate_all(
    api_method, limit: int = 200, max_pages: Optional[int] = None, **kwargs
):
    """
    Automatically paginate through all results from an Okta API list method.

    This is a convenience function that handles pagination logic automatically.
    It requires the API method to be the '_with_http_info' variant that returns
    (data, response, error) tuples.

    Args:
        api_method: The API method to call (must be _with_http_info variant)
        limit: Number of results per page (default: 200, max usually 200)
        max_pages: Maximum number of pages to fetch (default: None = unlimited)
        **kwargs: Additional arguments to pass to the API method

    Yields:
        Individual items from each page

    Example:
        >>> async for user in paginate_all(client.list_users_with_http_info, limit=100):
        ...     print(user.profile.email)

        >>> # Collect all users
        >>> all_users = [user async for user in paginate_all(client.list_users_with_http_info)]
    """
    after_cursor = kwargs.pop("after", None)
    page_count = 0

    while True:
        # Check page limit
        if max_pages is not None and page_count >= max_pages:
            break

        page_count += 1

        # Make API call with current cursor
        data, response, error = await api_method(
            limit=limit, after=after_cursor, **kwargs
        )

        # Handle errors
        if error or not data:
            break

        # Yield each item
        for item in data:
            yield item

        # Get next cursor
        after_cursor = PaginationHelper.extract_next_cursor(response.headers)

        # No more pages
        if not after_cursor:
            break


async def paginate_pages(
    api_method, limit: int = 200, max_pages: Optional[int] = None, **kwargs
):
    """
    Paginate through results, yielding complete pages.

    Similar to paginate_all but yields entire pages instead of individual items.
    Useful when you need to process results in batches.

    Args:
        api_method: The API method to call (must be _with_http_info variant)
        limit: Number of results per page (default: 200)
        max_pages: Maximum number of pages to fetch (default: None = unlimited)
        **kwargs: Additional arguments to pass to the API method

    Yields:
        Tuples of (page_data, page_number, has_more)

    Example:
        >>> async for page_data, page_num, has_more in paginate_pages(client.list_users_with_http_info):
        ...     print(f"Processing page {page_num} with {len(page_data)} users")
        ...     # Process batch
        ...     if not has_more:
        ...         print("Last page!")
    """
    after_cursor = kwargs.pop("after", None)
    page_count = 0

    while True:
        # Check page limit
        if max_pages is not None and page_count >= max_pages:
            break

        page_count += 1

        # Make API call with current cursor
        data, response, error = await api_method(
            limit=limit, after=after_cursor, **kwargs
        )

        # Handle errors
        if error or not data:
            break

        # Get next cursor to determine if more pages exist
        after_cursor = PaginationHelper.extract_next_cursor(response.headers)
        has_more = after_cursor is not None

        # Yield page data
        yield data, page_count, has_more

        # No more pages
        if not has_more:
            break
