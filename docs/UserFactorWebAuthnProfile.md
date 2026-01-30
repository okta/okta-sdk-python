# UserFactorWebAuthnProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticator_name** | **str** | Human-readable name of the authenticator  &gt; **Note:** This name is set from the AAGUID metadata during enrollment. It can&#39;t be changed in the Admin Console or by using any Okta APIs. | [optional] 
**credential_id** | **str** | ID for the factor credential | [optional] 

## Example

```python
from okta.models.user_factor_web_authn_profile import UserFactorWebAuthnProfile

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorWebAuthnProfile from a JSON string
user_factor_web_authn_profile_instance = UserFactorWebAuthnProfile.from_json(json)
# print the JSON string representation of the object
print(UserFactorWebAuthnProfile.to_json())

# convert the object into a dict
user_factor_web_authn_profile_dict = user_factor_web_authn_profile_instance.to_dict()
# create an instance of UserFactorWebAuthnProfile from a dict
user_factor_web_authn_profile_from_dict = UserFactorWebAuthnProfile.from_dict(user_factor_web_authn_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


