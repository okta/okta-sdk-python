# LogIpAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geographical_context** | [**LogGeographicalContext**](LogGeographicalContext.md) |  | [optional] 
**ip** | **str** |  | [optional] [readonly] 
**source** | **str** |  | [optional] [readonly] 
**version** | **str** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.log_ip_address import LogIpAddress

# TODO update the JSON string below
json = "{}"
# create an instance of LogIpAddress from a JSON string
log_ip_address_instance = LogIpAddress.from_json(json)
# print the JSON string representation of the object
print(LogIpAddress.to_json())

# convert the object into a dict
log_ip_address_dict = log_ip_address_instance.to_dict()
# create an instance of LogIpAddress from a dict
log_ip_address_form_dict = log_ip_address.from_dict(log_ip_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


