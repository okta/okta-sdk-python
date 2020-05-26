from okta.cache.cache import Cache
from okta.cache.no_op_cache import NoOpCache
from okta.cache.okta_cache import OktaCache

import pytest
import time

TTI = 5.0
TTL = 5.0


@pytest.mark.skip
def test_cache_key_creation():
    cache = Cache(TTL, TTI)
    key = "I am a string"
    new_key = cache.create_key(key)
    assert new_key is not None
    pass


def test_cache_key_creation_from_request():
    # TBD
    pass


def test_cache_add_entry():
    cache = OktaCache(TTL, TTI)
    key = "12345"
    value = "54321"
    cache.add(key, value)
    assert cache._store[key]["value"] == value


def test_cache_has_key():
    cache = OktaCache(TTL, TTI)
    key = "12345"
    value = "54321"

    assert(not cache.contains(key))

    cache.add(key, value)

    assert(cache.contains(key))
    assert(not cache.contains("key not in cache"))


def test_cache_get_value():
    cache = OktaCache(TTL, TTI)
    key = "12345"
    value = "54321"

    assert(cache.get(key) is None)
    cache.add(key, value)
    assert(cache.get(key) is value)


def test_cache_delete_value():
    cache = OktaCache(TTL, TTI)
    key = "12345"
    value = "54321"
    cache.add(key, value)

    assert(cache.contains(key))
    cache.delete(key)
    assert(not cache.contains(key))


def test_cache_clear():
    cache = OktaCache(TTL, TTI)

    first_key = "12345"
    first_value = "54321"

    second_key = "abcd"
    second_value = "dcba"

    cache.add(first_key, first_value)
    cache.add(second_key, second_value)
    assert(cache.contains(first_key) and cache.contains(second_key))
    cache.clear()
    assert(not (cache.contains(first_key) or cache.contains(second_key)))


def test_cache_TTI():
    local_TTL = float(10)
    local_TTI = float(1)
    cache = OktaCache(local_TTL, local_TTI)
    key = "12345"
    value = "54321"

    assert(cache.get(key) is None)
    cache.add(key, value)
    time.sleep(local_TTI / 2)
    assert(cache.get(key) is value)  # resets TTI
    time.sleep(local_TTI)
    assert(cache.get(key) is None)


def test_cache_TTL():
    local_TTL = float(2)
    local_TTI = float(10)
    cache = OktaCache(local_TTL, local_TTI)
    key = "12345"
    value = "54321"

    assert(cache.get(key) is None)
    cache.add(key, value)
    time.sleep(local_TTL)
    assert(cache.get(key) is None)  # deleted by now

    cache.add(key, value)
    time.sleep(local_TTL / 2)
    assert(cache.get(key) is value)
    time.sleep(local_TTL / 2)
    assert(cache.get(key) is None)  # deleted by now


@pytest.mark.parametrize("value", [None, "string", 1, 1.0, True])
def test_no_op_cache_for_nothingness(value):
    cache = NoOpCache()

    assert cache.contains(value) is False
    assert cache.get("any key") is None
