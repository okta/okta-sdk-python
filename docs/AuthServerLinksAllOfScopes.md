# AuthServerLinksAllOfScopes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hints** | [**HrefHints**](HrefHints.md) |  | [optional] 
**href** | **str** | Link URI | 
**name** | **str** | Link name | [optional] [readonly] 
**templated** | **bool** | Indicates whether the link object&#39;s &#x60;href&#x60; property is a URI template. | [optional] [readonly] 
**type** | **str** | The media type of the link. If omitted, it is implicitly &#x60;application/json&#x60;. | [optional] [readonly] 

## Example

```python
from okta.models.auth_server_links_all_of_scopes import AuthServerLinksAllOfScopes

# TODO update the JSON string below
json = "{}"
# create an instance of AuthServerLinksAllOfScopes from a JSON string
auth_server_links_all_of_scopes_instance = AuthServerLinksAllOfScopes.from_json(json)
# print the JSON string representation of the object
print(AuthServerLinksAllOfScopes.to_json())

# convert the object into a dict
auth_server_links_all_of_scopes_dict = auth_server_links_all_of_scopes_instance.to_dict()
# create an instance of AuthServerLinksAllOfScopes from a dict
auth_server_links_all_of_scopes_from_dict = AuthServerLinksAllOfScopes.from_dict(auth_server_links_all_of_scopes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


