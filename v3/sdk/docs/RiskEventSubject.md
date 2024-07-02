# RiskEventSubject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | The risk event subject IP address (either an IPv4 or IPv6 address) | 
**message** | **str** | Additional reasons for the risk level of the IP | [optional] 
**risk_level** | [**RiskEventSubjectRiskLevel**](RiskEventSubjectRiskLevel.md) |  | 

## Example

```python
from openapi_client.models.risk_event_subject import RiskEventSubject

# TODO update the JSON string below
json = "{}"
# create an instance of RiskEventSubject from a JSON string
risk_event_subject_instance = RiskEventSubject.from_json(json)
# print the JSON string representation of the object
print(RiskEventSubject.to_json())

# convert the object into a dict
risk_event_subject_dict = risk_event_subject_instance.to_dict()
# create an instance of RiskEventSubject from a dict
risk_event_subject_from_dict = RiskEventSubject.from_dict(risk_event_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


