# WellKnownOrgMetadataLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate** | [**HrefObject**](HrefObject.md) |  | [optional] 
**organization** | [**HrefObject**](HrefObject.md) |  | [optional] 

## Example

```python
from openapi_client.models.well_known_org_metadata_links import WellKnownOrgMetadataLinks

# TODO update the JSON string below
json = "{}"
# create an instance of WellKnownOrgMetadataLinks from a JSON string
well_known_org_metadata_links_instance = WellKnownOrgMetadataLinks.from_json(json)
# print the JSON string representation of the object
print(WellKnownOrgMetadataLinks.to_json())

# convert the object into a dict
well_known_org_metadata_links_dict = well_known_org_metadata_links_instance.to_dict()
# create an instance of WellKnownOrgMetadataLinks from a dict
well_known_org_metadata_links_form_dict = well_known_org_metadata_links.from_dict(well_known_org_metadata_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


