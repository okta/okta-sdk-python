# APNSPushProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**APNSConfiguration**](APNSConfiguration.md) |  | [optional] 

## Example

```python
from openapi_client.models.apns_push_provider import APNSPushProvider

# TODO update the JSON string below
json = "{}"
# create an instance of APNSPushProvider from a JSON string
apns_push_provider_instance = APNSPushProvider.from_json(json)
# print the JSON string representation of the object
print(APNSPushProvider.to_json())

# convert the object into a dict
apns_push_provider_dict = apns_push_provider_instance.to_dict()
# create an instance of APNSPushProvider from a dict
apns_push_provider_form_dict = apns_push_provider.from_dict(apns_push_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


