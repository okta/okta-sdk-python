# LogClient

When an event is triggered by an HTTP request, the `client` object describes the [client](https://datatracker.ietf.org/doc/html/rfc2616) that issues the HTTP request. For instance, the web browser is the client when a user accesses Okta. When this request is received and processed, a sign-in event is fired. When the event isn't sourced to an HTTP request, such as an automatic update, the `client` object field is blank.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | Type of device that the client operates from (for example, computer) | [optional] [readonly] 
**geographical_context** | [**LogGeographicalContext**](LogGeographicalContext.md) |  | [optional] 
**id** | **str** | For OAuth requests, this is the ID of the OAuth [client](https://datatracker.ietf.org/doc/html/rfc6749#section-1.1) making the request. For SSWS token requests, this is the ID of the agent making the request. | [optional] [readonly] 
**ip_address** | **str** | IP address that the client is making its request from | [optional] [readonly] 
**user_agent** | [**LogUserAgent**](LogUserAgent.md) |  | [optional] 
**zone** | **str** | The &#x60;name&#x60; of the [Zone](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/NetworkZone/#tag/NetworkZone/operation/getNetworkZone) that the client&#39;s location is mapped to | [optional] [readonly] 

## Example

```python
from okta.models.log_client import LogClient

# TODO update the JSON string below
json = "{}"
# create an instance of LogClient from a JSON string
log_client_instance = LogClient.from_json(json)
# print the JSON string representation of the object
print(LogClient.to_json())

# convert the object into a dict
log_client_dict = log_client_instance.to_dict()
# create an instance of LogClient from a dict
log_client_from_dict = LogClient.from_dict(log_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


