# RiscIdentifierChangedEvent

The subject's identifier has changed, which is either an email address or a phone number change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_timestamp** | **int** | The time of the event (UNIX timestamp) | 
**new_value** | **str** | The new identifier value | [optional] 
**subject** | [**SecurityEventSubject**](SecurityEventSubject.md) |  | 

## Example

```python
from okta.models.risc_identifier_changed_event import RiscIdentifierChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of RiscIdentifierChangedEvent from a JSON string
risc_identifier_changed_event_instance = RiscIdentifierChangedEvent.from_json(json)
# print the JSON string representation of the object
print(RiscIdentifierChangedEvent.to_json())

# convert the object into a dict
risc_identifier_changed_event_dict = risc_identifier_changed_event_instance.to_dict()
# create an instance of RiscIdentifierChangedEvent from a dict
risc_identifier_changed_event_from_dict = RiscIdentifierChangedEvent.from_dict(risc_identifier_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


