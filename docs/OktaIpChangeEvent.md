# OktaIpChangeEvent

IP changed for the subject's session

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_ip_address** | **str** | Current IP address of the subject | 
**event_timestamp** | **int** | The time of the event (UNIX timestamp) | 
**initiating_entity** | **str** | The entity that initiated the event | [optional] 
**previous_ip_address** | **str** | Previous IP address of the subject | 
**reason_admin** | [**CaepDeviceComplianceChangeEventReasonAdmin**](CaepDeviceComplianceChangeEventReasonAdmin.md) |  | [optional] 
**reason_user** | [**CaepDeviceComplianceChangeEventReasonUser**](CaepDeviceComplianceChangeEventReasonUser.md) |  | [optional] 
**subject** | [**SecurityEventSubject**](SecurityEventSubject.md) |  | 

## Example

```python
from okta.models.okta_ip_change_event import OktaIpChangeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of OktaIpChangeEvent from a JSON string
okta_ip_change_event_instance = OktaIpChangeEvent.from_json(json)
# print the JSON string representation of the object
print(OktaIpChangeEvent.to_json())

# convert the object into a dict
okta_ip_change_event_dict = okta_ip_change_event_instance.to_dict()
# create an instance of OktaIpChangeEvent from a dict
okta_ip_change_event_from_dict = OktaIpChangeEvent.from_dict(okta_ip_change_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


