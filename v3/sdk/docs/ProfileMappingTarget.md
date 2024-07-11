# ProfileMappingTarget

The parameter is the target of a profile mapping and is a valid [JSON Schema Draft 4](https://datatracker.ietf.org/doc/html/draft-zyp-json-schema-04) document with the following properties. The data type can be an app instance or an Okta object.   > **Note:** If the target is Okta and the UserTypes feature isn't enabled, then the target `_links` only has a link to the schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the application instance or UserType | [optional] [readonly] 
**name** | **str** | Variable name of the application instance or name of the referenced userType | [optional] [readonly] 
**type** | **str** | Type of user referenced in the mapping | [optional] [readonly] 
**links** | [**SourceLinks**](SourceLinks.md) |  | [optional] 

## Example

```python
from okta.models.profile_mapping_target import ProfileMappingTarget

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileMappingTarget from a JSON string
profile_mapping_target_instance = ProfileMappingTarget.from_json(json)
# print the JSON string representation of the object
print(ProfileMappingTarget.to_json())

# convert the object into a dict
profile_mapping_target_dict = profile_mapping_target_instance.to_dict()
# create an instance of ProfileMappingTarget from a dict
profile_mapping_target_from_dict = ProfileMappingTarget.from_dict(profile_mapping_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


