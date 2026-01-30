# SsfTransmitterSecurityEventSubject

The event subject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | The format of the subject | [optional] 
**iss** | **str** | An identifier of the actor | [optional] 
**sub** | **str** | An identifier for the subject that was acted on | [optional] 

## Example

```python
from okta.models.ssf_transmitter_security_event_subject import SsfTransmitterSecurityEventSubject

# TODO update the JSON string below
json = "{}"
# create an instance of SsfTransmitterSecurityEventSubject from a JSON string
ssf_transmitter_security_event_subject_instance = SsfTransmitterSecurityEventSubject.from_json(json)
# print the JSON string representation of the object
print(SsfTransmitterSecurityEventSubject.to_json())

# convert the object into a dict
ssf_transmitter_security_event_subject_dict = ssf_transmitter_security_event_subject_instance.to_dict()
# create an instance of SsfTransmitterSecurityEventSubject from a dict
ssf_transmitter_security_event_subject_from_dict = SsfTransmitterSecurityEventSubject.from_dict(ssf_transmitter_security_event_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


