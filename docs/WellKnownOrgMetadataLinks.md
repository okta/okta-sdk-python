# WellKnownOrgMetadataLinks

Specifies link relations (see [Web Linking](https://www.rfc-editor.org/rfc/rfc8288)) available for this object using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate** | [**WellKnownOrgMetadataLinksAlternate**](WellKnownOrgMetadataLinksAlternate.md) |  | [optional] 
**organization** | [**WellKnownOrgMetadataLinksOrganization**](WellKnownOrgMetadataLinksOrganization.md) |  | [optional] 

## Example

```python
from okta.models.well_known_org_metadata_links import WellKnownOrgMetadataLinks

# TODO update the JSON string below
json = "{}"
# create an instance of WellKnownOrgMetadataLinks from a JSON string
well_known_org_metadata_links_instance = WellKnownOrgMetadataLinks.from_json(json)
# print the JSON string representation of the object
print(WellKnownOrgMetadataLinks.to_json())

# convert the object into a dict
well_known_org_metadata_links_dict = well_known_org_metadata_links_instance.to_dict()
# create an instance of WellKnownOrgMetadataLinks from a dict
well_known_org_metadata_links_from_dict = WellKnownOrgMetadataLinks.from_dict(well_known_org_metadata_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


