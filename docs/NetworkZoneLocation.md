# NetworkZoneLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | The two-character ISO 3166-1 country code. Don&#39;t use continent codes since they are treated as generic codes for undesignated countries. &lt;br&gt;For example: &#x60;US&#x60; | [optional] 
**region** | **str** | (Optional) The ISO 3166-2 region code appended to the country code (&#x60;countryCode-regionCode&#x60;), or &#x60;null&#x60; if empty. Don&#39;t use continent codes since they are treated as generic codes for undesignated regions. &lt;br&gt;For example: &#x60;CA&#x60; (for &#x60;US-CA&#x60; country and region code) | [optional] 

## Example

```python
from okta.models.network_zone_location import NetworkZoneLocation

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkZoneLocation from a JSON string
network_zone_location_instance = NetworkZoneLocation.from_json(json)
# print the JSON string representation of the object
print(NetworkZoneLocation.to_json())

# convert the object into a dict
network_zone_location_dict = network_zone_location_instance.to_dict()
# create an instance of NetworkZoneLocation from a dict
network_zone_location_from_dict = NetworkZoneLocation.from_dict(network_zone_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


