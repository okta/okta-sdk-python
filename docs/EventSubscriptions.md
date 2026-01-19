# EventSubscriptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**EventHookFilters**](EventHookFilters.md) |  | [optional] 
**items** | **List[str]** | The subscribed event types that trigger the event hook. When you register an event hook you need to specify which events you want to subscribe to. To see the list of event types currently eligible for use in event hooks, use the [Event Types catalog](https://developer.okta.com/docs/reference/api/event-types/#catalog) and search with the parameter &#x60;event-hook-eligible&#x60;. | 
**type** | [**EventSubscriptionType**](EventSubscriptionType.md) |  | 

## Example

```python
from okta.models.event_subscriptions import EventSubscriptions

# TODO update the JSON string below
json = "{}"
# create an instance of EventSubscriptions from a JSON string
event_subscriptions_instance = EventSubscriptions.from_json(json)
# print the JSON string representation of the object
print(EventSubscriptions.to_json())

# convert the object into a dict
event_subscriptions_dict = event_subscriptions_instance.to_dict()
# create an instance of EventSubscriptions from a dict
event_subscriptions_from_dict = EventSubscriptions.from_dict(event_subscriptions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


