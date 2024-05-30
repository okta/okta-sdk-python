# EventSubscriptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[str]** |  | [optional] 
**type** | [**EventSubscriptionType**](EventSubscriptionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.event_subscriptions import EventSubscriptions

# TODO update the JSON string below
json = "{}"
# create an instance of EventSubscriptions from a JSON string
event_subscriptions_instance = EventSubscriptions.from_json(json)
# print the JSON string representation of the object
print(EventSubscriptions.to_json())

# convert the object into a dict
event_subscriptions_dict = event_subscriptions_instance.to_dict()
# create an instance of EventSubscriptions from a dict
event_subscriptions_form_dict = event_subscriptions.from_dict(event_subscriptions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


