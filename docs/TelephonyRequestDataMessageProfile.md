# TelephonyRequestDataMessageProfile

Message profile specifies information about the telephony (sms/voice) message to be sent to the Okta user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**msg_template** | **str** | Default or Okta org configured sms or voice message template | [optional] 
**phone_number** | **str** | The Okta&#39;s user&#39;s phone number | [optional] 
**otp_expires** | **str** | The time when OTP expires | [optional] 
**delivery_channel** | **str** | The channel for OTP delivery - SMS or voice | [optional] 
**otp_code** | **str** | The OTP code requested by the Okta user | [optional] 
**locale** | **str** | The locale associated with the Okta user | [optional] 

## Example

```python
from okta.models.telephony_request_data_message_profile import TelephonyRequestDataMessageProfile

# TODO update the JSON string below
json = "{}"
# create an instance of TelephonyRequestDataMessageProfile from a JSON string
telephony_request_data_message_profile_instance = TelephonyRequestDataMessageProfile.from_json(json)
# print the JSON string representation of the object
print(TelephonyRequestDataMessageProfile.to_json())

# convert the object into a dict
telephony_request_data_message_profile_dict = telephony_request_data_message_profile_instance.to_dict()
# create an instance of TelephonyRequestDataMessageProfile from a dict
telephony_request_data_message_profile_from_dict = TelephonyRequestDataMessageProfile.from_dict(telephony_request_data_message_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


