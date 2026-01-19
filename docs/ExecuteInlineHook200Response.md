# ExecuteInlineHook200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commands** | [**List[UserImportResponseCommandsInner]**](UserImportResponseCommandsInner.md) | The &#x60;commands&#x60; object is where you can provide commands to Okta. It is an array that allows you to send multiple commands. Each array element needs to consist of a type-value pair. | [optional] 
**error** | [**UserImportResponseError**](UserImportResponseError.md) |  | [optional] 

## Example

```python
from okta.models.execute_inline_hook200_response import ExecuteInlineHook200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteInlineHook200Response from a JSON string
execute_inline_hook200_response_instance = ExecuteInlineHook200Response.from_json(json)
# print the JSON string representation of the object
print(ExecuteInlineHook200Response.to_json())

# convert the object into a dict
execute_inline_hook200_response_dict = execute_inline_hook200_response_instance.to_dict()
# create an instance of ExecuteInlineHook200Response from a dict
execute_inline_hook200_response_from_dict = ExecuteInlineHook200Response.from_dict(execute_inline_hook200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


