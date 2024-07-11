# WebAuthnUserFactor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**WebAuthnUserFactorProfile**](WebAuthnUserFactorProfile.md) |  | [optional] 

## Example

```python
from openapi_client.models.web_authn_user_factor import WebAuthnUserFactor

# TODO update the JSON string below
json = "{}"
# create an instance of WebAuthnUserFactor from a JSON string
web_authn_user_factor_instance = WebAuthnUserFactor.from_json(json)
# print the JSON string representation of the object
print(WebAuthnUserFactor.to_json())

# convert the object into a dict
web_authn_user_factor_dict = web_authn_user_factor_instance.to_dict()
# create an instance of WebAuthnUserFactor from a dict
web_authn_user_factor_from_dict = WebAuthnUserFactor.from_dict(web_authn_user_factor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


