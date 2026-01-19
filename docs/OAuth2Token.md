# OAuth2Token


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Client ID | [optional] [readonly] 
**created** | **datetime** | Timestamp when the object was created | [optional] [readonly] 
**expires_at** | **datetime** | Expiration time of the OAuth 2.0 Token | [optional] [readonly] 
**id** | **str** | ID of the Token object | [optional] [readonly] 
**issuer** | **str** | The complete URL of the authorization server that issued the Token | [optional] 
**last_updated** | **datetime** | Timestamp when the object was last updated | [optional] [readonly] 
**scopes** | **List[str]** | Name of scopes attached to the Token | [optional] 
**status** | [**GrantOrTokenStatus**](GrantOrTokenStatus.md) |  | [optional] 
**user_id** | **str** |  | [optional] 
**embedded** | **Dict[str, object]** | Embedded resources related to the object if the &#x60;expand&#x60; query parameter is specified | [optional] [readonly] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.o_auth2_token import OAuth2Token

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2Token from a JSON string
o_auth2_token_instance = OAuth2Token.from_json(json)
# print the JSON string representation of the object
print(OAuth2Token.to_json())

# convert the object into a dict
o_auth2_token_dict = o_auth2_token_instance.to_dict()
# create an instance of OAuth2Token from a dict
o_auth2_token_from_dict = OAuth2Token.from_dict(o_auth2_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


