# ProfileMappingSource

The parameter is the source of a profile mapping and is a valid [JSON Schema Draft 4](https://datatracker.ietf.org/doc/html/draft-zyp-json-schema-04) document with the following properties. The data type can be an app instance or an Okta object.  > **Note:** If the source is Okta and the UserTypes feature isn't enabled, then the source `_links` only has a link to the schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the application instance or userType | [optional] [readonly] 
**name** | **str** | Variable name of the application instance or name of the referenced UserType | [optional] [readonly] 
**type** | **str** | Type of user referenced in the mapping | [optional] [readonly] 
**links** | [**SourceLinks**](SourceLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.profile_mapping_source import ProfileMappingSource

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileMappingSource from a JSON string
profile_mapping_source_instance = ProfileMappingSource.from_json(json)
# print the JSON string representation of the object
print(ProfileMappingSource.to_json())

# convert the object into a dict
profile_mapping_source_dict = profile_mapping_source_instance.to_dict()
# create an instance of ProfileMappingSource from a dict
profile_mapping_source_form_dict = profile_mapping_source.from_dict(profile_mapping_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


