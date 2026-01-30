# AgentPool

An agent pool is a collection of agents that serve a common purpose. An agent pool has a unique ID within an org, and contains a collection of agents disjoint to every other agent pool, meaning that no two agent pools share an agent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents** | [**List[Agent]**](Agent.md) |  | [optional] 
**disrupted_agents** | **int** | Number of agents in the pool that are in a disrupted state | [optional] 
**id** | **str** | Agent pool ID | [optional] [readonly] 
**inactive_agents** | **int** | Number of agents in the pool that are in an inactive state | [optional] 
**name** | **str** | Agent pool name | [optional] 
**operational_status** | [**OperationalStatus**](OperationalStatus.md) |  | [optional] 
**type** | [**AgentType**](AgentType.md) |  | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.agent_pool import AgentPool

# TODO update the JSON string below
json = "{}"
# create an instance of AgentPool from a JSON string
agent_pool_instance = AgentPool.from_json(json)
# print the JSON string representation of the object
print(AgentPool.to_json())

# convert the object into a dict
agent_pool_dict = agent_pool_instance.to_dict()
# create an instance of AgentPool from a dict
agent_pool_from_dict = AgentPool.from_dict(agent_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


