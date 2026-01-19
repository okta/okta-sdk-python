# WellKnownURIObjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**representation** | **object** | The well-known URI content in JSON format | [optional] 
**links** | [**WellKnownURIArrayResponseLinks**](WellKnownURIArrayResponseLinks.md) |  | [optional] 

## Example

```python
from okta.models.well_known_uri_object_response import WellKnownURIObjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WellKnownURIObjectResponse from a JSON string
well_known_uri_object_response_instance = WellKnownURIObjectResponse.from_json(json)
# print the JSON string representation of the object
print(WellKnownURIObjectResponse.to_json())

# convert the object into a dict
well_known_uri_object_response_dict = well_known_uri_object_response_instance.to_dict()
# create an instance of WellKnownURIObjectResponse from a dict
well_known_uri_object_response_from_dict = WellKnownURIObjectResponse.from_dict(well_known_uri_object_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


