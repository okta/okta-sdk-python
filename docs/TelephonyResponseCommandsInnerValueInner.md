# TelephonyResponseCommandsInnerValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of telephony callout | [optional] 
**provider** | **str** | Telephony provider for sms/voice | [optional] 
**transaction_id** | **str** | Transaction ID for sms/voice | [optional] 
**transaction_metadata** | **str** | Any relevant metadata for the telephony transaction | [optional] 

## Example

```python
from okta.models.telephony_response_commands_inner_value_inner import TelephonyResponseCommandsInnerValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of TelephonyResponseCommandsInnerValueInner from a JSON string
telephony_response_commands_inner_value_inner_instance = TelephonyResponseCommandsInnerValueInner.from_json(json)
# print the JSON string representation of the object
print(TelephonyResponseCommandsInnerValueInner.to_json())

# convert the object into a dict
telephony_response_commands_inner_value_inner_dict = telephony_response_commands_inner_value_inner_instance.to_dict()
# create an instance of TelephonyResponseCommandsInnerValueInner from a dict
telephony_response_commands_inner_value_inner_from_dict = TelephonyResponseCommandsInnerValueInner.from_dict(telephony_response_commands_inner_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


