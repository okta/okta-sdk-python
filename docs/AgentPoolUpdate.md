# AgentPoolUpdate

Various information about agent auto-update configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents** | [**List[Agent]**](Agent.md) |  | [optional] 
**agent_type** | [**AgentType**](AgentType.md) |  | [optional] 
**enabled** | **bool** | Indicates if auto-update is enabled for the agent pool | [optional] 
**id** | **str** | ID of the agent pool update | [optional] [readonly] 
**name** | **str** | Name of the agent pool update | [optional] 
**notify_admin** | **bool** | Indicates if the admin is notified about the update | [optional] 
**reason** | **str** | Reason for the update | [optional] 
**schedule** | [**AutoUpdateSchedule**](AutoUpdateSchedule.md) |  | [optional] 
**sort_order** | **int** | Specifies the sort order | [optional] 
**status** | [**AgentUpdateJobStatus**](AgentUpdateJobStatus.md) |  | [optional] 
**target_version** | **str** | The agent version to update to | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.agent_pool_update import AgentPoolUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AgentPoolUpdate from a JSON string
agent_pool_update_instance = AgentPoolUpdate.from_json(json)
# print the JSON string representation of the object
print(AgentPoolUpdate.to_json())

# convert the object into a dict
agent_pool_update_dict = agent_pool_update_instance.to_dict()
# create an instance of AgentPoolUpdate from a dict
agent_pool_update_from_dict = AgentPoolUpdate.from_dict(agent_pool_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


