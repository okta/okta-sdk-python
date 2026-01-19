# WellKnownURIsRoot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**WellKnownURIsRootEmbedded**](WellKnownURIsRootEmbedded.md) |  | [optional] 
**links** | [**WellKnownURIsRootLinks**](WellKnownURIsRootLinks.md) |  | [optional] 

## Example

```python
from okta.models.well_known_uris_root import WellKnownURIsRoot

# TODO update the JSON string below
json = "{}"
# create an instance of WellKnownURIsRoot from a JSON string
well_known_uris_root_instance = WellKnownURIsRoot.from_json(json)
# print the JSON string representation of the object
print(WellKnownURIsRoot.to_json())

# convert the object into a dict
well_known_uris_root_dict = well_known_uris_root_instance.to_dict()
# create an instance of WellKnownURIsRoot from a dict
well_known_uris_root_from_dict = WellKnownURIsRoot.from_dict(well_known_uris_root_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


