# AgentPool

An AgentPool is a collection of agents that serve a common purpose. An AgentPool has a unique ID within an org, and contains a collection of agents disjoint to every other AgentPool (i.e. no two AgentPools share an Agent).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents** | [**List[Agent]**](Agent.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**operational_status** | [**OperationalStatus**](OperationalStatus.md) |  | [optional] 
**type** | [**AgentType**](AgentType.md) |  | [optional] 

## Example

```python
from openapi_client.models.agent_pool import AgentPool

# TODO update the JSON string below
json = "{}"
# create an instance of AgentPool from a JSON string
agent_pool_instance = AgentPool.from_json(json)
# print the JSON string representation of the object
print(AgentPool.to_json())

# convert the object into a dict
agent_pool_dict = agent_pool_instance.to_dict()
# create an instance of AgentPool from a dict
agent_pool_form_dict = agent_pool.from_dict(agent_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


