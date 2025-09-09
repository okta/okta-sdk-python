# OAuth2Scope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent** | [**OAuth2ScopeConsentType**](OAuth2ScopeConsentType.md) |  | [optional] 
**default** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**metadata_publish** | [**OAuth2ScopeMetadataPublish**](OAuth2ScopeMetadataPublish.md) |  | [optional] 
**name** | **str** |  | [optional] 
**system** | **bool** |  | [optional] 

## Example

```python
from okta.models.o_auth2_scope import OAuth2Scope

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2Scope from a JSON string
o_auth2_scope_instance = OAuth2Scope.from_json(json)
# print the JSON string representation of the object
print(OAuth2Scope.to_json())

# convert the object into a dict
o_auth2_scope_dict = o_auth2_scope_instance.to_dict()
# create an instance of OAuth2Scope from a dict
o_auth2_scope_from_dict = OAuth2Scope.from_dict(o_auth2_scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


