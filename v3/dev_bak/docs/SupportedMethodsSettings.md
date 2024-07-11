# SupportedMethodsSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_protection** | **str** |  | [optional] 
**algorithms** | [**List[AuthenticatorMethodAlgorithm]**](AuthenticatorMethodAlgorithm.md) |  | [optional] 
**transaction_types** | [**List[AuthenticatorMethodTransactionType]**](AuthenticatorMethodTransactionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.supported_methods_settings import SupportedMethodsSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SupportedMethodsSettings from a JSON string
supported_methods_settings_instance = SupportedMethodsSettings.from_json(json)
# print the JSON string representation of the object
print(SupportedMethodsSettings.to_json())

# convert the object into a dict
supported_methods_settings_dict = supported_methods_settings_instance.to_dict()
# create an instance of SupportedMethodsSettings from a dict
supported_methods_settings_from_dict = SupportedMethodsSettings.from_dict(supported_methods_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


