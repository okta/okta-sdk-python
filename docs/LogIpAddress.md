# LogIpAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geographical_context** | [**LogGeographicalContext**](LogGeographicalContext.md) |  | [optional] 
**ip** | **str** | IP address | [optional] [readonly] 
**source** | **str** | Details regarding the source | [optional] [readonly] 
**version** | **str** | IP address version | [optional] [readonly] 

## Example

```python
from okta.models.log_ip_address import LogIpAddress

# TODO update the JSON string below
json = "{}"
# create an instance of LogIpAddress from a JSON string
log_ip_address_instance = LogIpAddress.from_json(json)
# print the JSON string representation of the object
print(LogIpAddress.to_json())

# convert the object into a dict
log_ip_address_dict = log_ip_address_instance.to_dict()
# create an instance of LogIpAddress from a dict
log_ip_address_from_dict = LogIpAddress.from_dict(log_ip_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


