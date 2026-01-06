"""
Unit tests for the pagination module
"""
import pytest
from okta.pagination import PaginationHelper


class TestPaginationHelper:
    """Test cases for PaginationHelper class"""

    def test_extract_next_cursor_basic(self):
        """Test basic cursor extraction"""
        headers = {
            'Link': '<https://dev.okta.com/api/v1/users?after=abc123>; rel="next"'
        }
        cursor = PaginationHelper.extract_next_cursor(headers)
        assert cursor == 'abc123'

    def test_extract_next_cursor_with_additional_params(self):
        """Test cursor extraction with additional query parameters"""
        headers = {
            'Link': '<https://dev.okta.com/api/v1/users?after=xyz789&limit=200>; rel="next"'
        }
        cursor = PaginationHelper.extract_next_cursor(headers)
        assert cursor == 'xyz789'

    def test_extract_next_cursor_multiple_links(self):
        """Test cursor extraction from multiple Link headers"""
        headers = {
            'Link': '<https://dev.okta.com/api/v1/users?after=page2>; rel="next", <https://dev.okta.com/api/v1/users>; rel="self"'
        }
        cursor = PaginationHelper.extract_next_cursor(headers)
        assert cursor == 'page2'

    def test_extract_next_cursor_no_link_header(self):
        """Test when no Link header is present"""
        headers = {}
        cursor = PaginationHelper.extract_next_cursor(headers)
        assert cursor is None

    def test_extract_next_cursor_no_next_rel(self):
        """Test when Link header exists but no next rel"""
        headers = {
            'Link': '<https://dev.okta.com/api/v1/users>; rel="self"'
        }
        cursor = PaginationHelper.extract_next_cursor(headers)
        assert cursor is None

    def test_extract_next_cursor_lowercase_link(self):
        """Test with lowercase 'link' header"""
        headers = {
            'link': '<https://dev.okta.com/api/v1/users?after=lower123>; rel="next"'
        }
        cursor = PaginationHelper.extract_next_cursor(headers)
        assert cursor == 'lower123'

    def test_has_next_page_true(self):
        """Test has_next_page returns True when next page exists"""
        headers = {
            'Link': '<https://dev.okta.com/api/v1/users?after=abc>; rel="next"'
        }
        assert PaginationHelper.has_next_page(headers) is True

    def test_has_next_page_false(self):
        """Test has_next_page returns False when no next page"""
        headers = {
            'Link': '<https://dev.okta.com/api/v1/users>; rel="self"'
        }
        assert PaginationHelper.has_next_page(headers) is False

    def test_has_next_page_no_headers(self):
        """Test has_next_page returns False with empty headers"""
        headers = {}
        assert PaginationHelper.has_next_page(headers) is False

    def test_extract_pagination_info(self):
        """Test extracting all pagination information"""
        headers = {
            'Link': '<https://dev.okta.com/api/v1/users?after=next123>; rel="next", '
                   '<https://dev.okta.com/api/v1/users?after=current>; rel="self"'
        }
        info = PaginationHelper.extract_pagination_info(headers)
        assert info['next'] == 'next123'
        assert info['self'] == 'current'
        assert info['prev'] is None

    def test_extract_pagination_info_empty(self):
        """Test extract_pagination_info with no headers"""
        headers = {}
        info = PaginationHelper.extract_pagination_info(headers)
        assert info == {'next': None, 'prev': None, 'self': None}

    def test_extract_next_cursor_single_quotes(self):
        """Test cursor extraction with single quotes in rel"""
        headers = {
            'Link': "<https://dev.okta.com/api/v1/users?after=single123>; rel='next'"
        }
        cursor = PaginationHelper.extract_next_cursor(headers)
        assert cursor == 'single123'

    def test_extract_next_cursor_encoded(self):
        """Test cursor extraction with URL encoded cursor"""
        headers = {
            'Link': '<https://dev.okta.com/api/v1/users?after=encoded%3D%3D123>; rel="next"'
        }
        cursor = PaginationHelper.extract_next_cursor(headers)
        # Should return the encoded value as-is
        assert 'encoded' in cursor


if __name__ == '__main__':
    # Run tests with pytest
    pytest.main([__file__, '-v'])

