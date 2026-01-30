# SloParticipate

Determines if the app participates in Single Logout (SLO)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binding_type** | **str** | Request binding type | [optional] 
**enabled** | **bool** | Indicates whether the app is allowed to participate in front-channel SLO | [optional] 
**logout_request_url** | **str** | URL where Okta sends the logout request | [optional] 
**session_index_required** | **bool** | Determines whether Okta sends the &#x60;SessionIndex&#x60; elements in the logout request | [optional] 

## Example

```python
from okta.models.slo_participate import SloParticipate

# TODO update the JSON string below
json = "{}"
# create an instance of SloParticipate from a JSON string
slo_participate_instance = SloParticipate.from_json(json)
# print the JSON string representation of the object
print(SloParticipate.to_json())

# convert the object into a dict
slo_participate_dict = slo_participate_instance.to_dict()
# create an instance of SloParticipate from a dict
slo_participate_from_dict = SloParticipate.from_dict(slo_participate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


