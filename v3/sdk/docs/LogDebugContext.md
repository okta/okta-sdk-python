# LogDebugContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**debug_data** | **Dict[str, object]** |  | [optional] [readonly] 

## Example

```python
from okta.models.log_debug_context import LogDebugContext

# TODO update the JSON string below
json = "{}"
# create an instance of LogDebugContext from a JSON string
log_debug_context_instance = LogDebugContext.from_json(json)
# print the JSON string representation of the object
print(LogDebugContext.to_json())

# convert the object into a dict
log_debug_context_dict = log_debug_context_instance.to_dict()
# create an instance of LogDebugContext from a dict
log_debug_context_from_dict = LogDebugContext.from_dict(log_debug_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


