# WellKnownURIArrayResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**representation** | **List[str]** | The well-known URI content in a JSON array of objects format | [optional] 
**links** | [**WellKnownURIArrayResponseLinks**](WellKnownURIArrayResponseLinks.md) |  | [optional] 

## Example

```python
from okta.models.well_known_uri_array_response import WellKnownURIArrayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WellKnownURIArrayResponse from a JSON string
well_known_uri_array_response_instance = WellKnownURIArrayResponse.from_json(json)
# print the JSON string representation of the object
print(WellKnownURIArrayResponse.to_json())

# convert the object into a dict
well_known_uri_array_response_dict = well_known_uri_array_response_instance.to_dict()
# create an instance of WellKnownURIArrayResponse from a dict
well_known_uri_array_response_from_dict = WellKnownURIArrayResponse.from_dict(well_known_uri_array_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


