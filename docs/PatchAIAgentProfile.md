# PatchAIAgentProfile

Partial update for AI agent profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the AI agent | [optional] 
**name** | **str** | Unique name of the AI agent | [optional] 

## Example

```python
from okta.models.patch_ai_agent_profile import PatchAIAgentProfile

# TODO update the JSON string below
json = "{}"
# create an instance of PatchAIAgentProfile from a JSON string
patch_ai_agent_profile_instance = PatchAIAgentProfile.from_json(json)
# print the JSON string representation of the object
print(PatchAIAgentProfile.to_json())

# convert the object into a dict
patch_ai_agent_profile_dict = patch_ai_agent_profile_instance.to_dict()
# create an instance of PatchAIAgentProfile from a dict
patch_ai_agent_profile_from_dict = PatchAIAgentProfile.from_dict(patch_ai_agent_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


