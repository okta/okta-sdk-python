# WellKnownOrgMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the Org | [optional] 
**pipeline** | [**PipelineType**](PipelineType.md) |  | [optional] 
**settings** | [**WellKnownOrgMetadataSettings**](WellKnownOrgMetadataSettings.md) |  | [optional] 
**links** | [**WellKnownOrgMetadataLinks**](WellKnownOrgMetadataLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.well_known_org_metadata import WellKnownOrgMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of WellKnownOrgMetadata from a JSON string
well_known_org_metadata_instance = WellKnownOrgMetadata.from_json(json)
# print the JSON string representation of the object
print(WellKnownOrgMetadata.to_json())

# convert the object into a dict
well_known_org_metadata_dict = well_known_org_metadata_instance.to_dict()
# create an instance of WellKnownOrgMetadata from a dict
well_known_org_metadata_form_dict = well_known_org_metadata.from_dict(well_known_org_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


