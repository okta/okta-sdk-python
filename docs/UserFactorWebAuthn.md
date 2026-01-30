# UserFactorWebAuthn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**UserFactorWebAuthnProfile**](UserFactorWebAuthnProfile.md) |  | [optional] 

## Example

```python
from okta.models.user_factor_web_authn import UserFactorWebAuthn

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorWebAuthn from a JSON string
user_factor_web_authn_instance = UserFactorWebAuthn.from_json(json)
# print the JSON string representation of the object
print(UserFactorWebAuthn.to_json())

# convert the object into a dict
user_factor_web_authn_dict = user_factor_web_authn_instance.to_dict()
# create an instance of UserFactorWebAuthn from a dict
user_factor_web_authn_from_dict = UserFactorWebAuthn.from_dict(user_factor_web_authn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


