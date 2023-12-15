from okta.oauth import OAuth

"""
Testing OAuth.clear_access_token
"""
class WasCalled:
    def __init__(self):
        self.value = False

cache_delete_was_called = WasCalled
headers_pop_was_called = WasCalled

class mockCache:
    def delete(token):
        cache_delete_was_called.value = True

class mockHeaders:
    def pop(header, ignored):
        headers_pop_was_called.value = True

class mockRequestExecutor:
    def __init__(self, cache):
        self._cache = cache
        self._default_headers = mockHeaders

def test_oauth_clear_access_token():
    _mockRequestExecutor = mockRequestExecutor(mockCache)
    oauth = OAuth(_mockRequestExecutor, {})
    oauth.clear_access_token()
    assert cache_delete_was_called.value
    assert headers_pop_was_called.value

