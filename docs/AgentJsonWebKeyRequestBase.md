# AgentJsonWebKeyRequestBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kid** | **str** | Unique identifier of the JSON Web Key in the AI agent&#39;s JSON Web Key Set (JWKS) | [optional] 
**status** | **str** | Status of the AI agent JSON Web Key | [optional] [default to 'ACTIVE']

## Example

```python
from okta.models.agent_json_web_key_request_base import AgentJsonWebKeyRequestBase

# TODO update the JSON string below
json = "{}"
# create an instance of AgentJsonWebKeyRequestBase from a JSON string
agent_json_web_key_request_base_instance = AgentJsonWebKeyRequestBase.from_json(json)
# print the JSON string representation of the object
print(AgentJsonWebKeyRequestBase.to_json())

# convert the object into a dict
agent_json_web_key_request_base_dict = agent_json_web_key_request_base_instance.to_dict()
# create an instance of AgentJsonWebKeyRequestBase from a dict
agent_json_web_key_request_base_from_dict = AgentJsonWebKeyRequestBase.from_dict(agent_json_web_key_request_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


