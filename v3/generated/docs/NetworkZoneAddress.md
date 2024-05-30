# NetworkZoneAddress

Specifies the value of an IP address expressed using either `range` or `CIDR` form.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**NetworkZoneAddressType**](NetworkZoneAddressType.md) |  | [optional] 
**value** | **str** | Value in CIDR/range form depending on the type specified | [optional] 

## Example

```python
from openapi_client.models.network_zone_address import NetworkZoneAddress

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkZoneAddress from a JSON string
network_zone_address_instance = NetworkZoneAddress.from_json(json)
# print the JSON string representation of the object
print(NetworkZoneAddress.to_json())

# convert the object into a dict
network_zone_address_dict = network_zone_address_instance.to_dict()
# create an instance of NetworkZoneAddress from a dict
network_zone_address_form_dict = network_zone_address.from_dict(network_zone_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


