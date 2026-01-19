# CaepDeviceComplianceChangeEvent

The subject's device compliance was revoked

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_status** | **str** | Current device compliance status | 
**event_timestamp** | **int** | The time of the event (UNIX timestamp) | 
**initiating_entity** | **str** | The entity that initiated the event | [optional] 
**previous_status** | **str** | Previous device compliance status | 
**reason_admin** | [**CaepDeviceComplianceChangeEventReasonAdmin**](CaepDeviceComplianceChangeEventReasonAdmin.md) |  | [optional] 
**reason_user** | [**CaepDeviceComplianceChangeEventReasonUser**](CaepDeviceComplianceChangeEventReasonUser.md) |  | [optional] 
**subject** | [**SecurityEventSubject**](SecurityEventSubject.md) |  | 

## Example

```python
from okta.models.caep_device_compliance_change_event import CaepDeviceComplianceChangeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CaepDeviceComplianceChangeEvent from a JSON string
caep_device_compliance_change_event_instance = CaepDeviceComplianceChangeEvent.from_json(json)
# print the JSON string representation of the object
print(CaepDeviceComplianceChangeEvent.to_json())

# convert the object into a dict
caep_device_compliance_change_event_dict = caep_device_compliance_change_event_instance.to_dict()
# create an instance of CaepDeviceComplianceChangeEvent from a dict
caep_device_compliance_change_event_from_dict = CaepDeviceComplianceChangeEvent.from_dict(caep_device_compliance_change_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


