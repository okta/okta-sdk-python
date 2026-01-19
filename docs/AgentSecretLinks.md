# AgentSecretLinks

Specifies link relations (see [Web Linking](https://www.rfc-editor.org/rfc/rfc8288)) available for the current status of an AI agent using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification. This object is used for dynamic discovery of related resources and lifecycle operations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activate** | [**HrefObjectActivateLink**](HrefObjectActivateLink.md) |  | [optional] 
**deactivate** | [**HrefObjectDeactivateLink**](HrefObjectDeactivateLink.md) |  | [optional] 
**delete** | [**HrefObjectDeleteLink**](HrefObjectDeleteLink.md) |  | [optional] 

## Example

```python
from okta.models.agent_secret_links import AgentSecretLinks

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSecretLinks from a JSON string
agent_secret_links_instance = AgentSecretLinks.from_json(json)
# print the JSON string representation of the object
print(AgentSecretLinks.to_json())

# convert the object into a dict
agent_secret_links_dict = agent_secret_links_instance.to_dict()
# create an instance of AgentSecretLinks from a dict
agent_secret_links_from_dict = AgentSecretLinks.from_dict(agent_secret_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


