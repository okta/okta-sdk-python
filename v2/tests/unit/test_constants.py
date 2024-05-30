import okta.models as models
from okta.constants import find_app_model

def test_find_app_model():
    expected = models.SamlApplication
    actual = find_app_model('SAML_1_1', 'office365')
    assert expected == actual

    expected = models.SwaApplication
    actual = find_app_model(None, 'template_swa')
    assert expected == actual

    expected = models.Application
    actual = find_app_model(None, 'unknown_application')
    assert expected == actual
