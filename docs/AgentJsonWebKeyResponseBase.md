# AgentJsonWebKeyResponseBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **str** | Timestamp of when the AI agent JSON Web Key was created | [optional] [readonly] 
**id** | **str** | The unique ID of the AI agent JSON Web Key | [optional] [readonly] 
**last_updated** | **str** | Timestamp of when the AI agent JSON Web Key was last updated | [optional] [readonly] 
**links** | [**AgentSecretLinks**](AgentSecretLinks.md) |  | [optional] 

## Example

```python
from okta.models.agent_json_web_key_response_base import AgentJsonWebKeyResponseBase

# TODO update the JSON string below
json = "{}"
# create an instance of AgentJsonWebKeyResponseBase from a JSON string
agent_json_web_key_response_base_instance = AgentJsonWebKeyResponseBase.from_json(json)
# print the JSON string representation of the object
print(AgentJsonWebKeyResponseBase.to_json())

# convert the object into a dict
agent_json_web_key_response_base_dict = agent_json_web_key_response_base_instance.to_dict()
# create an instance of AgentJsonWebKeyResponseBase from a dict
agent_json_web_key_response_base_from_dict = AgentJsonWebKeyResponseBase.from_dict(agent_json_web_key_response_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


