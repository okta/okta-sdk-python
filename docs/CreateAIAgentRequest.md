# CreateAIAgentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | The ID of the connected app for the AI agent | [optional] 
**profile** | [**AIAgentProfile**](AIAgentProfile.md) |  | [optional] 

## Example

```python
from okta.models.create_ai_agent_request import CreateAIAgentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAIAgentRequest from a JSON string
create_ai_agent_request_instance = CreateAIAgentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAIAgentRequest.to_json())

# convert the object into a dict
create_ai_agent_request_dict = create_ai_agent_request_instance.to_dict()
# create an instance of CreateAIAgentRequest from a dict
create_ai_agent_request_from_dict = CreateAIAgentRequest.from_dict(create_ai_agent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


