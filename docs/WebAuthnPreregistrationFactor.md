# WebAuthnPreregistrationFactor

User factor variant used for WebAuthn preregistration factors

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp indicating when the factor was enrolled | [optional] [readonly] 
**factor_type** | [**UserFactorType**](UserFactorType.md) |  | [optional] 
**id** | **str** | ID of the factor | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp indicating when the factor was last updated | [optional] [readonly] 
**profile** | **object** | Specific attributes related to the factor | [optional] 
**provider** | [**UserFactorProvider**](UserFactorProvider.md) |  | [optional] 
**status** | [**UserFactorStatus**](UserFactorStatus.md) |  | [optional] 
**vendor_name** | **str** | Name of the factor vendor. This is usually the same as the provider. | [optional] [readonly] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.web_authn_preregistration_factor import WebAuthnPreregistrationFactor

# TODO update the JSON string below
json = "{}"
# create an instance of WebAuthnPreregistrationFactor from a JSON string
web_authn_preregistration_factor_instance = WebAuthnPreregistrationFactor.from_json(json)
# print the JSON string representation of the object
print(WebAuthnPreregistrationFactor.to_json())

# convert the object into a dict
web_authn_preregistration_factor_dict = web_authn_preregistration_factor_instance.to_dict()
# create an instance of WebAuthnPreregistrationFactor from a dict
web_authn_preregistration_factor_from_dict = WebAuthnPreregistrationFactor.from_dict(web_authn_preregistration_factor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


