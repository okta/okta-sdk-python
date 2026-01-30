# SecurityEventTokenRequestJwtEvents

A non-empty collection of events

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**https__schemas_okta_com_secevent_okta_event_type_device_risk_change** | [**OktaDeviceRiskChangeEvent**](OktaDeviceRiskChangeEvent.md) |  | [optional] 
**https__schemas_okta_com_secevent_okta_event_type_ip_change** | [**OktaIpChangeEvent**](OktaIpChangeEvent.md) |  | [optional] 
**https__schemas_okta_com_secevent_okta_event_type_user_risk_change** | [**OktaUserRiskChangeEvent**](OktaUserRiskChangeEvent.md) |  | [optional] 
**https__schemas_openid_net_secevent_caep_event_type_device_compliance_change** | [**CaepDeviceComplianceChangeEvent**](CaepDeviceComplianceChangeEvent.md) |  | [optional] 
**https__schemas_openid_net_secevent_caep_event_type_session_revoked** | [**CaepSessionRevokedEvent**](CaepSessionRevokedEvent.md) |  | [optional] 
**https__schemas_openid_net_secevent_risc_event_type_identifier_changed** | [**RiscIdentifierChangedEvent**](RiscIdentifierChangedEvent.md) |  | [optional] 

## Example

```python
from okta.models.security_event_token_request_jwt_events import SecurityEventTokenRequestJwtEvents

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityEventTokenRequestJwtEvents from a JSON string
security_event_token_request_jwt_events_instance = SecurityEventTokenRequestJwtEvents.from_json(json)
# print the JSON string representation of the object
print(SecurityEventTokenRequestJwtEvents.to_json())

# convert the object into a dict
security_event_token_request_jwt_events_dict = security_event_token_request_jwt_events_instance.to_dict()
# create an instance of SecurityEventTokenRequestJwtEvents from a dict
security_event_token_request_jwt_events_from_dict = SecurityEventTokenRequestJwtEvents.from_dict(security_event_token_request_jwt_events_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


