from okta.client import Client as OktaClient
import pytest
import constants as const
import yaml
import os

ERROR_MESSAGE_ORG_URL_MISSING = (
    "Your Okta URL is missing. You can copy "
    "your domain from the Okta Developer "
    "Console. Follow these instructions to"
    f" find it: {const.FINDING_OKTA_DOMAIN}"
)
ERROR_MESSAGE_ORG_URL_NOT_HTTPS = (
    "Your Okta URL must start with 'https'."
)
ERROR_MESSAGE_AUTH_MODE_INVALID = (
    "The AuthorizationMode configuration "
    "option must be one of: "
    "[SSWS, PrivateKey]. "
    "You provided the SDK with "
)
ERROR_MESSAGE_ORG_URL_YOUROKTADOMAIN = (
    "Replace {{yourOktaDomain}} with your Okta domain. "
    "You can copy your domain from the Okta Developer Console. "
    "Follow these instructions to find it: "
    f"{const.FINDING_OKTA_DOMAIN}"
)

ERROR_MESSAGE_ORG_URL_ADMIN = (
    "Your Okta domain should not contain -admin. "
)

ERROR_MESSAGE_ORG_URL_TYPO = (
    "It looks like there's a typo in your Okta domain."
)

ERROR_MESSAGE_API_TOKEN_MISSING = (
    "Your Okta API token is missing. "
    "You can generate one in the Okta Developer"
    " Console. Follow these instructions:"
    f" {const.GET_OKTA_API_TOKEN}"
)

ERROR_MESSAGE_API_TOKEN_DEFAULT = (
    "Replace {{apiToken}} with your Okta API token. "
    "You can generate one in the Okta Developer Console. "
    f"Follow these instructions: {const.GET_OKTA_API_TOKEN}"
)

ERROR_MESSAGE_CLIENT_ID_MISSING = (
    "Your client ID is missing. You can copy it from the "
    "Okta Developer Console in the details for the Application "
    "you created. Follow these instructions to find it: "
    f"{const.FINDING_OKTA_APP_CRED}"
)

ERROR_MESSAGE_CLIENT_ID_DEFAULT = (
    "Replace {{clientId}} with the client ID of your Application. "
    "You can copy it from the Okta Developer Console in the "
    "details for the Application you created. Follow these "
    f"instructions to find it: {const.FINDING_OKTA_APP_CRED}"
)

ERROR_MESSAGE_SCOPES_PK_MISSING = (
    "When using authorization mode 'PrivateKey', you must supply "
    "'okta.client.scopes' and 'okta.client.privateKey'"
)

_GLOBAL_YAML_PATH = os.path.join(os.path.expanduser('~'), ".okta",
                                 "okta.yaml")
_LOCAL_YAML_PATH = os.path.join(os.getcwd(), "okta.yaml")


"""
Testing Okta Client Instantiation in different scenarios
"""


def test_constructor_user_config_empty():
    config = {}
    with pytest.raises(ValueError) as exception_info:
        OktaClient(input_config=config)
    assert ERROR_MESSAGE_ORG_URL_MISSING in str(exception_info.value)
    assert ERROR_MESSAGE_API_TOKEN_MISSING in str(exception_info.value)


def test_constructor_user_config_url_empty():
    config = {'orgUrl': '', 'token': 'TOKEN'}
    with pytest.raises(ValueError) as exception_info:
        OktaClient(input_config=config)
    assert ERROR_MESSAGE_ORG_URL_MISSING in str(exception_info.value)


def test_constructor_user_config_url_not_https():
    config = {'orgUrl': 'http://test.okta.com', 'token': 'TOKEN'}
    with pytest.raises(ValueError) as exception_info:
        OktaClient(input_config=config)
    assert ERROR_MESSAGE_ORG_URL_NOT_HTTPS in str(exception_info.value)
    assert const.FINDING_OKTA_DOMAIN in str(exception_info.value)


def test_constructor_user_config_url_has_yourOktaDomain():
    config = {
        'orgUrl': 'https://{yourOktaDomain}.okta.com', 'token': 'TOKEN'
    }
    with pytest.raises(ValueError) as exception_info:
        OktaClient(input_config=config)
    assert ERROR_MESSAGE_ORG_URL_YOUROKTADOMAIN in str(exception_info.value)


@ pytest.mark.parametrize("url", ["https://dev-admin.okta.com",
                                  "https://dev-admin.oktapreview.com",
                                  "https://dev-admin.okta-emea.com",
                                  "https://test-admin.okta.com"])
def test_constructor_user_config_url_has_admin(url):
    config = {
        'orgUrl': url, 'token': 'TOKEN'
    }
    with pytest.raises(ValueError) as exception_info:
        OktaClient(input_config=config)
    assert all(string in str(exception_info.value) for string in [
               ERROR_MESSAGE_ORG_URL_ADMIN, f"Current value: {url}"])


def test_constructor_user_config_url_dot_com_twice():
    url = 'https://test.okta.com.com'
    config = {
        'orgUrl': url, 'token': 'TOKEN'
    }
    with pytest.raises(ValueError) as exception_info:
        OktaClient(input_config=config)
    assert all(string in str(exception_info.value) for string in [
               ERROR_MESSAGE_ORG_URL_TYPO, f"Current value: {url}"])


def test_constructor_user_config_url_punctuation():
    # test for urls with '://' multiple times
    url = 'https://://test.okta.com'
    config = {
        'orgUrl': url, 'token': 'TOKEN'
    }
    with pytest.raises(ValueError) as exception_info:
        OktaClient(input_config=config)
    assert all(string in str(exception_info.value) for string in [
               ERROR_MESSAGE_ORG_URL_TYPO, f"Current value: {url}"])


def test_constructor_user_config_token_empty():
    config = {'orgUrl': 'https://test.okta.com', 'token': ''}
    with pytest.raises(ValueError) as exception_info:
        OktaClient(input_config=config)
    assert ERROR_MESSAGE_API_TOKEN_MISSING in str(exception_info.value)


def test_constructor_user_config_url_has_apiToken():
    config = {
        'orgUrl': 'https://test.okta.com', 'token': '{apiToken}'
    }
    with pytest.raises(ValueError) as exception_info:
        OktaClient(input_config=config)
    assert ERROR_MESSAGE_API_TOKEN_DEFAULT in str(exception_info.value)


def test_constructor_user_config_auth_mode_invalid():
    authorizationMode = "blah"
    config = {'orgUrl': "https://test.okta.com",
              'token': "TOKEN",
              'authorizationMode': authorizationMode}
    with pytest.raises(ValueError) as exception_info:
        OktaClient(input_config=config)
    assert all(string in str(exception_info.value) for string in [
               ERROR_MESSAGE_AUTH_MODE_INVALID, f"with {authorizationMode}"])


def test_constructor_user_config_SSWS():
    org_url = "https://test.okta.com"
    token = "TOKEN"
    config = {'orgUrl': org_url, 'token': token}
    client = OktaClient(input_config=config)
    loaded_config = client.get_config()
    assert org_url == loaded_config['client']['orgUrl']
    assert token == loaded_config['client']['token']


def test_constructor_user_config_PK():
    org_url = "https://test.okta.com"
    authorizationMode = "PrivateKey"
    client_id = "clientID"
    scopes = ["scope1"]
    private_key_hash = "private key hash"

    config = {
        'orgUrl': org_url,
        'authorizationMode': authorizationMode,
        'clientId': client_id,
        'scopes': scopes,
        'privateKey': private_key_hash
    }
    client = OktaClient(input_config=config)
    loaded_config = client.get_config()
    assert org_url == loaded_config['client']['orgUrl']
    assert authorizationMode == loaded_config['client']['authorizationMode']
    assert client_id == loaded_config['client']['clientId']
    assert scopes == loaded_config['client']['scopes']
    assert private_key_hash == loaded_config['client']['privateKey']


def test_constructor_user_config_PK_empty():
    org_url = "https://test.okta.com"
    authorizationMode = "PrivateKey"

    config = {
        'orgUrl': org_url,
        'authorizationMode': authorizationMode,
    }
    with pytest.raises(ValueError) as exception_info:
        OktaClient(input_config=config)
    assert all(string in str(exception_info.value) for string in [
               ERROR_MESSAGE_CLIENT_ID_MISSING, ERROR_MESSAGE_SCOPES_PK_MISSING
               ])


def test_constructor_user_config_PK_client_id_empty():
    org_url = "https://test.okta.com"
    authorizationMode = "PrivateKey"
    scopes = ["scope1"]
    private_key_hash = "private key hash"

    config = {
        'orgUrl': org_url,
        'authorizationMode': authorizationMode,
        'clientId': "",
        'scopes': scopes,
        'privateKey': private_key_hash
    }
    with pytest.raises(ValueError) as exception_info:
        OktaClient(input_config=config)
    assert all(string in str(exception_info.value) for string in [
               ERROR_MESSAGE_CLIENT_ID_MISSING
               ])


@ pytest.mark.parametrize("scopes,private_key", [([], "private key hash"),
                                                 (["scope1"], ""),
                                                 ([], "")])
def test_constructor_user_config_PK_scopes_and_or_private_key_empty(
        scopes,
        private_key):
    org_url = "https://test.okta.com"
    authorizationMode = "PrivateKey"
    client_id = "clientID"

    config = {
        'orgUrl': org_url,
        'authorizationMode': authorizationMode,
        'clientId': client_id,
        'scopes': scopes,
        'privateKey': private_key
    }
    with pytest.raises(ValueError) as exception_info:
        OktaClient(input_config=config)
    assert all(string in str(exception_info.value) for string in [
               ERROR_MESSAGE_SCOPES_PK_MISSING
               ])


"""
Testing constructor with YAML configurations
"""


def test_constructor_global_config_SSWS(fs):
    fs.pause()
    global_sample = os.path.join(os.path.dirname(
        __file__), "files", "SSWS-sample-global.yaml")
    with open(global_sample) as file:
        global_config = yaml.load(file, Loader=yaml.SafeLoader)
        org_url = global_config["okta"]["client"]["orgUrl"]
        token = global_config["okta"]["client"]["token"]
        fs.resume()
        fs.create_file(_GLOBAL_YAML_PATH, contents=yaml.dump(global_config))

    client = OktaClient()
    loaded_config = client.get_config()

    assert org_url == loaded_config['client']['orgUrl']
    assert token == loaded_config['client']['token']


def test_constructor_local_config_SSWS(fs):
    fs.pause()
    local_sample = os.path.join(os.path.dirname(
        __file__), "files", "SSWS-sample-local.yaml")
    with open(local_sample) as file:
        local_config = yaml.load(file, Loader=yaml.SafeLoader)
        org_url = local_config["okta"]["client"]["orgUrl"]
        token = local_config["okta"]["client"]["token"]
        fs.resume()
        fs.create_file(_LOCAL_YAML_PATH, contents=yaml.dump(local_config))

    client = OktaClient()
    loaded_config = client.get_config()

    assert org_url == loaded_config['client']['orgUrl']
    assert token == loaded_config['client']['token']


def test_constructor_global_config_PK(fs):
    fs.pause()
    global_sample = os.path.join(os.path.dirname(
        __file__), "files", "PK-sample-global.yaml")
    with open(global_sample) as file:
        global_config = yaml.load(file, Loader=yaml.SafeLoader)
        org_url = global_config["okta"]["client"]["orgUrl"]
        client_id = global_config["okta"]["client"]["clientId"]
        private_key = global_config["okta"]["client"]["privateKey"]
        fs.resume()
        fs.create_file(_GLOBAL_YAML_PATH, contents=yaml.dump(global_config))

    client = OktaClient()
    loaded_config = client.get_config()

    assert org_url == loaded_config['client']['orgUrl']
    assert client_id == loaded_config['client']['clientId']
    assert private_key == loaded_config['client']['privateKey']


def test_constructor_local_config_PK(fs):
    fs.pause()
    local_sample = os.path.join(os.path.dirname(
        __file__), "files", "PK-sample-local.yaml")
    with open(local_sample) as file:
        local_config = yaml.load(file, Loader=yaml.SafeLoader)
        org_url = local_config["okta"]["client"]["orgUrl"]
        client_id = local_config["okta"]["client"]["clientId"]
        private_key = local_config["okta"]["client"]["privateKey"]
        fs.resume()
        fs.create_file(_LOCAL_YAML_PATH, contents=yaml.dump(local_config))

    client = OktaClient()
    loaded_config = client.get_config()

    assert org_url == loaded_config['client']['orgUrl']
    assert client_id == loaded_config['client']['clientId']
    assert private_key == loaded_config['client']['privateKey']


def test_constructor_env_vars_SSWS():
    org_url = "https://test.okta.com"
    token = "TOKEN"
    os.environ["OKTA_CLIENT_ORGURL"] = org_url
    os.environ["OKTA_CLIENT_TOKEN"] = token

    client = OktaClient()
    loaded_config = client.get_config()

    os.environ.pop("OKTA_CLIENT_ORGURL")
    os.environ.pop("OKTA_CLIENT_TOKEN")

    assert org_url == loaded_config['client']['orgUrl']
    assert token == loaded_config['client']['token']


def test_constructor_env_vars_PK():
    authorizationMode = "PrivateKey"
    org_url = "https://test.okta.com"
    client_id = "clientID"
    scopes = "scope1,scope2,scope3"
    private_key = "private key"
    os.environ["OKTA_CLIENT_AUTHORIZATIONMODE"] = authorizationMode
    os.environ["OKTA_CLIENT_ORGURL"] = org_url
    os.environ["OKTA_CLIENT_CLIENTID"] = client_id
    os.environ["OKTA_CLIENT_SCOPES"] = scopes
    os.environ["OKTA_CLIENT_PRIVATEKEY"] = private_key

    client = OktaClient()
    loaded_config = client.get_config()

    os.environ.pop("OKTA_CLIENT_ORGURL")
    os.environ.pop("OKTA_CLIENT_AUTHORIZATIONMODE")
    os.environ.pop("OKTA_CLIENT_CLIENTID")
    os.environ.pop("OKTA_CLIENT_SCOPES")
    os.environ.pop("OKTA_CLIENT_PRIVATEKEY")

    assert authorizationMode == loaded_config['client']['authorizationMode']
    assert org_url == loaded_config['client']['orgUrl']
    assert client_id == loaded_config['client']['clientId']
    assert scopes.split(',') == loaded_config['client']['scopes']
    assert private_key == loaded_config['client']['privateKey']


def test_constructor_precedence_highest_rank_local_yaml(fs):
    # Setup Global config
    fs.pause()
    global_sample = os.path.join(os.path.dirname(
        __file__), "files", "SSWS-sample-global.yaml")
    with open(global_sample) as file:
        global_config = yaml.load(file, Loader=yaml.SafeLoader)
        global_org_url = global_config["okta"]["client"]["orgUrl"]
        global_token = global_config["okta"]["client"]["token"]
        fs.resume()
        fs.create_file(_GLOBAL_YAML_PATH, contents=yaml.dump(global_config))

    # Setup Local config
    fs.pause()
    local_sample = os.path.join(os.path.dirname(
        __file__), "files", "SSWS-sample-local.yaml")
    with open(local_sample) as file:
        local_config = yaml.load(file, Loader=yaml.SafeLoader)
        local_org_url = local_config["okta"]["client"]["orgUrl"]
        local_token = local_config["okta"]["client"]["token"]
        fs.resume()
        fs.create_file(_LOCAL_YAML_PATH, contents=yaml.dump(local_config))

    # Create client and validate values
    client = OktaClient()
    loaded_config = client.get_config()

    assert local_org_url == loaded_config['client']['orgUrl']
    assert local_token == loaded_config['client']['token']
    assert local_org_url != global_org_url
    assert local_token != global_token
    assert global_org_url != loaded_config['client']['orgUrl']
    assert global_token != loaded_config['client']['token']


def test_constructor_precedence_highest_rank_env_vars(fs):
    # Setup Local config
    fs.pause()
    local_sample = os.path.join(os.path.dirname(
        __file__), "files", "SSWS-sample-local.yaml")
    with open(local_sample) as file:
        local_config = yaml.load(file, Loader=yaml.SafeLoader)
        local_org_url = local_config["okta"]["client"]["orgUrl"]
        local_token = local_config["okta"]["client"]["token"]
        fs.resume()
        fs.create_file(_LOCAL_YAML_PATH, contents=yaml.dump(local_config))
    # Setup env. vars
    env_org_url = "https://test.env.okta.com"
    env_token = "envTOKEN"
    os.environ["OKTA_CLIENT_ORGURL"] = env_org_url
    os.environ["OKTA_CLIENT_TOKEN"] = env_token

    client = OktaClient()
    loaded_config = client.get_config()

    os.environ.pop("OKTA_CLIENT_ORGURL")
    os.environ.pop("OKTA_CLIENT_TOKEN")

    assert local_org_url != loaded_config['client']['orgUrl']
    assert local_token != loaded_config['client']['token']
    assert local_org_url != env_org_url
    assert local_token != env_token
    assert env_org_url == loaded_config['client']['orgUrl']
    assert env_token == loaded_config['client']['token']


def test_constructor_precedence_highest_rank_user_config(fs):
    # Setup env. vars
    env_org_url = "https://test.env.okta.com"
    env_token = "envTOKEN"
    os.environ["OKTA_CLIENT_ORGURL"] = env_org_url
    os.environ["OKTA_CLIENT_TOKEN"] = env_token

    # Setup user config
    user_org_url = "https://test.user.okta.com"
    user_token = "userTOKEN"
    config = {'orgUrl': user_org_url, 'token': user_token}

    client = OktaClient(config)
    loaded_config = client.get_config()

    os.environ.pop("OKTA_CLIENT_ORGURL")
    os.environ.pop("OKTA_CLIENT_TOKEN")

    assert user_org_url == loaded_config['client']['orgUrl']
    assert user_token == loaded_config['client']['token']
    assert user_org_url != env_org_url
    assert user_token != env_token
    assert env_org_url != loaded_config['client']['orgUrl']
    assert env_token != loaded_config['client']['token']
