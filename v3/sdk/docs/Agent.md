# Agent

Agent details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**is_hidden** | **bool** |  | [optional] 
**is_latest_g_aed_version** | **bool** |  | [optional] 
**last_connection** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**operational_status** | [**OperationalStatus**](OperationalStatus.md) |  | [optional] 
**pool_id** | **str** |  | [optional] 
**type** | [**AgentType**](AgentType.md) |  | [optional] 
**update_message** | **str** |  | [optional] 
**update_status** | [**AgentUpdateInstanceStatus**](AgentUpdateInstanceStatus.md) |  | [optional] 
**version** | **str** |  | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.agent import Agent

# TODO update the JSON string below
json = "{}"
# create an instance of Agent from a JSON string
agent_instance = Agent.from_json(json)
# print the JSON string representation of the object
print(Agent.to_json())

# convert the object into a dict
agent_dict = agent_instance.to_dict()
# create an instance of Agent from a dict
agent_from_dict = Agent.from_dict(agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


