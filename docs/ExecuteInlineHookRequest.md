# ExecuteInlineHookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_event_version** | **str** | The inline hook cloud version | [optional] 
**content_type** | **str** | The inline hook request header content | [optional] 
**event_id** | **str** | The individual inline hook request ID | [optional] 
**event_time** | **str** | The time the inline hook request was sent | [optional] 
**event_type_version** | **str** | The inline hook version | [optional] 
**data** | [**UserImportRequestData**](UserImportRequestData.md) |  | [optional] 
**event_type** | **str** | The type of inline hook. The user import inline hook type is &#x60;com.okta.import.transform&#x60;. | [optional] 
**source** | **str** | The ID of the user import inline hook | [optional] 
**request_type** | **str** | The type of inline hook request. For example, &#x60;com.okta.user.telephony.pre-enrollment&#x60;. | [optional] 

## Example

```python
from okta.models.execute_inline_hook_request import ExecuteInlineHookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteInlineHookRequest from a JSON string
execute_inline_hook_request_instance = ExecuteInlineHookRequest.from_json(json)
# print the JSON string representation of the object
print(ExecuteInlineHookRequest.to_json())

# convert the object into a dict
execute_inline_hook_request_dict = execute_inline_hook_request_instance.to_dict()
# create an instance of ExecuteInlineHookRequest from a dict
execute_inline_hook_request_from_dict = ExecuteInlineHookRequest.from_dict(execute_inline_hook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


