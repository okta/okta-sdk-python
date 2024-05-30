# NetworkZoneLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | Format of the country value: length 2 [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. Do not use continent codes as they are treated as generic codes for undesignated countries. | [optional] 
**region** | **str** | Format of the region value (optional): region code [ISO-3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) appended to country code (&#x60;countryCode-regionCode&#x60;), or &#x60;null&#x60; if empty. Do not use continent codes as they are treated as generic codes for undesignated regions. | [optional] 

## Example

```python
from openapi_client.models.network_zone_location import NetworkZoneLocation

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkZoneLocation from a JSON string
network_zone_location_instance = NetworkZoneLocation.from_json(json)
# print the JSON string representation of the object
print(NetworkZoneLocation.to_json())

# convert the object into a dict
network_zone_location_dict = network_zone_location_instance.to_dict()
# create an instance of NetworkZoneLocation from a dict
network_zone_location_form_dict = network_zone_location.from_dict(network_zone_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


