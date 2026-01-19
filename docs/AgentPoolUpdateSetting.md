# AgentPoolUpdateSetting

Setting for auto-update

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_type** | [**AgentType**](AgentType.md) |  | [optional] 
**continue_on_error** | **bool** | Continues the update even if some agents fail to update | [optional] 
**latest_version** | **str** | Latest version of the agent | [optional] 
**minimal_supported_version** | **str** | Minimal version of the agent | [optional] 
**pool_id** | **str** | ID of the agent pool that the settings apply to | [optional] [readonly] 
**pool_name** | **str** | Pool name | [optional] 
**release_channel** | [**ReleaseChannel**](ReleaseChannel.md) |  | [optional] 

## Example

```python
from okta.models.agent_pool_update_setting import AgentPoolUpdateSetting

# TODO update the JSON string below
json = "{}"
# create an instance of AgentPoolUpdateSetting from a JSON string
agent_pool_update_setting_instance = AgentPoolUpdateSetting.from_json(json)
# print the JSON string representation of the object
print(AgentPoolUpdateSetting.to_json())

# convert the object into a dict
agent_pool_update_setting_dict = agent_pool_update_setting_instance.to_dict()
# create an instance of AgentPoolUpdateSetting from a dict
agent_pool_update_setting_from_dict = AgentPoolUpdateSetting.from_dict(agent_pool_update_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


