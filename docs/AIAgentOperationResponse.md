# AIAgentOperationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **datetime** | Timestamp of when the AI agent operation completed | [optional] 
**created** | **datetime** | Timestamp of when the AI agent operation was created | 
**error_details** | [**ErrorDetails**](ErrorDetails.md) |  | [optional] 
**id** | **str** | ID of the AI agent operation | 
**resource** | [**AIAgentResource**](AIAgentResource.md) |  | [optional] 
**started** | **datetime** | Timestamp of when the AI agent operation started | [optional] 
**status** | **str** | The status of the AI agent operation | 
**type** | **str** | The AI agent operation type | 

## Example

```python
from okta.models.ai_agent_operation_response import AIAgentOperationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AIAgentOperationResponse from a JSON string
ai_agent_operation_response_instance = AIAgentOperationResponse.from_json(json)
# print the JSON string representation of the object
print(AIAgentOperationResponse.to_json())

# convert the object into a dict
ai_agent_operation_response_dict = ai_agent_operation_response_instance.to_dict()
# create an instance of AIAgentOperationResponse from a dict
ai_agent_operation_response_from_dict = AIAgentOperationResponse.from_dict(ai_agent_operation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


