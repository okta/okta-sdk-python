# SecurityEventsProviderResponse

The Security Events Provider response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of this instance | [optional] [readonly] 
**name** | **str** | The name of the Security Events Provider instance | [optional] 
**settings** | [**SecurityEventsProviderSettingsResponse**](SecurityEventsProviderSettingsResponse.md) |  | [optional] 
**status** | **str** | Indicates whether the Security Events Provider is active or not | [optional] [readonly] 
**type** | **str** | The application type of the Security Events Provider | [optional] 
**links** | [**LinksSelfAndLifecycle**](LinksSelfAndLifecycle.md) |  | [optional] 

## Example

```python
from okta.models.security_events_provider_response import SecurityEventsProviderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityEventsProviderResponse from a JSON string
security_events_provider_response_instance = SecurityEventsProviderResponse.from_json(json)
# print the JSON string representation of the object
print(SecurityEventsProviderResponse.to_json())

# convert the object into a dict
security_events_provider_response_dict = security_events_provider_response_instance.to_dict()
# create an instance of SecurityEventsProviderResponse from a dict
security_events_provider_response_from_dict = SecurityEventsProviderResponse.from_dict(security_events_provider_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


