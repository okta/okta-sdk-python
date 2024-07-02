# ListProfileMappings

A collection of the profile mappings that include a subset of the profile mapping object's properties. The Profile Mapping object describes a mapping between an Okta User's and an App User's properties using [JSON Schema Draft 4](https://datatracker.ietf.org/doc/html/draft-zyp-json-schema-04).  > **Note:** Same type source/target mappings aren't supported by this API. Profile mappings must either be Okta->App or App->Okta.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for profile mapping | [optional] [readonly] 
**source** | [**ProfileMappingSource**](.md) |  | [optional] 
**target** | [**ProfileMappingTarget**](.md) |  | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_profile_mappings import ListProfileMappings

# TODO update the JSON string below
json = "{}"
# create an instance of ListProfileMappings from a JSON string
list_profile_mappings_instance = ListProfileMappings.from_json(json)
# print the JSON string representation of the object
print(ListProfileMappings.to_json())

# convert the object into a dict
list_profile_mappings_dict = list_profile_mappings_instance.to_dict()
# create an instance of ListProfileMappings from a dict
list_profile_mappings_from_dict = ListProfileMappings.from_dict(list_profile_mappings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


