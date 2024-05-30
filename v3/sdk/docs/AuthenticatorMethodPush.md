# AuthenticatorMethodPush


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**AuthenticatorMethodPushAllOfSettings**](AuthenticatorMethodPushAllOfSettings.md) |  | [optional] 

## Example

```python
from openapi_client.models.authenticator_method_push import AuthenticatorMethodPush

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorMethodPush from a JSON string
authenticator_method_push_instance = AuthenticatorMethodPush.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorMethodPush.to_json())

# convert the object into a dict
authenticator_method_push_dict = authenticator_method_push_instance.to_dict()
# create an instance of AuthenticatorMethodPush from a dict
authenticator_method_push_form_dict = authenticator_method_push.from_dict(authenticator_method_push_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


