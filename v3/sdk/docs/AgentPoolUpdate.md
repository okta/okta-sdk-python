# AgentPoolUpdate

Various information about agent auto update configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents** | [**List[Agent]**](Agent.md) |  | [optional] 
**agent_type** | [**AgentType**](AgentType.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**notify_admin** | **bool** |  | [optional] 
**reason** | **str** |  | [optional] 
**schedule** | [**AutoUpdateSchedule**](AutoUpdateSchedule.md) |  | [optional] 
**sort_order** | **int** |  | [optional] 
**status** | [**AgentUpdateJobStatus**](AgentUpdateJobStatus.md) |  | [optional] 
**target_version** | **str** |  | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from openapi_client.models.agent_pool_update import AgentPoolUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AgentPoolUpdate from a JSON string
agent_pool_update_instance = AgentPoolUpdate.from_json(json)
# print the JSON string representation of the object
print(AgentPoolUpdate.to_json())

# convert the object into a dict
agent_pool_update_dict = agent_pool_update_instance.to_dict()
# create an instance of AgentPoolUpdate from a dict
agent_pool_update_form_dict = agent_pool_update.from_dict(agent_pool_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


