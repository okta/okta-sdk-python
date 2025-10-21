# FCMPushProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**FCMConfiguration**](FCMConfiguration.md) |  | [optional] 

## Example

```python
from okta.models.fcm_push_provider import FCMPushProvider

# TODO update the JSON string below
json = "{}"
# create an instance of FCMPushProvider from a JSON string
fcm_push_provider_instance = FCMPushProvider.from_json(json)
# print the JSON string representation of the object
print(FCMPushProvider.to_json())

# convert the object into a dict
fcm_push_provider_dict = fcm_push_provider_instance.to_dict()
# create an instance of FCMPushProvider from a dict
fcm_push_provider_from_dict = FCMPushProvider.from_dict(fcm_push_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


