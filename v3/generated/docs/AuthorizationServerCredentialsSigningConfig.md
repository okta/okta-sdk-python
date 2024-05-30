# AuthorizationServerCredentialsSigningConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kid** | **str** |  | [optional] 
**last_rotated** | **datetime** |  | [optional] [readonly] 
**next_rotation** | **datetime** |  | [optional] [readonly] 
**rotation_mode** | [**AuthorizationServerCredentialsRotationMode**](AuthorizationServerCredentialsRotationMode.md) |  | [optional] 
**use** | [**AuthorizationServerCredentialsUse**](AuthorizationServerCredentialsUse.md) |  | [optional] 

## Example

```python
from openapi_client.models.authorization_server_credentials_signing_config import AuthorizationServerCredentialsSigningConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationServerCredentialsSigningConfig from a JSON string
authorization_server_credentials_signing_config_instance = AuthorizationServerCredentialsSigningConfig.from_json(json)
# print the JSON string representation of the object
print(AuthorizationServerCredentialsSigningConfig.to_json())

# convert the object into a dict
authorization_server_credentials_signing_config_dict = authorization_server_credentials_signing_config_instance.to_dict()
# create an instance of AuthorizationServerCredentialsSigningConfig from a dict
authorization_server_credentials_signing_config_form_dict = authorization_server_credentials_signing_config.from_dict(authorization_server_credentials_signing_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


