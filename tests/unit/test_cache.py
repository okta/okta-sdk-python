from okta.cache.cache import Cache
from okta.cache.no_op_cache import NoOpCache
from okta.cache.okta_cache import OktaCache
from tests.mocks import mock_pause_function, mock_cache_return_none,\
    mock_cache_return_value, TTI, TTL, CACHE_KEY, CACHE_VALUE,\
    ALT_CACHE_KEY, ALT_CACHE_VALUE

import pytest
import time


@pytest.fixture(scope="module")
def setup(monkeypatch):
    monkeypatch.setattr(time, 'sleep', mock_pause_function)


def test_cache_key_creation():
    cache = Cache()
    new_key = cache.create_key(CACHE_KEY)
    assert new_key is not None
    assert new_key == CACHE_KEY


def test_cache_add_entry():
    cache = OktaCache(TTL, TTI)
    cache.add(CACHE_KEY, CACHE_VALUE)
    assert cache._store[CACHE_KEY]["value"] == CACHE_VALUE

    cache.add("test string", CACHE_VALUE)
    assert cache._store["test string"]["value"] == CACHE_VALUE


def test_cache_has_key():
    cache = OktaCache(TTL, TTI)

    assert(not cache.contains(CACHE_KEY))

    cache.add(CACHE_KEY, CACHE_VALUE)

    assert(cache.contains(CACHE_KEY))
    assert(not cache.contains(ALT_CACHE_KEY))


def test_cache_get_value():
    cache = OktaCache(TTL, TTI)

    assert(cache.get(CACHE_KEY) is None)
    cache.add(CACHE_KEY, CACHE_VALUE)
    assert(cache.get(CACHE_KEY) is CACHE_VALUE)


def test_cache_delete_value():
    cache = OktaCache(TTL, TTI)
    cache.add(CACHE_KEY, CACHE_VALUE)

    assert(cache.contains(CACHE_KEY))
    cache.delete(CACHE_KEY)
    assert(not cache.contains(CACHE_KEY))


def test_cache_clear():
    cache = OktaCache(TTL, TTI)

    first_key = CACHE_KEY
    first_value = CACHE_VALUE

    second_key = ALT_CACHE_KEY
    second_value = ALT_CACHE_VALUE

    cache.add(first_key, first_value)
    cache.add(second_key, second_value)
    assert(cache.contains(first_key) and cache.contains(second_key))
    cache.clear()
    assert(not (cache.contains(first_key) or cache.contains(second_key)))


def test_cache_TTI(monkeypatch):
    local_TTL = float(10)
    local_TTI = float(1)
    cache = OktaCache(local_TTL, local_TTI)

    assert(cache.get(CACHE_KEY) is None)
    cache.add(CACHE_KEY, CACHE_VALUE)
    time.sleep(local_TTI / 2)
    monkeypatch.setattr(OktaCache, 'get', mock_cache_return_value)
    assert(cache.get(CACHE_KEY) is CACHE_VALUE)  # resets TTI
    time.sleep(local_TTI)
    monkeypatch.setattr(OktaCache, 'get', mock_cache_return_none)
    assert(cache.get(CACHE_KEY) is None)


def test_cache_TTL(monkeypatch):
    local_TTL = float(2)
    local_TTI = float(10)
    cache = OktaCache(local_TTL, local_TTI)
    KEY = "12345"
    VALUE = "54321"

    assert(cache.get(KEY) is None)
    cache.add(KEY, VALUE)
    time.sleep(local_TTL)
    monkeypatch.setattr(OktaCache, 'get', mock_cache_return_none)
    assert(cache.get(KEY) is None)  # deleted by now

    cache.add(KEY, VALUE)
    time.sleep(local_TTL / 2)
    monkeypatch.setattr(OktaCache, 'get', mock_cache_return_value)
    assert(cache.get(KEY) is VALUE)
    time.sleep(local_TTL / 2)
    monkeypatch.setattr(OktaCache, 'get', mock_cache_return_none)
    assert(cache.get(KEY) is None)  # deleted by now


@pytest.mark.parametrize("value", [None, "string", 1, 1.0, True])
def test_no_op_cache_for_nothingness(value):
    cache = NoOpCache()

    assert cache.contains(value) is False
    cache.add(value, value)
    assert cache.get(value) is None
