
import os
from openapi_client.configuration import Configuration
from pathlib import Path

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

class OktaConfigurationProvider():
    """
    Configuraiton Provider
    """
    def get_okta_configuration(self) -> Configuration:
        return self.get_configuration(os.path.expanduser('~/.okta/okta.yaml'))

    def get_configuration(self, file_path) -> Configuration:
        if Path(file_path).is_file():
            text = open(file_path).read()
            okta_config = load(text, Loader=Loader)
            config = Configuration()
            config.host = okta_config['oktaDomain']
            config.api_key['apiToken'] = okta_config['apiKey']
            config.api_key_prefix['apiToken'] = okta_config['apiKeyPrefix']
            config.verify_ssl = okta_config['verifySsl']
            return config

        return Configuration.get_default()