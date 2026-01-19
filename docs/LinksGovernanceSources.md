# LinksGovernanceSources

Specifies link relations (see [Web Linking](https://www.rfc-editor.org/rfc/rfc8288)) available for the sources using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignee** | [**HrefObjectUserLink**](HrefObjectUserLink.md) |  | [optional] 
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 

## Example

```python
from okta.models.links_governance_sources import LinksGovernanceSources

# TODO update the JSON string below
json = "{}"
# create an instance of LinksGovernanceSources from a JSON string
links_governance_sources_instance = LinksGovernanceSources.from_json(json)
# print the JSON string representation of the object
print(LinksGovernanceSources.to_json())

# convert the object into a dict
links_governance_sources_dict = links_governance_sources_instance.to_dict()
# create an instance of LinksGovernanceSources from a dict
links_governance_sources_from_dict = LinksGovernanceSources.from_dict(links_governance_sources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


