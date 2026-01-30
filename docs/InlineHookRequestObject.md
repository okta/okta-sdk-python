# InlineHookRequestObject

The API request that triggered the inline hook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier that Okta assigned to the API request | [optional] 
**ip_address** | **str** | The IP address of the client that made the API request | [optional] 
**method** | **str** | The HTTP request method of the API request | [optional] 
**url** | [**InlineHookRequestObjectUrl**](InlineHookRequestObjectUrl.md) |  | [optional] 

## Example

```python
from okta.models.inline_hook_request_object import InlineHookRequestObject

# TODO update the JSON string below
json = "{}"
# create an instance of InlineHookRequestObject from a JSON string
inline_hook_request_object_instance = InlineHookRequestObject.from_json(json)
# print the JSON string representation of the object
print(InlineHookRequestObject.to_json())

# convert the object into a dict
inline_hook_request_object_dict = inline_hook_request_object_instance.to_dict()
# create an instance of InlineHookRequestObject from a dict
inline_hook_request_object_from_dict = InlineHookRequestObject.from_dict(inline_hook_request_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


