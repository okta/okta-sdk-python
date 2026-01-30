# AuthorizationServerCredentialsSigningConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kid** | **str** | The ID of the JSON Web Key used for signing tokens issued by the authorization server | [optional] [readonly] 
**last_rotated** | **datetime** | The timestamp when the authorization server started using the &#x60;kid&#x60; for signing tokens | [optional] [readonly] 
**next_rotation** | **datetime** | The timestamp when the authorization server changes the Key for signing tokens. This is only returned when &#x60;rotationMode&#x60; is set to &#x60;AUTO&#x60;. | [optional] [readonly] 
**rotation_mode** | [**AuthorizationServerCredentialsRotationMode**](AuthorizationServerCredentialsRotationMode.md) |  | [optional] 
**use** | [**AuthorizationServerCredentialsUse**](AuthorizationServerCredentialsUse.md) |  | [optional] 

## Example

```python
from okta.models.authorization_server_credentials_signing_config import AuthorizationServerCredentialsSigningConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationServerCredentialsSigningConfig from a JSON string
authorization_server_credentials_signing_config_instance = AuthorizationServerCredentialsSigningConfig.from_json(json)
# print the JSON string representation of the object
print(AuthorizationServerCredentialsSigningConfig.to_json())

# convert the object into a dict
authorization_server_credentials_signing_config_dict = authorization_server_credentials_signing_config_instance.to_dict()
# create an instance of AuthorizationServerCredentialsSigningConfig from a dict
authorization_server_credentials_signing_config_from_dict = AuthorizationServerCredentialsSigningConfig.from_dict(authorization_server_credentials_signing_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


