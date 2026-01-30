# DeviceListAllOfEmbedded

List of associated users for the device if the `expand=user` query parameter is specified in the request. Use `expand=userSummary` to get only a summary of each associated user for the device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[DeviceUser]**](DeviceUser.md) | Users for the device | [optional] 

## Example

```python
from okta.models.device_list_all_of_embedded import DeviceListAllOfEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceListAllOfEmbedded from a JSON string
device_list_all_of_embedded_instance = DeviceListAllOfEmbedded.from_json(json)
# print the JSON string representation of the object
print(DeviceListAllOfEmbedded.to_json())

# convert the object into a dict
device_list_all_of_embedded_dict = device_list_all_of_embedded_instance.to_dict()
# create an instance of DeviceListAllOfEmbedded from a dict
device_list_all_of_embedded_from_dict = DeviceListAllOfEmbedded.from_dict(device_list_all_of_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


