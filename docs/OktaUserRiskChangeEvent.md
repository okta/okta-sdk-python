# OktaUserRiskChangeEvent

The user risk level changed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_level** | **str** | Current risk level of the user | 
**event_timestamp** | **int** | The time of the event (UNIX timestamp) | 
**initiating_entity** | **str** | The entity that initiated the event | [optional] 
**previous_level** | **str** | Previous risk level of the user | 
**reason_admin** | [**CaepDeviceComplianceChangeEventReasonAdmin**](CaepDeviceComplianceChangeEventReasonAdmin.md) |  | [optional] 
**reason_user** | [**CaepDeviceComplianceChangeEventReasonUser**](CaepDeviceComplianceChangeEventReasonUser.md) |  | [optional] 
**subject** | [**SecurityEventSubject**](SecurityEventSubject.md) |  | 

## Example

```python
from okta.models.okta_user_risk_change_event import OktaUserRiskChangeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of OktaUserRiskChangeEvent from a JSON string
okta_user_risk_change_event_instance = OktaUserRiskChangeEvent.from_json(json)
# print the JSON string representation of the object
print(OktaUserRiskChangeEvent.to_json())

# convert the object into a dict
okta_user_risk_change_event_dict = okta_user_risk_change_event_instance.to_dict()
# create an instance of OktaUserRiskChangeEvent from a dict
okta_user_risk_change_event_from_dict = OktaUserRiskChangeEvent.from_dict(okta_user_risk_change_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


