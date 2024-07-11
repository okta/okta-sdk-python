# WellKnownOrgMetadataSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytics_collection_enabled** | **bool** |  | [optional] 
**bug_reporting_enabled** | **bool** |  | [optional] 
**om_enabled** | **bool** | Whether the legacy Okta Mobile application is enabled for the org | [optional] 

## Example

```python
from openapi_client.models.well_known_org_metadata_settings import WellKnownOrgMetadataSettings

# TODO update the JSON string below
json = "{}"
# create an instance of WellKnownOrgMetadataSettings from a JSON string
well_known_org_metadata_settings_instance = WellKnownOrgMetadataSettings.from_json(json)
# print the JSON string representation of the object
print(WellKnownOrgMetadataSettings.to_json())

# convert the object into a dict
well_known_org_metadata_settings_dict = well_known_org_metadata_settings_instance.to_dict()
# create an instance of WellKnownOrgMetadataSettings from a dict
well_known_org_metadata_settings_from_dict = WellKnownOrgMetadataSettings.from_dict(well_known_org_metadata_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


