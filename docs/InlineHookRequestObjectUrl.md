# InlineHookRequestObjectUrl

The URL of the API endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The URL value of the API endpoint | [optional] 

## Example

```python
from okta.models.inline_hook_request_object_url import InlineHookRequestObjectUrl

# TODO update the JSON string below
json = "{}"
# create an instance of InlineHookRequestObjectUrl from a JSON string
inline_hook_request_object_url_instance = InlineHookRequestObjectUrl.from_json(json)
# print the JSON string representation of the object
print(InlineHookRequestObjectUrl.to_json())

# convert the object into a dict
inline_hook_request_object_url_dict = inline_hook_request_object_url_instance.to_dict()
# create an instance of InlineHookRequestObjectUrl from a dict
inline_hook_request_object_url_from_dict = InlineHookRequestObjectUrl.from_dict(inline_hook_request_object_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


