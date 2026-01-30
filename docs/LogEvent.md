# LogEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor** | [**LogActor**](LogActor.md) |  | [optional] 
**authentication_context** | [**LogAuthenticationContext**](LogAuthenticationContext.md) |  | [optional] 
**client** | [**LogClient**](LogClient.md) |  | [optional] 
**debug_context** | [**LogDebugContext**](LogDebugContext.md) |  | [optional] 
**display_message** | **str** | The display message for an event | [optional] [readonly] 
**event_type** | **str** | The published event type. Event instances are categorized by action in the event type attribute. This attribute is key to navigating the System Log through expression filters. See [Event Types catalog](https://developer.okta.com/docs/reference/api/event-types/#catalog) for a complete list of System Log event types. | [optional] [readonly] 
**legacy_event_type** | **str** | Associated Events API Action &#x60;objectType&#x60; attribute value | [optional] [readonly] 
**outcome** | [**LogOutcome**](LogOutcome.md) |  | [optional] 
**published** | **datetime** | Timestamp when the event is published | [optional] [readonly] 
**request** | [**LogRequest**](LogRequest.md) |  | [optional] 
**security_context** | [**LogSecurityContext**](LogSecurityContext.md) |  | [optional] 
**severity** | [**LogSeverity**](LogSeverity.md) |  | [optional] 
**target** | [**List[LogTarget]**](LogTarget.md) | The entity that an actor performs an action on. Targets can be anything, such as an app user, a sign-in token, or anything else.  &gt; **Note:** When searching the target array, search for a given &#x60;type&#x60; rather than the array location. Target types, such as &#x60;User&#x60; and &#x60;AppInstance&#x60;, for a given &#x60;eventType&#x60; are not always in the same array location. | [optional] [readonly] 
**transaction** | [**LogTransaction**](LogTransaction.md) |  | [optional] 
**uuid** | **str** | Unique identifier for an individual event | [optional] [readonly] 
**version** | **str** | Versioning indicator | [optional] [readonly] 

## Example

```python
from okta.models.log_event import LogEvent

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


