# TelephonyResponse

Telephony inline hook response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commands** | [**List[TelephonyResponseCommandsInner]**](TelephonyResponseCommandsInner.md) | The &#x60;commands&#x60; object specifies whether Okta accepts the end user&#39;s sign-in credentials as valid or not. For the telephony inline hook, you typically only return one &#x60;commands&#x60; object with one array element in it. | [optional] 

## Example

```python
from okta.models.telephony_response import TelephonyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TelephonyResponse from a JSON string
telephony_response_instance = TelephonyResponse.from_json(json)
# print the JSON string representation of the object
print(TelephonyResponse.to_json())

# convert the object into a dict
telephony_response_dict = telephony_response_instance.to_dict()
# create an instance of TelephonyResponse from a dict
telephony_response_from_dict = TelephonyResponse.from_dict(telephony_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


