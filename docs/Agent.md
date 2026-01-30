# Agent

Agent details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the agent that&#39;s generated during installation | [optional] [readonly] 
**is_hidden** | **bool** | Determines if an agent is hidden from the Admin Console | [optional] 
**is_latest_g_aed_version** | **bool** | Determines if the agent is on the latest generally available version | [optional] 
**last_connection** | **int** | Unix timestamp in milliseconds when the agent last connected to Okta | [optional] 
**name** | **str** | Agent name | [optional] 
**operational_status** | [**OperationalStatus**](OperationalStatus.md) |  | [optional] 
**pool_id** | **str** | Pool ID | [optional] 
**type** | [**AgentType**](AgentType.md) |  | [optional] 
**update_message** | **str** | Status message of the agent | [optional] 
**update_status** | [**AgentUpdateInstanceStatus**](AgentUpdateInstanceStatus.md) |  | [optional] 
**version** | **str** | Agent version number | [optional] 
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


