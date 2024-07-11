# AuthenticatorMethodPushAllOfSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithms** | [**List[AuthenticatorMethodAlgorithm]**](AuthenticatorMethodAlgorithm.md) |  | [optional] 
**key_protection** | [**PushMethodKeyProtection**](PushMethodKeyProtection.md) |  | [optional] 
**transaction_types** | [**List[AuthenticatorMethodTransactionType]**](AuthenticatorMethodTransactionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.authenticator_method_push_all_of_settings import AuthenticatorMethodPushAllOfSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorMethodPushAllOfSettings from a JSON string
authenticator_method_push_all_of_settings_instance = AuthenticatorMethodPushAllOfSettings.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorMethodPushAllOfSettings.to_json())

# convert the object into a dict
authenticator_method_push_all_of_settings_dict = authenticator_method_push_all_of_settings_instance.to_dict()
# create an instance of AuthenticatorMethodPushAllOfSettings from a dict
authenticator_method_push_all_of_settings_from_dict = AuthenticatorMethodPushAllOfSettings.from_dict(authenticator_method_push_all_of_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


