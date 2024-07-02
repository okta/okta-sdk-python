# LogClient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** |  | [optional] [readonly] 
**geographical_context** | [**LogGeographicalContext**](LogGeographicalContext.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**ip_address** | **str** |  | [optional] [readonly] 
**user_agent** | [**LogUserAgent**](LogUserAgent.md) |  | [optional] 
**zone** | **str** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.log_client import LogClient

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


