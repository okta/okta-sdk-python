import pickle
import pytest
import okta.models as models


def test_attribute_case():
    """Verify UserProfile can handle different case for basic and custom attributes."""
    first_name = 'TestFirstName'
    last_name = 'TestLastName'
    custom_attr = 'TestCustomAttr'
    config = {'firstName': first_name,
              'lastName': last_name,
              'CustomAttr': custom_attr}
    profile = models.UserProfile(config)
    assert profile.first_name == first_name
    assert profile.firstName == first_name
    assert profile.last_name == last_name
    assert profile.lastName == last_name
    assert profile.display_name is None
    assert profile.displayName is None
    assert profile.CustomAttr == custom_attr

    display_name = 'TestName'
    profile.displayName = display_name
    assert profile.display_name == display_name

    new_display_name = 'NewTestName'
    profile.display_name = new_display_name
    assert profile.displayName == new_display_name

    new_custom_attr = 'NewCustomAttr'
    profile.CustomAttr = new_custom_attr

    req_format = profile.request_format()
    assert req_format['CustomAttr'] == new_custom_attr
    assert req_format['firstName'] == first_name
    assert req_format['lastName'] == last_name
    assert req_format['displayName'] == new_display_name


def test_profile_serializing():
    """Verify UserProfile can be serialized and deserialized with pickle library."""
    first_name = 'TestFirstName'
    last_name = 'TestLastName'
    custom_attr = 'TestCustomAttr'
    config = {'firstName': first_name,
              'lastName': last_name,
              'CustomAttr': custom_attr}
    profile = models.UserProfile(config)
    pickled_profile = pickle.dumps(profile)
    unpickled_profile = pickle.loads(pickled_profile)
    assert isinstance(unpickled_profile, models.UserProfile)
    assert profile.as_dict() == unpickled_profile.as_dict()
