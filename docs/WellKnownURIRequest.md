# WellKnownURIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**representation** | **object** | The well-known URI content in JSON object format | 

## Example

```python
from okta.models.well_known_uri_request import WellKnownURIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WellKnownURIRequest from a JSON string
well_known_uri_request_instance = WellKnownURIRequest.from_json(json)
# print the JSON string representation of the object
print(WellKnownURIRequest.to_json())

# convert the object into a dict
well_known_uri_request_dict = well_known_uri_request_instance.to_dict()
# create an instance of WellKnownURIRequest from a dict
well_known_uri_request_from_dict = WellKnownURIRequest.from_dict(well_known_uri_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


