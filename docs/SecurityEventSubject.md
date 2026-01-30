# SecurityEventSubject

The event subjects

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **object** | The device involved with the event | [optional] 
**user** | **object** | The user involved with the event | [optional] 

## Example

```python
from okta.models.security_event_subject import SecurityEventSubject

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityEventSubject from a JSON string
security_event_subject_instance = SecurityEventSubject.from_json(json)
# print the JSON string representation of the object
print(SecurityEventSubject.to_json())

# convert the object into a dict
security_event_subject_dict = security_event_subject_instance.to_dict()
# create an instance of SecurityEventSubject from a dict
security_event_subject_from_dict = SecurityEventSubject.from_dict(security_event_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


