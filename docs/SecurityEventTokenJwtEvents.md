# SecurityEventTokenJwtEvents

A non-empty set of events. Expected size is 1 for each SET

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**https__schemas_openid_net_secevent_caep_event_type_credential_change** | [**CaepCredentialChangeEvent**](CaepCredentialChangeEvent.md) |  | [optional] 
**https__schemas_openid_net_secevent_caep_event_type_session_revoked** | [**SsfTransmitterCaepSessionRevokedEvent**](SsfTransmitterCaepSessionRevokedEvent.md) |  | [optional] 

## Example

```python
from okta.models.security_event_token_jwt_events import SecurityEventTokenJwtEvents

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityEventTokenJwtEvents from a JSON string
security_event_token_jwt_events_instance = SecurityEventTokenJwtEvents.from_json(json)
# print the JSON string representation of the object
print(SecurityEventTokenJwtEvents.to_json())

# convert the object into a dict
security_event_token_jwt_events_dict = security_event_token_jwt_events_instance.to_dict()
# create an instance of SecurityEventTokenJwtEvents from a dict
security_event_token_jwt_events_from_dict = SecurityEventTokenJwtEvents.from_dict(security_event_token_jwt_events_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


