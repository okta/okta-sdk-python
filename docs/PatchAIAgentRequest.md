# PatchAIAgentRequest

JSON Merge Patch for AI agent. Send only the fields to update. Use null to remove a value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | The ID of the connected app for the AI Agent | [optional] 
**profile** | [**PatchAIAgentProfile**](PatchAIAgentProfile.md) |  | [optional] 

## Example

```python
from okta.models.patch_ai_agent_request import PatchAIAgentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchAIAgentRequest from a JSON string
patch_ai_agent_request_instance = PatchAIAgentRequest.from_json(json)
# print the JSON string representation of the object
print(PatchAIAgentRequest.to_json())

# convert the object into a dict
patch_ai_agent_request_dict = patch_ai_agent_request_instance.to_dict()
# create an instance of PatchAIAgentRequest from a dict
patch_ai_agent_request_from_dict = PatchAIAgentRequest.from_dict(patch_ai_agent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


