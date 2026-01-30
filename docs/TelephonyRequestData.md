# TelephonyRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**RegistrationInlineHookSSRDataAllOfDataContext**](RegistrationInlineHookSSRDataAllOfDataContext.md) |  | [optional] 
**message_profile** | [**TelephonyRequestDataMessageProfile**](TelephonyRequestDataMessageProfile.md) |  | [optional] 
**user_profile** | [**TelephonyRequestDataUserProfile**](TelephonyRequestDataUserProfile.md) |  | [optional] 

## Example

```python
from okta.models.telephony_request_data import TelephonyRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of TelephonyRequestData from a JSON string
telephony_request_data_instance = TelephonyRequestData.from_json(json)
# print the JSON string representation of the object
print(TelephonyRequestData.to_json())

# convert the object into a dict
telephony_request_data_dict = telephony_request_data_instance.to_dict()
# create an instance of TelephonyRequestData from a dict
telephony_request_data_from_dict = TelephonyRequestData.from_dict(telephony_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


