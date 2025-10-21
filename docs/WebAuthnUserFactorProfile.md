# WebAuthnUserFactorProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticator_name** | **str** |  | [optional] 
**credential_id** | **str** |  | [optional] 

## Example

```python
from okta.models.web_authn_user_factor_profile import WebAuthnUserFactorProfile

# TODO update the JSON string below
json = "{}"
# create an instance of WebAuthnUserFactorProfile from a JSON string
web_authn_user_factor_profile_instance = WebAuthnUserFactorProfile.from_json(json)
# print the JSON string representation of the object
print(WebAuthnUserFactorProfile.to_json())

# convert the object into a dict
web_authn_user_factor_profile_dict = web_authn_user_factor_profile_instance.to_dict()
# create an instance of WebAuthnUserFactorProfile from a dict
web_authn_user_factor_profile_from_dict = WebAuthnUserFactorProfile.from_dict(web_authn_user_factor_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


