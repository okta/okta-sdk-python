# InlineHookLinksCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**deactivate** | [**HrefObject**](HrefObject.md) | URL to deactivate the inline hook | [optional] 
**execute** | [**HrefObject**](HrefObject.md) | URL to test the inline hook | [optional] 

## Example

```python
from okta.models.inline_hook_links_create import InlineHookLinksCreate

# TODO update the JSON string below
json = "{}"
# create an instance of InlineHookLinksCreate from a JSON string
inline_hook_links_create_instance = InlineHookLinksCreate.from_json(json)
# print the JSON string representation of the object
print(InlineHookLinksCreate.to_json())

# convert the object into a dict
inline_hook_links_create_dict = inline_hook_links_create_instance.to_dict()
# create an instance of InlineHookLinksCreate from a dict
inline_hook_links_create_from_dict = InlineHookLinksCreate.from_dict(inline_hook_links_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


