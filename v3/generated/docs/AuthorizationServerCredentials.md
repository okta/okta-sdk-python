# AuthorizationServerCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signing** | [**AuthorizationServerCredentialsSigningConfig**](AuthorizationServerCredentialsSigningConfig.md) |  | [optional] 

## Example

```python
from openapi_client.models.authorization_server_credentials import AuthorizationServerCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationServerCredentials from a JSON string
authorization_server_credentials_instance = AuthorizationServerCredentials.from_json(json)
# print the JSON string representation of the object
print(AuthorizationServerCredentials.to_json())

# convert the object into a dict
authorization_server_credentials_dict = authorization_server_credentials_instance.to_dict()
# create an instance of AuthorizationServerCredentials from a dict
authorization_server_credentials_form_dict = authorization_server_credentials.from_dict(authorization_server_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


