from okta.in_memory_cache import InMemoryCache
from okta.default_cache_middlware import DefaultCacheMiddleware


class HTTPClient:
    def __init__(self, http_config={}):
        self._default_headers = {}
        self._requestExecutor = http_config.get("request_executor", None)
        self._in_memory_cache = http_config.get(
            "in_memory_cache") or InMemoryCache()
        if http_config.get("cache_middleware") is not None:
            self._cache_middleware = http_config.get("cache_middleware") or\
                DefaultCacheMiddleware()
        self._oauth = http_config.get("oauth")

    def add_header(self, new_header):
        self._default_headers.update(new_header)
