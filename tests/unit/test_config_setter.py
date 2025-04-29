from okta.config.config_setter import ConfigSetter

"""
Testing Config Setter
"""

def test_env_variable_application(monkeypatch):
    config_setter = ConfigSetter()
    config_setter._apply_default_values()

    assert config_setter._config["client"]["oauthTokenRenewalOffset"] == 5
