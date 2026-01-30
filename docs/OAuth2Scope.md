# OAuth2Scope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent** | [**OAuth2ScopeConsentType**](OAuth2ScopeConsentType.md) |  | [optional] [default to OAuth2ScopeConsentType.IMPLICIT]
**default** | **bool** | Indicates if this Scope is a default scope | [optional] [default to False]
**description** | **str** | Description of the Scope | [optional] 
**display_name** | **str** | Name of the end user displayed in a consent dialog | [optional] 
**id** | **str** | Scope object ID | [optional] [readonly] 
**metadata_publish** | [**OAuth2ScopeMetadataPublish**](OAuth2ScopeMetadataPublish.md) |  | [optional] [default to OAuth2ScopeMetadataPublish.NO_CLIENTS]
**name** | **str** | Scope name | 
**optional** | **bool** | Indicates whether the Scope is optional. When set to &#x60;true&#x60;, the user can skip consent for the scope. | [optional] [default to False]
**system** | **bool** | Indicates if Okta created the Scope | [optional] [default to False]
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

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


