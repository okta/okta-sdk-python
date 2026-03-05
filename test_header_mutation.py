"""
Simple test to verify OAuth header mutation fix
"""
import asyncio
from okta.http_client import HTTPClient


async def test_header_mutation():
    """Test that sending form data doesn't mutate shared headers"""

    # Initialize HTTPClient with minimal config
    http_config = {
        "headers": {
            "User-Agent": "test-client",
            "Accept": "application/json"
        }
    }
    http_client = HTTPClient(http_config)

    # Get initial default headers
    initial_headers = dict(http_client._default_headers)
    print(f"Initial headers: {initial_headers}")

    # Simulate an OAuth request with form data
    oauth_request = {
        "method": "POST",
        "url": "https://test.okta.com/oauth2/v1/token",
        "headers": {
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
        },
        "data": None,
        "form": {
            "grant_type": "client_credentials",
            "client_assertion": "test_jwt_token"
        }
    }

    # This should NOT mutate _default_headers
    try:
        # We'll get an error since we're not actually making a request,
        # but we just want to check header mutation doesn't happen
        # in the preparation phase
        result = await http_client.send_request(oauth_request)
    except Exception as e:
        # Expected to fail, we're just testing header mutation
        pass

    # Check headers after the request
    after_headers = dict(http_client._default_headers)
    print(f"After headers: {after_headers}")

    # Verify headers weren't mutated
    if initial_headers == after_headers:
        print("✅ SUCCESS: Headers were not mutated!")
        print("   Shared state is preserved correctly.")
        return True
    else:
        print("❌ FAILURE: Headers were mutated!")
        print(f"   Initial: {initial_headers}")
        print(f"   After:   {after_headers}")
        added = set(after_headers.keys()) - set(initial_headers.keys())
        removed = set(initial_headers.keys()) - set(after_headers.keys())
        if added:
            print(f"   Added keys: {added}")
        if removed:
            print(f"   Removed keys: {removed}")
        return False


if __name__ == '__main__':
    print("Testing OAuth header mutation fix...")
    print("=" * 60)
    result = asyncio.run(test_header_mutation())
    print("=" * 60)
    if result:
        print("All tests passed! ✅")
    else:
        print("Tests failed! ❌")
        exit(1)


