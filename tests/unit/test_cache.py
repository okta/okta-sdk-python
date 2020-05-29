from okta.cache.cache import Cache
from okta.cache.no_op_cache import NoOpCache
from okta.cache.okta_cache import OktaCache

import pytest
import time

TTI = 5.0
TTL = 5.0
KEY = ("https://example.com/sample/cache-key/test+test@test."
       "com?with=a&query=string")
VALUE = "54321"
ALT_KEY = ("https://sample.com/example/cache-key/test+2@test."
           "com?with=a&query=string")
ALT_VALUE = "dbca"


def test_cache_key_creation():
    cache = Cache()
    new_key = cache.create_key(KEY)
    assert new_key is not None
    assert new_key == KEY


def test_cache_add_entry():
    cache = OktaCache(TTL, TTI)
    cache.add(KEY, VALUE)
    assert cache._store[KEY]["value"] == VALUE


def test_cache_has_key():
    cache = OktaCache(TTL, TTI)

    assert(not cache.contains(KEY))

    cache.add(KEY, VALUE)

    assert(cache.contains(KEY))
    assert(not cache.contains(ALT_KEY))


def test_cache_get_value():
    cache = OktaCache(TTL, TTI)

    assert(cache.get(KEY) is None)
    cache.add(KEY, VALUE)
    assert(cache.get(KEY) is VALUE)


def test_cache_delete_value():
    cache = OktaCache(TTL, TTI)
    cache.add(KEY, VALUE)

    assert(cache.contains(KEY))
    cache.delete(KEY)
    assert(not cache.contains(KEY))


def test_cache_clear():
    cache = OktaCache(TTL, TTI)

    first_key = KEY
    first_value = VALUE

    second_key = ALT_KEY
    second_value = ALT_VALUE

    cache.add(first_key, first_value)
    cache.add(second_key, second_value)
    assert(cache.contains(first_key) and cache.contains(second_key))
    cache.clear()
    assert(not (cache.contains(first_key) or cache.contains(second_key)))


def test_cache_TTI():
    local_TTL = float(10)
    local_TTI = float(1)
    cache = OktaCache(local_TTL, local_TTI)

    assert(cache.get(KEY) is None)
    cache.add(KEY, VALUE)
    time.sleep(local_TTI / 2)
    assert(cache.get(KEY) is VALUE)  # resets TTI
    time.sleep(local_TTI)
    assert(cache.get(KEY) is None)


def test_cache_TTL():
    local_TTL = float(2)
    local_TTI = float(10)
    cache = OktaCache(local_TTL, local_TTI)
    KEY = "12345"
    VALUE = "54321"

    assert(cache.get(KEY) is None)
    cache.add(KEY, VALUE)
    time.sleep(local_TTL)
    assert(cache.get(KEY) is None)  # deleted by now

    cache.add(KEY, VALUE)
    time.sleep(local_TTL / 2)
    assert(cache.get(KEY) is VALUE)
    time.sleep(local_TTL / 2)
    assert(cache.get(KEY) is None)  # deleted by now


@pytest.mark.parametrize("value", [None, "string", 1, 1.0, True])
def test_no_op_cache_for_nothingness(value):
    cache = NoOpCache()

    assert cache.contains(value) is False
    cache.add(value, value)
    assert cache.get(value) is None
