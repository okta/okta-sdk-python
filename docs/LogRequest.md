# LogRequest

The `Request` object describes details that are related to the HTTP request that triggers this event, if available. When the event isn't sourced to an HTTP request, such as an automatic update on the Okta servers, the `Request` object still exists, but the `ipChain` field is empty.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_chain** | [**List[LogIpAddress]**](LogIpAddress.md) | If the incoming request passes through any proxies, the IP addresses of those proxies are stored here in the format of clientIp, proxy1, proxy2, and so on. This field is useful when working with trusted proxies. | [optional] [readonly] 

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


