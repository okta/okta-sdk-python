# ProfileMappingProperty

A target property, in string form, that maps to a valid [JSON Schema Draft](https://tools.ietf.org/html/draft-zyp-json-schema-04) document.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **str** | Combination or single source properties that are mapped to the target property | [optional] 
**push_status** | [**ProfileMappingPropertyPushStatus**](ProfileMappingPropertyPushStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.profile_mapping_property import ProfileMappingProperty

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileMappingProperty from a JSON string
profile_mapping_property_instance = ProfileMappingProperty.from_json(json)
# print the JSON string representation of the object
print(ProfileMappingProperty.to_json())

# convert the object into a dict
profile_mapping_property_dict = profile_mapping_property_instance.to_dict()
# create an instance of ProfileMappingProperty from a dict
profile_mapping_property_form_dict = profile_mapping_property.from_dict(profile_mapping_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


