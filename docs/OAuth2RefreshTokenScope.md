# OAuth2RefreshTokenScope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the Scope | [optional] 
**display_name** | **str** | Name of the end user displayed in a consent dialog | [optional] 
**id** | **str** | Scope object ID | [optional] [readonly] 
**name** | **str** | Scope name | [optional] 
**links** | [**OAuth2RefreshTokenScopeLinks**](OAuth2RefreshTokenScopeLinks.md) |  | [optional] 

## Example

```python
from okta.models.o_auth2_refresh_token_scope import OAuth2RefreshTokenScope

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2RefreshTokenScope from a JSON string
o_auth2_refresh_token_scope_instance = OAuth2RefreshTokenScope.from_json(json)
# print the JSON string representation of the object
print(OAuth2RefreshTokenScope.to_json())

# convert the object into a dict
o_auth2_refresh_token_scope_dict = o_auth2_refresh_token_scope_instance.to_dict()
# create an instance of OAuth2RefreshTokenScope from a dict
o_auth2_refresh_token_scope_from_dict = OAuth2RefreshTokenScope.from_dict(o_auth2_refresh_token_scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


