# LinksGovernanceResources

Specifies link relations (see [Web Linking](https://www.rfc-editor.org/rfc/rfc8288)) available for the resources using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | [**HrefObjectGovernanceResourcesLink**](HrefObjectGovernanceResourcesLink.md) |  | [optional] 

## Example

```python
from okta.models.links_governance_resources import LinksGovernanceResources

# TODO update the JSON string below
json = "{}"
# create an instance of LinksGovernanceResources from a JSON string
links_governance_resources_instance = LinksGovernanceResources.from_json(json)
# print the JSON string representation of the object
print(LinksGovernanceResources.to_json())

# convert the object into a dict
links_governance_resources_dict = links_governance_resources_instance.to_dict()
# create an instance of LinksGovernanceResources from a dict
links_governance_resources_from_dict = LinksGovernanceResources.from_dict(links_governance_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


