# OAuthApplicationCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signing** | [**ApplicationCredentialsSigning**](ApplicationCredentialsSigning.md) |  | [optional] 
**user_name_template** | [**ApplicationCredentialsUsernameTemplate**](ApplicationCredentialsUsernameTemplate.md) |  | [optional] 
**oauth_client** | [**ApplicationCredentialsOAuthClient**](ApplicationCredentialsOAuthClient.md) |  | [optional] 

## Example

```python
from okta.models.o_auth_application_credentials import OAuthApplicationCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthApplicationCredentials from a JSON string
o_auth_application_credentials_instance = OAuthApplicationCredentials.from_json(json)
# print the JSON string representation of the object
print(OAuthApplicationCredentials.to_json())

# convert the object into a dict
o_auth_application_credentials_dict = o_auth_application_credentials_instance.to_dict()
# create an instance of OAuthApplicationCredentials from a dict
o_auth_application_credentials_from_dict = OAuthApplicationCredentials.from_dict(o_auth_application_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


