# CaepEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_timestamp** | **int** | The time of the event (UNIX timestamp) | [optional] 
**reason_admin** | [**CaepCredentialChangeEventReasonAdmin**](CaepCredentialChangeEventReasonAdmin.md) |  | [optional] 
**reason_user** | [**CaepCredentialChangeEventReasonUser**](CaepCredentialChangeEventReasonUser.md) |  | [optional] 
**subject** | [**SsfTransmitterSecurityEventSubject**](SsfTransmitterSecurityEventSubject.md) |  | [optional] 

## Example

```python
from okta.models.caep_event import CaepEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CaepEvent from a JSON string
caep_event_instance = CaepEvent.from_json(json)
# print the JSON string representation of the object
print(CaepEvent.to_json())

# convert the object into a dict
caep_event_dict = caep_event_instance.to_dict()
# create an instance of CaepEvent from a dict
caep_event_from_dict = CaepEvent.from_dict(caep_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


