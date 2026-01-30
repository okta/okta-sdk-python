# AIAgentResource

The AI agent resource associated with the operation. These properties are available after the operation completes successfully.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the AI agent resource | 
**status** | **str** | The status of the AI agent resource | 
**type** | **str** | The type of resource | 
**links** | [**LinksSelf**](LinksSelf.md) |  | 

## Example

```python
from okta.models.ai_agent_resource import AIAgentResource

# TODO update the JSON string below
json = "{}"
# create an instance of AIAgentResource from a JSON string
ai_agent_resource_instance = AIAgentResource.from_json(json)
# print the JSON string representation of the object
print(AIAgentResource.to_json())

# convert the object into a dict
ai_agent_resource_dict = ai_agent_resource_instance.to_dict()
# create an instance of AIAgentResource from a dict
ai_agent_resource_from_dict = AIAgentResource.from_dict(ai_agent_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


