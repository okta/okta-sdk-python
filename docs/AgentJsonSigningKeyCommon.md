# AgentJsonSigningKeyCommon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** | Algorithm that&#39;s used in the JSON Web Key | [optional] 
**use** | **str** | Acceptable use of the JSON Web Key  You can only use signing keys for AI agents, so the value of &#x60;use&#x60; is always &#x60;sig&#x60;. | [optional] 

## Example

```python
from okta.models.agent_json_signing_key_common import AgentJsonSigningKeyCommon

# TODO update the JSON string below
json = "{}"
# create an instance of AgentJsonSigningKeyCommon from a JSON string
agent_json_signing_key_common_instance = AgentJsonSigningKeyCommon.from_json(json)
# print the JSON string representation of the object
print(AgentJsonSigningKeyCommon.to_json())

# convert the object into a dict
agent_json_signing_key_common_dict = agent_json_signing_key_common_instance.to_dict()
# create an instance of AgentJsonSigningKeyCommon from a dict
agent_json_signing_key_common_from_dict = AgentJsonSigningKeyCommon.from_dict(agent_json_signing_key_common_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


