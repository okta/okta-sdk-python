"""
Copyright 2021 - Present Okta, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import asyncio
import atexit
import inspect
import os
import sys

from .api_client_adapter import ApiClientAdapter
from .config.config_setter import ConfigSetter
from .config.config_validator import ConfigValidator
from .cache.no_op_cache import NoOpCache
from .cache.okta_cache import OktaCache
from .helpers import to_snake_case
from .request_executor import RequestExecutor

# TODO: consider creating a package (with or separate)
#parent_dir = os.path.dirname(os.path.realpath(__name__))
#sys.path.insert(0, parent_dir)

import okta.api as swagger_api

from okta.configuration import Configuration


def swagger_args_adapter(f):
    def wrapper(*okta_args, **okta_kwargs):
        """Convert okta's methods call to swagger's methods call.

        Adapt function signature:
        1)
        okta:
        create_user(create_user_req, query_params, **kwargs), where {'activate': False} in query_params
        swagger:
        create_user(create_user_req, **kwargs), where {'activate': False} in kwargs

        2)
        okta:
        activate_user(user_id, query_params, **kwargs), where {'sendEmail': False} in query_params
        swagger:
        activate_user(user_id, send_email, **kwargs), send_email - required parameter

        """
        swagger_arg_names = inspect.getfullargspec(f)[0]
        swagger_arg_names.remove('self')
        swagger_args = okta_args[:len(swagger_arg_names)]
        swagger_kwargs = okta_kwargs

        # check if some arguments are in okta's query_params, like "send_email" in docstring above
        swagger_args_list = []
        for arg in swagger_args:
            query_params = False
            if type(arg) == dict:
                for key in arg:
                    if to_snake_case(key) in swagger_arg_names:
                        swagger_kwargs.update({to_snake_case(key): arg[key]})
                        query_params = True
            if not query_params:
                swagger_args_list.append(arg)

        # adapt query_params
        if len(okta_args) > len(swagger_arg_names):
            for parameter in okta_args[len(swagger_arg_names):]:
                kwargs_to_snake_case = {to_snake_case(kw_name): kw_value for kw_name, kw_value in parameter.items()}
                swagger_kwargs.update(**kwargs_to_snake_case)
        swagger_kwargs.update({'async_req': True})
        # query_params can be passed with keyword
        if 'query_params' in okta_kwargs:
            query_params = okta_kwargs.pop('query_params')
            okta_kwargs.update(query_params)

        # TODO: to_snake_case some args, but we can have user.id as arg and it will be malformed
        #swagger_args_list = [to_snake_case(arg) for arg in swagger_args_list]
        swagger_kwargs = {to_snake_case(key): swagger_kwargs[key] for key in swagger_kwargs}
        return f(*swagger_args_list, **swagger_kwargs)
    return wrapper


class Client():
    """An Okta client object"""

    def __init__(self, user_config: dict = {}):
        # Load configuration
        client_config_setter = ConfigSetter()
        client_config_setter._apply_config({'client': user_config})
        self._config = client_config_setter.get_config()
        # Prune configuration to remove unnecesary fields
        self._config = client_config_setter._prune_config(self._config)
        # Validate configuration
        ConfigValidator(self._config)

        # set client variables since validation passes
        self._authorization_mode = self._config["client"]["authorizationMode"]
        self._base_url = self._config["client"]["orgUrl"]
        self._api_token = self._config["client"].get("token", None)
        self._client_id = None
        self._scopes = None
        self._private_key = None

        # Determine which cache to use
        cache = NoOpCache()
        if self._config["client"]["cache"]["enabled"] is True:
            if user_config.get("cacheManager", None) is None:
                time_to_idle = self._config["client"]["cache"]["defaultTti"]
                time_to_live = self._config["client"]["cache"]["defaultTtl"]
                cache = OktaCache(
                    time_to_live,
                    time_to_idle
                )
            else:
                cache = user_config.get("cacheManager")

        # Determine request executor to use
        self._request_executor = \
            user_config.get("requestExecutor", ApiClientAdapter)(
                configuration=self._config,
                cache=cache,
                http_client=user_config.get("httpClient", None))

        # set private key variables
        if self._authorization_mode == 'PrivateKey':
            self._client_id = self._config["client"]["clientId"]
            self._scopes = self._config["client"]["scopes"]
            self._private_key = self._config["client"]["privateKey"]

        # ------------------ v3 begin -----------------
        # get all api clients from swagger_client, resource clients in okta terms
        swagger_api_clients = inspect.getmembers(swagger_api, predicate=inspect.isclass)

        # configure client
        #configuration = Configuration()
        #configuration.host = orgUrl
        #configuration.api_key['Authorization'] = token
        #configuration.api_key_prefix['Authorization']='SSWS'
        #api_client_adapter = ApiClientAdapter(configuration)


        # assign all available methods in api clients to okta main client
        for api_client_name, api_client_class in swagger_api_clients:
            #client = api_client_class(api_client_adapter)
            client = api_client_class(self._request_executor)
            api_methods = inspect.getmembers(client, predicate=inspect.ismethod)
            for method_name, method in api_methods:
                if method_name != '__init__':
                    setattr(self, method_name, swagger_args_adapter(method))
        # ------------------ v3 end -----------------

    """
    Getters
    """

    def get_config(self):
        return self._config

    def get_scopes(self):
        return self._scopes

    def get_base_url(self):
        return self._base_url

    def get_request_executor(self):
        return self._request_executor

    """
    Misc
    """
    def set_custom_headers(self, headers):
        self._request_executor.set_custom_headers(headers)

    def clear_custom_headers(self):
        self._request_executor.clear_custom_headers()

    def get_custom_headers(self):
        return self._request_executor.get_custom_headers()

    def get_default_headers(self):
        return self._request_executor.get_default_headers()
