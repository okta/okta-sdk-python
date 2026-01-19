# OAuth2RefreshToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Client ID | [optional] 
**created** | **datetime** | Timestamp when the object was created | [optional] [readonly] 
**expires_at** | **datetime** | Expiration time of the OAuth 2.0 Token | [optional] [readonly] 
**id** | **str** | ID of the Token object | [optional] [readonly] 
**issuer** | **str** | The complete URL of the authorization server that issued the Token | [optional] 
**last_updated** | **datetime** | Timestamp when the object was last updated | [optional] [readonly] 
**scopes** | **List[str]** | The scope names attached to the Token | [optional] 
**status** | [**GrantOrTokenStatus**](GrantOrTokenStatus.md) |  | [optional] 
**user_id** | **str** | The ID of the user associated with the Token | [optional] 
**embedded** | [**OAuth2RefreshTokenEmbedded**](OAuth2RefreshTokenEmbedded.md) |  | [optional] 
**links** | [**OAuth2RefreshTokenLinks**](OAuth2RefreshTokenLinks.md) |  | [optional] 

## Example

```python
from okta.models.o_auth2_refresh_token import OAuth2RefreshToken

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2RefreshToken from a JSON string
o_auth2_refresh_token_instance = OAuth2RefreshToken.from_json(json)
# print the JSON string representation of the object
print(OAuth2RefreshToken.to_json())

# convert the object into a dict
o_auth2_refresh_token_dict = o_auth2_refresh_token_instance.to_dict()
# create an instance of OAuth2RefreshToken from a dict
o_auth2_refresh_token_from_dict = OAuth2RefreshToken.from_dict(o_auth2_refresh_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


