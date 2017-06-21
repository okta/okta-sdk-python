from .okta_utils import Utils
from .http import Http

class Collection(object):
    def __init__(self, client, path, model):
        self._client = client
        self._org_url = self._client.orgUrl + path
        self._model = model
        self._slice = None

    def __iter__(self):
        next_page_url = self._org_url
        self._slice = self._slice or slice(0, None, 1)
        start = self._slice.start or 0
        stop = self._slice.stop
        step = self._slice.step or 1
        index = 0

        while True:
            r = self._client.http.get(next_page_url)
            r_json = Utils.validate_response(r)
            for obj in r_json:
                if (index - start) % step != 0:
                    index += 1
                    continue

                if stop is not None and index >= stop:
                    return

                # Convert json to correct object type
                if index >= start:
                    yield self._model(obj, self._client)
                index += 1

            if 'next' in r.links:
                print 'got next page'
                next_page_url = r.links['next']['url']
            else:
                break

    def __getitem__(self, key):
        if isinstance(key, slice):
            self._slice = key
            return self
        elif isinstance(key, str):
            # Call our api and return some instance
            # Ex: client.users['me']
            self._org_url = '{}/{}'.format(self._org_url, key)
            return self._model(Utils.validate_response(self._client.http.get(self._org_url)))
