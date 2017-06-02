import os
import yaml
import json

from future.moves.urllib.parse import quote_plus as qp
from .models.okta_api_error import OktaApiError


class Utils(object):
    """ Check for configuration in the following hierarchy:
        1. okta.yaml file from ~/.okta/okta.yaml
        2. okta.yaml file from the developer's application root directory
    """

    @staticmethod
    def check_for_config():
        """
        Checks for known locations for Okta configuration files.
        """
        locations = ['~/.okta/okta.yaml', os.getcwd() + '/okta.yaml']
        for path in locations:
            if os.path.exists(path):
                with open(path, 'r') as yaml_file:
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
        if hasattr(obj, '_map'):
            hash = obj._map
        else:
            hash = obj
        return json.dumps(hash)

    @staticmethod
    def build_query_params(**kwargs):
        """
        Urlencode all given kwargs.
        """
        query_string = ','.join([
            '%s=%s' % (key, qp(str(value))) for (key, value) in kwargs.items()
        ])
        return "?" + query_string if len(query_string) > 0 else query_string
