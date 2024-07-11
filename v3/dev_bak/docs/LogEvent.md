# LogEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor** | [**LogActor**](LogActor.md) |  | [optional] 
**authentication_context** | [**LogAuthenticationContext**](LogAuthenticationContext.md) |  | [optional] 
**client** | [**LogClient**](LogClient.md) |  | [optional] 
**debug_context** | [**LogDebugContext**](LogDebugContext.md) |  | [optional] 
**display_message** | **str** |  | [optional] [readonly] 
**event_type** | **str** |  | [optional] [readonly] 
**legacy_event_type** | **str** |  | [optional] [readonly] 
**outcome** | [**LogOutcome**](LogOutcome.md) |  | [optional] 
**published** | **datetime** |  | [optional] [readonly] 
**request** | [**LogRequest**](LogRequest.md) |  | [optional] 
**security_context** | [**LogSecurityContext**](LogSecurityContext.md) |  | [optional] 
**severity** | [**LogSeverity**](LogSeverity.md) |  | [optional] 
**target** | [**List[LogTarget]**](LogTarget.md) |  | [optional] [readonly] 
**transaction** | [**LogTransaction**](LogTransaction.md) |  | [optional] 
**uuid** | **str** |  | [optional] [readonly] 
**version** | **str** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.log_event import LogEvent

# TODO update the JSON string below
json = "{}"
# create an instance of LogEvent from a JSON string
log_event_instance = LogEvent.from_json(json)
# print the JSON string representation of the object
print(LogEvent.to_json())

# convert the object into a dict
log_event_dict = log_event_instance.to_dict()
# create an instance of LogEvent from a dict
log_event_from_dict = LogEvent.from_dict(log_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


