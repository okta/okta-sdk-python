# InlineHookLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**activate** | [**HrefObject**](HrefObject.md) | URL to activate the inline hook | [optional] 
**deactivate** | [**HrefObject**](HrefObject.md) | URL to deactivate the inline hook | [optional] 
**delete** | [**HrefObject**](HrefObject.md) | URL to delete the inline hook | [optional] 
**execute** | [**HrefObject**](HrefObject.md) | URL to test the inline hook | [optional] 

## Example

```python
from okta.models.inline_hook_links import InlineHookLinks

# TODO update the JSON string below
json = "{}"
# create an instance of InlineHookLinks from a JSON string
inline_hook_links_instance = InlineHookLinks.from_json(json)
# print the JSON string representation of the object
print(InlineHookLinks.to_json())

# convert the object into a dict
inline_hook_links_dict = inline_hook_links_instance.to_dict()
# create an instance of InlineHookLinks from a dict
inline_hook_links_from_dict = InlineHookLinks.from_dict(inline_hook_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


