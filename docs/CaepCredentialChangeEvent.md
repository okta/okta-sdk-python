# CaepCredentialChangeEvent

The credential was created, changed, revoked or deleted

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_type** | **str** | The type of action done towards the credential | 
**credential_type** | **str** | The credential type of the changed credential. It will one of the supported enum values or any other credential type supported mutually by the Transmitter and the Receiver. | 
**event_timestamp** | **int** | The time of the event (UNIX timestamp) | [optional] 
**fido2_aaguid** | **str** | FIDO2 Authenticator Attestation GUID | [optional] 
**friendly_name** | **str** | Credential friendly name | [optional] 
**initiating_entity** | **str** | The entity that initiated the event | [optional] 
**reason_admin** | [**CaepCredentialChangeEventReasonAdmin**](CaepCredentialChangeEventReasonAdmin.md) |  | [optional] 
**reason_user** | [**CaepCredentialChangeEventReasonUser**](CaepCredentialChangeEventReasonUser.md) |  | [optional] 
**subject** | [**SsfTransmitterSecurityEventSubject**](SsfTransmitterSecurityEventSubject.md) |  | [optional] 

## Example

```python
from okta.models.caep_credential_change_event import CaepCredentialChangeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CaepCredentialChangeEvent from a JSON string
caep_credential_change_event_instance = CaepCredentialChangeEvent.from_json(json)
# print the JSON string representation of the object
print(CaepCredentialChangeEvent.to_json())

# convert the object into a dict
caep_credential_change_event_dict = caep_credential_change_event_instance.to_dict()
# create an instance of CaepCredentialChangeEvent from a dict
caep_credential_change_event_from_dict = CaepCredentialChangeEvent.from_dict(caep_credential_change_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


