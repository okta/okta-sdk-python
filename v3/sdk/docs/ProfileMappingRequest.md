# ProfileMappingRequest

The updated request body properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**Dict[str, ProfileMappingProperty]**](ProfileMappingProperty.md) |  | 

## Example

```python
from openapi_client.models.profile_mapping_request import ProfileMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileMappingRequest from a JSON string
profile_mapping_request_instance = ProfileMappingRequest.from_json(json)
# print the JSON string representation of the object
print(ProfileMappingRequest.to_json())

# convert the object into a dict
profile_mapping_request_dict = profile_mapping_request_instance.to_dict()
# create an instance of ProfileMappingRequest from a dict
profile_mapping_request_from_dict = ProfileMappingRequest.from_dict(profile_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


