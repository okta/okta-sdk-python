# OAuthCredentials

Client authentication credentials for an [OAuth 2.0 Authorization Server](https://tools.ietf.org/html/rfc6749#section-2.3)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client** | [**OAuthCredentialsClient**](OAuthCredentialsClient.md) |  | [optional] 
**signing** | [**AppleClientSigning**](AppleClientSigning.md) |  | [optional] 

## Example

```python
from okta.models.o_auth_credentials import OAuthCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthCredentials from a JSON string
o_auth_credentials_instance = OAuthCredentials.from_json(json)
# print the JSON string representation of the object
print(OAuthCredentials.to_json())

# convert the object into a dict
o_auth_credentials_dict = o_auth_credentials_instance.to_dict()
# create an instance of OAuthCredentials from a dict
o_auth_credentials_from_dict = OAuthCredentials.from_dict(o_auth_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


