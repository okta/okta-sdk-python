# TelephonyResponseCommandsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The location where you specify the command. For the telephony inline hook, there&#39;s only one command, &#x60;com.okta.telephony.action&#x60;. | [optional] 
**value** | [**List[TelephonyResponseCommandsInnerValueInner]**](TelephonyResponseCommandsInnerValueInner.md) | The status of the telephony operation along with optional additional information about the provider, transaction ID and any other transaction metadata. | [optional] 

## Example

```python
from okta.models.telephony_response_commands_inner import TelephonyResponseCommandsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TelephonyResponseCommandsInner from a JSON string
telephony_response_commands_inner_instance = TelephonyResponseCommandsInner.from_json(json)
# print the JSON string representation of the object
print(TelephonyResponseCommandsInner.to_json())

# convert the object into a dict
telephony_response_commands_inner_dict = telephony_response_commands_inner_instance.to_dict()
# create an instance of TelephonyResponseCommandsInner from a dict
telephony_response_commands_inner_from_dict = TelephonyResponseCommandsInner.from_dict(telephony_response_commands_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


