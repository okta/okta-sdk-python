# SecurityEventReason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**en** | **str** | The event reason in English | 

## Example

```python
from okta.models.security_event_reason import SecurityEventReason

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityEventReason from a JSON string
security_event_reason_instance = SecurityEventReason.from_json(json)
# print the JSON string representation of the object
print(SecurityEventReason.to_json())

# convert the object into a dict
security_event_reason_dict = security_event_reason_instance.to_dict()
# create an instance of SecurityEventReason from a dict
security_event_reason_from_dict = SecurityEventReason.from_dict(security_event_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


