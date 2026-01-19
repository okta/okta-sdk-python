# SsfTransmitterCaepSessionRevokedEvent

The session of the subject was revoked

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_timestamp** | **int** | The time of the event (UNIX timestamp) | [optional] 
**reason_admin** | [**CaepCredentialChangeEventReasonAdmin**](CaepCredentialChangeEventReasonAdmin.md) |  | [optional] 
**reason_user** | [**CaepCredentialChangeEventReasonUser**](CaepCredentialChangeEventReasonUser.md) |  | [optional] 
**subject** | [**SsfTransmitterSecurityEventSubject**](SsfTransmitterSecurityEventSubject.md) |  | [optional] 

## Example

```python
from okta.models.ssf_transmitter_caep_session_revoked_event import SsfTransmitterCaepSessionRevokedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SsfTransmitterCaepSessionRevokedEvent from a JSON string
ssf_transmitter_caep_session_revoked_event_instance = SsfTransmitterCaepSessionRevokedEvent.from_json(json)
# print the JSON string representation of the object
print(SsfTransmitterCaepSessionRevokedEvent.to_json())

# convert the object into a dict
ssf_transmitter_caep_session_revoked_event_dict = ssf_transmitter_caep_session_revoked_event_instance.to_dict()
# create an instance of SsfTransmitterCaepSessionRevokedEvent from a dict
ssf_transmitter_caep_session_revoked_event_from_dict = SsfTransmitterCaepSessionRevokedEvent.from_dict(ssf_transmitter_caep_session_revoked_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


