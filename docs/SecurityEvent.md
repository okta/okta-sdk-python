# SecurityEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_timestamp** | **int** | The time of the event (UNIX timestamp) | 
**subject** | [**SecurityEventSubject**](SecurityEventSubject.md) |  | 

## Example

```python
from okta.models.security_event import SecurityEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityEvent from a JSON string
security_event_instance = SecurityEvent.from_json(json)
# print the JSON string representation of the object
print(SecurityEvent.to_json())

# convert the object into a dict
security_event_dict = security_event_instance.to_dict()
# create an instance of SecurityEvent from a dict
security_event_from_dict = SecurityEvent.from_dict(security_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


