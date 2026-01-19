# OAuth2RefreshTokenEmbedded

The embedded resources related to the object if the `expand` query parameter is specified

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scopes** | [**List[OAuth2RefreshTokenScope]**](OAuth2RefreshTokenScope.md) | The scope objects attached to the Token | [optional] 

## Example

```python
from okta.models.o_auth2_refresh_token_embedded import OAuth2RefreshTokenEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2RefreshTokenEmbedded from a JSON string
o_auth2_refresh_token_embedded_instance = OAuth2RefreshTokenEmbedded.from_json(json)
# print the JSON string representation of the object
print(OAuth2RefreshTokenEmbedded.to_json())

# convert the object into a dict
o_auth2_refresh_token_embedded_dict = o_auth2_refresh_token_embedded_instance.to_dict()
# create an instance of OAuth2RefreshTokenEmbedded from a dict
o_auth2_refresh_token_embedded_from_dict = OAuth2RefreshTokenEmbedded.from_dict(o_auth2_refresh_token_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


