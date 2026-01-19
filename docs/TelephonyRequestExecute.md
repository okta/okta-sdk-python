# TelephonyRequestExecute

Telephony inline hook request body

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_event_version** | **str** | The inline hook cloud version | [optional] 
**content_type** | **str** | The inline hook request header content | [optional] 
**event_id** | **str** | The individual inline hook request ID | [optional] 
**event_time** | **str** | The time the inline hook request was sent | [optional] 
**event_type_version** | **str** | The inline hook version | [optional] 
**data** | [**TelephonyRequestData**](TelephonyRequestData.md) |  | [optional] 
**event_type** | **str** | The type of inline hook. The telephony inline hook type is &#x60;com.okta.telephony.provider&#x60;. | [optional] 
**request_type** | **str** | The type of inline hook request. For example, &#x60;com.okta.user.telephony.pre-enrollment&#x60;. | [optional] 
**source** | **str** | The ID and URL of the telephony inline hook | [optional] 

## Example

```python
from okta.models.telephony_request_execute import TelephonyRequestExecute

# TODO update the JSON string below
json = "{}"
# create an instance of TelephonyRequestExecute from a JSON string
telephony_request_execute_instance = TelephonyRequestExecute.from_json(json)
# print the JSON string representation of the object
print(TelephonyRequestExecute.to_json())

# convert the object into a dict
telephony_request_execute_dict = telephony_request_execute_instance.to_dict()
# create an instance of TelephonyRequestExecute from a dict
telephony_request_execute_from_dict = TelephonyRequestExecute.from_dict(telephony_request_execute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


