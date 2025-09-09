# ProfileMapping

The Profile Mapping object describes a mapping between an Okta User's and an App User's properties using [JSON Schema Draft 4](https://datatracker.ietf.org/doc/html/draft-zyp-json-schema-04).  > **Note:** Same type source/target mappings aren't supported by this API. Profile mappings must either be Okta->App or App->Okta.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for a profile mapping | [optional] [readonly] 
**properties** | [**Dict[str, ProfileMappingProperty]**](ProfileMappingProperty.md) |  | [optional] 
**source** | [**ProfileMappingSource**](.md) |  | [optional] 
**target** | [**ProfileMappingTarget**](.md) |  | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.profile_mapping import ProfileMapping

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileMapping from a JSON string
profile_mapping_instance = ProfileMapping.from_json(json)
# print the JSON string representation of the object
print(ProfileMapping.to_json())

# convert the object into a dict
profile_mapping_dict = profile_mapping_instance.to_dict()
# create an instance of ProfileMapping from a dict
profile_mapping_from_dict = ProfileMapping.from_dict(profile_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


