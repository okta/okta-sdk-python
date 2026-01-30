# CaepSessionRevokedEvent

The session of the subject was revoked

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_ip** | **str** | Current IP of the session | [optional] 
**current_user_agent** | **str** | Current User Agent of the session | [optional] 
**event_timestamp** | **int** | The time of the event (UNIX timestamp) | 
**initiating_entity** | **str** | The entity that initiated the event | [optional] 
**last_known_ip** | **str** | Last known IP of the session | [optional] 
**last_known_user_agent** | **str** | Last known User Agent of the session | [optional] 
**reason_admin** | [**CaepDeviceComplianceChangeEventReasonAdmin**](CaepDeviceComplianceChangeEventReasonAdmin.md) |  | [optional] 
**reason_user** | [**CaepDeviceComplianceChangeEventReasonUser**](CaepDeviceComplianceChangeEventReasonUser.md) |  | [optional] 
**subject** | [**SecurityEventSubject**](SecurityEventSubject.md) |  | 

## Example

```python
from okta.models.caep_session_revoked_event import CaepSessionRevokedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CaepSessionRevokedEvent from a JSON string
caep_session_revoked_event_instance = CaepSessionRevokedEvent.from_json(json)
# print the JSON string representation of the object
print(CaepSessionRevokedEvent.to_json())

# convert the object into a dict
caep_session_revoked_event_dict = caep_session_revoked_event_instance.to_dict()
# create an instance of CaepSessionRevokedEvent from a dict
caep_session_revoked_event_from_dict = CaepSessionRevokedEvent.from_dict(caep_session_revoked_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


