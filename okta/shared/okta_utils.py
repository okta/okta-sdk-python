""" Common utility methods """
from os import getcwd, path, sep, environ
from datetime import datetime
from sys import version_info
from platform import platform, mac_ver, win32_ver, linux_distribution, system

import json
import yaml
import dateutil.parser

from future.moves.urllib.parse import quote_plus as qp
from okta import __version__ as OKTA_VERSION
from ..models.okta_api_error import OktaApiError


class Utils(object):
    """ Check for non-constructor configuration in the following hierarchy:
        1. Environment variables
        2. okta.yaml file from the developer's application root directory
        3. okta.yaml file from ~/.okta/okta.yaml
        4. Defaults
    """

    @staticmethod
    def get_config(key):
        """
        Properly set the config value for the key
        """
        if key == 'orgUrl':
            if environ.get('OKTA_CLIENT'):
                return environ.get('OKTA_CLIENT')

        if key == 'token':
            if environ.get('OKTA_TOKEN'):
                return environ.get('OKTA_TOKEN')

        config = Utils.check_for_config_files()
        if config.get('okta') and config.get('okta').get('client'):
            # Found .yaml config file
            return config['okta']['client'].get(key)

    @staticmethod
    def check_for_config_files():
        """
        Checks for known locations for Okta configuration files.
        """
        locations = [getcwd() + '/okta.yaml', path.abspath(sep) + '.okta/okta.yaml']
        for config_path in locations:
            if path.exists(config_path):
                with open(config_path, 'r') as yaml_file:
                    try:
                        return yaml.load(yaml_file)
                    except yaml.YAMLError as error:
                        raise ValueError(error)

    @staticmethod
    def validate_response(response):
        """
        Verifies that there is no error, returns the class object
        """
        r_json = response.json()
        if response.status_code >= 200 and response.status_code < 300:
            return r_json
        else:
            raise OktaApiError(r_json)

    @staticmethod
    def to_json(obj):
        """
        Converts OktaObject into dictionary for serialization.
        """
        def default_parser(obj):
            if hasattr(obj, '_map'):
                return obj._map
            if isinstance(obj, datetime):
                return obj.strftime('%Y-%m-%dT%H:%M:%SZ')
            return obj.__dict__
        return json.dumps(obj, default=default_parser)

    @staticmethod
    def build_query_params(**kwargs):
        """
        Urlencode all given kwargs.
        """
        query_string = ','.join([
            '%s=%s' % (key, qp(str(value))) for (key, value) in kwargs.items()
        ])
        return "?" + query_string if len(query_string) > 0 else query_string

    @staticmethod
    def get_okta_user_agent():
        os_info = platform()
        os_versions = {
            'Linux': '{} ({})'.format(linux_distribution()[0], os_info),
            'Windows': '{} ({})'.format(win32_ver()[0], os_info),
            'Darwin': '{} ({})'.format(mac_ver()[0], os_info)
        }

        python_version = '{}.{}.{}'.format(
            version_info.major,
            version_info.minor,
            version_info.micro
        )

        return 'okta-sdk-python/{} python/{} {}/{}'.format(
            OKTA_VERSION,
            python_version,
            system(),
            os_versions.get(system(), ''),
        )

    @staticmethod
    def parse_date(date):
        return dateutil.parser.parse(date)
        