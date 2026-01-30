# OrgTechnicalContactTypeLinks

Specifies link relations (see [Web Linking](https://www.rfc-editor.org/rfc/rfc8288)) available for the org technical Contact Type object using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**technical** | [**OrgTechnicalContactTypeLinksTechnical**](OrgTechnicalContactTypeLinksTechnical.md) |  | [optional] 

## Example

```python
from okta.models.org_technical_contact_type_links import OrgTechnicalContactTypeLinks

# TODO update the JSON string below
json = "{}"
# create an instance of OrgTechnicalContactTypeLinks from a JSON string
org_technical_contact_type_links_instance = OrgTechnicalContactTypeLinks.from_json(json)
# print the JSON string representation of the object
print(OrgTechnicalContactTypeLinks.to_json())

# convert the object into a dict
org_technical_contact_type_links_dict = org_technical_contact_type_links_instance.to_dict()
# create an instance of OrgTechnicalContactTypeLinks from a dict
org_technical_contact_type_links_from_dict = OrgTechnicalContactTypeLinks.from_dict(org_technical_contact_type_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


