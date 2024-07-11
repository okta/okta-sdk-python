# ApplicationCredentialsOAuthClient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_key_rotation** | **bool** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**token_endpoint_auth_method** | [**OAuthEndpointAuthenticationMethod**](OAuthEndpointAuthenticationMethod.md) |  | [optional] 

## Example

```python
from openapi_client.models.application_credentials_o_auth_client import ApplicationCredentialsOAuthClient

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCredentialsOAuthClient from a JSON string
application_credentials_o_auth_client_instance = ApplicationCredentialsOAuthClient.from_json(json)
# print the JSON string representation of the object
print(ApplicationCredentialsOAuthClient.to_json())

# convert the object into a dict
application_credentials_o_auth_client_dict = application_credentials_o_auth_client_instance.to_dict()
# create an instance of ApplicationCredentialsOAuthClient from a dict
application_credentials_o_auth_client_from_dict = ApplicationCredentialsOAuthClient.from_dict(application_credentials_o_auth_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


