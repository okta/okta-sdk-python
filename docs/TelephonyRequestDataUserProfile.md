# TelephonyRequestDataUserProfile

User profile specifies information about the Okta user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | The user&#39;s first name | [optional] 
**last_name** | **str** | The user&#39;s last name | [optional] 
**login** | **str** | The user&#39;s Okta login | [optional] 
**user_id** | **str** | The user&#39;s Okta user ID | [optional] 

## Example

```python
from okta.models.telephony_request_data_user_profile import TelephonyRequestDataUserProfile

# TODO update the JSON string below
json = "{}"
# create an instance of TelephonyRequestDataUserProfile from a JSON string
telephony_request_data_user_profile_instance = TelephonyRequestDataUserProfile.from_json(json)
# print the JSON string representation of the object
print(TelephonyRequestDataUserProfile.to_json())

# convert the object into a dict
telephony_request_data_user_profile_dict = telephony_request_data_user_profile_instance.to_dict()
# create an instance of TelephonyRequestDataUserProfile from a dict
telephony_request_data_user_profile_from_dict = TelephonyRequestDataUserProfile.from_dict(telephony_request_data_user_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


