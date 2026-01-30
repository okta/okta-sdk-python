# TelephonyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TelephonyRequestData**](TelephonyRequestData.md) |  | [optional] 
**event_type** | **str** | The type of inline hook. The telephony inline hook type is &#x60;com.okta.telephony.provider&#x60;. | [optional] 
**request_type** | **str** | The type of inline hook request. For example, &#x60;com.okta.user.telephony.pre-enrollment&#x60;. | [optional] 
**source** | **str** | The ID and URL of the telephony inline hook | [optional] 

## Example

```python
from okta.models.telephony_request import TelephonyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TelephonyRequest from a JSON string
telephony_request_instance = TelephonyRequest.from_json(json)
# print the JSON string representation of the object
print(TelephonyRequest.to_json())

# convert the object into a dict
telephony_request_dict = telephony_request_instance.to_dict()
# create an instance of TelephonyRequest from a dict
telephony_request_from_dict = TelephonyRequest.from_dict(telephony_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


