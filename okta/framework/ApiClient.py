import requests
import json
import time
from okta.framework.Serializer import Serializer
from okta.framework.OktaError import OktaError
import six


class ApiClient(object):

    def __init__(self, *args, **kwargs):
        if 'pathname' not in kwargs:
            raise ValueError('A pathname must be provided to create an ApiClient')

        if 'base_url' in kwargs and kwargs['base_url']:
            self.base_url = kwargs['base_url'] + kwargs['pathname']
        elif len(args) > 0 and args[0]:
            self.base_url = args[0] + kwargs['pathname']
        else:
            raise ValueError('A base_url must be provided to create an ApiClient')

        if 'api_token' in kwargs and kwargs['api_token']:
            self.api_token = kwargs['api_token']
        elif len(args) > 1 and args[1]:
            self.api_token = args[1]
        else:
            raise ValueError('An api_token must be provied to create an ApiClient')

        self.api_version = 1
        self.max_attempts = 4

        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'SSWS ' + self.api_token
        }

        if 'headers' in kwargs:
            self.headers.update(kwargs['headers'])

    def get(self, url, params=None, attempts=0):
        params_str = self.__dict_to_query_params(params)
        resp = requests.get(url + params_str, headers=self.headers)
        attempts += 1
        if self.__check_response(resp, attempts):
            return resp
        else:
            return self.get(url, params, attempts)

    def put(self, url, data=None, params=None, attempts=0):
        if data:
            data = json.dumps(data, cls=Serializer)
        params_str = self.__dict_to_query_params(params)
        resp = requests.put(url + params_str, data=data, headers=self.headers)
        attempts += 1
        if self.__check_response(resp, attempts):
            return resp
        else:
            return self.put(url, data, params, attempts)

    def post(self, url, data=None, params=None, attempts=0):
        if data:
            data = json.dumps(data, cls=Serializer, separators=(',', ':'))
        params_str = self.__dict_to_query_params(params)
        resp = requests.post(url + params_str, data=data, headers=self.headers)
        attempts += 1
        if self.__check_response(resp, attempts):
            return resp
        else:
            return self.post(url, data, params, attempts)

    def delete(self, url, params=None, attempts=0):
        params_str = self.__dict_to_query_params(params)
        resp = requests.delete(url + params_str, headers=self.headers)
        attempts += 1
        if self.__check_response(resp, attempts):
            return resp
        else:
            return self.delete(url, params, attempts)

    def get_path(self, url_path, params=None):
        return self.get(self.base_url + url_path, params)

    def put_path(self, url_path, data=None, params=None):
        return self.put(self.base_url + url_path, data, params)

    def post_path(self, url_path, data=None, params=None):
        return self.post(self.base_url + url_path, data, params)

    def delete_path(self, url_path, params=None):
        return self.delete(self.base_url + url_path, params)

    def __check_response(self, resp, attempts=1):
        if resp is None:
            raise ValueError("A response wasn't received")

        if 200 <= resp.status_code < 300:
            return True

        # If we made it this far, we need to handle an exception
        if attempts >= self.max_attempts or resp.status_code != 429:
            raise OktaError(json.loads(resp.text))

        # Assume we're going to retry with exponential backoff
        time.sleep(2 ** (attempts - 1))

        return False

    @staticmethod
    def __dict_to_query_params(d):
        if d is None or len(d) == 0:
            return ''

        param_list = [param + '=' + (str(value).lower() if type(value) == bool else str(value))
                      for param, value in six.iteritems(d) if value is not None]
        return '?' + "&".join(param_list)
