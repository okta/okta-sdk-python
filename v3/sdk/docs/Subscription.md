# Subscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channels** | **List[str]** | An array of sources send notifications to users. &gt; **Note**: Currently, Okta only allows &#x60;email&#x60; channels. | [optional] 
**notification_type** | [**NotificationType**](NotificationType.md) |  | [optional] 
**status** | [**SubscriptionStatus**](SubscriptionStatus.md) |  | [optional] 
**links** | [**SubscriptionLinks**](SubscriptionLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.subscription import Subscription

# TODO update the JSON string below
json = "{}"
# create an instance of Subscription from a JSON string
subscription_instance = Subscription.from_json(json)
# print the JSON string representation of the object
print(Subscription.to_json())

# convert the object into a dict
subscription_dict = subscription_instance.to_dict()
# create an instance of Subscription from a dict
subscription_form_dict = subscription.from_dict(subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


