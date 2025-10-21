# LogRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_chain** | [**List[LogIpAddress]**](LogIpAddress.md) |  | [optional] [readonly] 

## Example

```python
from okta.models.log_request import LogRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LogRequest from a JSON string
log_request_instance = LogRequest.from_json(json)
# print the JSON string representation of the object
print(LogRequest.to_json())

# convert the object into a dict
log_request_dict = log_request_instance.to_dict()
# create an instance of LogRequest from a dict
log_request_from_dict = LogRequest.from_dict(log_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


