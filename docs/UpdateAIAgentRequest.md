# UpdateAIAgentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | The ID of the connected app for the AI agent | [optional] 
**profile** | [**AIAgentProfile**](AIAgentProfile.md) |  | [optional] 

## Example

```python
from okta.models.update_ai_agent_request import UpdateAIAgentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAIAgentRequest from a JSON string
update_ai_agent_request_instance = UpdateAIAgentRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAIAgentRequest.to_json())

# convert the object into a dict
update_ai_agent_request_dict = update_ai_agent_request_instance.to_dict()
# create an instance of UpdateAIAgentRequest from a dict
update_ai_agent_request_from_dict = UpdateAIAgentRequest.from_dict(update_ai_agent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


