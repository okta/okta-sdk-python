# AIAgentOperationListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AIAgentOperationResponse]**](AIAgentOperationResponse.md) |  | [optional] 
**links** | [**AIAgentOperationListResponseLinks**](AIAgentOperationListResponseLinks.md) |  | [optional] 

## Example

```python
from okta.models.ai_agent_operation_list_response import AIAgentOperationListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AIAgentOperationListResponse from a JSON string
ai_agent_operation_list_response_instance = AIAgentOperationListResponse.from_json(json)
# print the JSON string representation of the object
print(AIAgentOperationListResponse.to_json())

# convert the object into a dict
ai_agent_operation_list_response_dict = ai_agent_operation_list_response_instance.to_dict()
# create an instance of AIAgentOperationListResponse from a dict
ai_agent_operation_list_response_from_dict = AIAgentOperationListResponse.from_dict(ai_agent_operation_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


