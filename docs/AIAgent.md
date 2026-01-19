# AIAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | The ID of the connected app for the AI agent | [optional] 
**created** | **datetime** | Timestamp when the AI agent was created | [optional] [readonly] 
**id** | **str** | Unique ID for the AI agent | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the AI agent was updated | [optional] [readonly] 
**profile** | [**AIAgentProfile**](AIAgentProfile.md) |  | [optional] 
**status** | **str** | When an AI agent is created, it&#39;s in the STAGED status.  After credentials and owners are associated with the agent, it can be set to the ACTIVE status. | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.ai_agent import AIAgent

# TODO update the JSON string below
json = "{}"
# create an instance of AIAgent from a JSON string
ai_agent_instance = AIAgent.from_json(json)
# print the JSON string representation of the object
print(AIAgent.to_json())

# convert the object into a dict
ai_agent_dict = ai_agent_instance.to_dict()
# create an instance of AIAgent from a dict
ai_agent_from_dict = AIAgent.from_dict(ai_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


