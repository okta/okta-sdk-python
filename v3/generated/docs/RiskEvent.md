# RiskEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **datetime** | Timestamp at which the event expires (expressed as a UTC time zone using ISO 8601 format: yyyy-MM-dd&#x60;T&#x60;HH:mm:ss.SSS&#x60;Z&#x60;). If this optional field is not included, Okta automatically expires the event 24 hours after the event is consumed. | [optional] 
**subjects** | [**List[RiskEventSubject]**](RiskEventSubject.md) | List of Risk Event Subjects | 
**timestamp** | **datetime** | Timestamp of when the event is produced (expressed as a UTC time zone using ISO 8601 format: yyyy-MM-dd&#x60;T&#x60;HH:mm:ss.SSS&#x60;Z&#x60;) | [optional] 

## Example

```python
from openapi_client.models.risk_event import RiskEvent

# TODO update the JSON string below
json = "{}"
# create an instance of RiskEvent from a JSON string
risk_event_instance = RiskEvent.from_json(json)
# print the JSON string representation of the object
print(RiskEvent.to_json())

# convert the object into a dict
risk_event_dict = risk_event_instance.to_dict()
# create an instance of RiskEvent from a dict
risk_event_form_dict = risk_event.from_dict(risk_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


