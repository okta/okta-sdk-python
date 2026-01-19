# CaepSecurityEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_timestamp** | **int** | The time of the event (UNIX timestamp) | 
**initiating_entity** | **str** | The entity that initiated the event | [optional] 
**reason_admin** | [**CaepDeviceComplianceChangeEventReasonAdmin**](CaepDeviceComplianceChangeEventReasonAdmin.md) |  | [optional] 
**reason_user** | [**CaepDeviceComplianceChangeEventReasonUser**](CaepDeviceComplianceChangeEventReasonUser.md) |  | [optional] 
**subject** | [**SecurityEventSubject**](SecurityEventSubject.md) |  | 

## Example

```python
from okta.models.caep_security_event import CaepSecurityEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CaepSecurityEvent from a JSON string
caep_security_event_instance = CaepSecurityEvent.from_json(json)
# print the JSON string representation of the object
print(CaepSecurityEvent.to_json())

# convert the object into a dict
caep_security_event_dict = caep_security_event_instance.to_dict()
# create an instance of CaepSecurityEvent from a dict
caep_security_event_from_dict = CaepSecurityEvent.from_dict(caep_security_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


