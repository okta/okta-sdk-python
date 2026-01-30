# AIAgentProfile

AI agent profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the AI agent | [optional] 
**name** | **str** | Unique name of the AI agent | 

## Example

```python
from okta.models.ai_agent_profile import AIAgentProfile

# TODO update the JSON string below
json = "{}"
# create an instance of AIAgentProfile from a JSON string
ai_agent_profile_instance = AIAgentProfile.from_json(json)
# print the JSON string representation of the object
print(AIAgentProfile.to_json())

# convert the object into a dict
ai_agent_profile_dict = ai_agent_profile_instance.to_dict()
# create an instance of AIAgentProfile from a dict
ai_agent_profile_from_dict = AIAgentProfile.from_dict(ai_agent_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


