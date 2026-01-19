# OAuth2ClientSecret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_secret** | **str** | The OAuth 2.0 client secret string | [optional] [readonly] 
**created** | **str** | Timestamp when the OAuth Client 2.0 Secret was created | [optional] [readonly] 
**id** | **str** | The unique ID of the OAuth Client Secret | [optional] [readonly] 
**last_updated** | **str** | Timestamp when the OAuth Client 2.0 Secret was updated | [optional] [readonly] 
**secret_hash** | **str** | OAuth 2.0 client secret string hash | [optional] [readonly] 
**status** | **str** | Status of the OAuth 2.0 Client Secret | [optional] [default to 'ACTIVE']
**links** | [**OAuthClientSecretLinks**](OAuthClientSecretLinks.md) |  | [optional] 

## Example

```python
from okta.models.o_auth2_client_secret import OAuth2ClientSecret

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2ClientSecret from a JSON string
o_auth2_client_secret_instance = OAuth2ClientSecret.from_json(json)
# print the JSON string representation of the object
print(OAuth2ClientSecret.to_json())

# convert the object into a dict
o_auth2_client_secret_dict = o_auth2_client_secret_instance.to_dict()
# create an instance of OAuth2ClientSecret from a dict
o_auth2_client_secret_from_dict = OAuth2ClientSecret.from_dict(o_auth2_client_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


