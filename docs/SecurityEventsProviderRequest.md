# SecurityEventsProviderRequest

The request schema for creating or updating a Security Events Provider. The `settings` must match one of the schemas.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Security Events Provider instance | 
**settings** | [**SecurityEventsProviderRequestSettings**](SecurityEventsProviderRequestSettings.md) |  | 
**type** | **str** | The application type of the Security Events Provider | 

## Example

```python
from okta.models.security_events_provider_request import SecurityEventsProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityEventsProviderRequest from a JSON string
security_events_provider_request_instance = SecurityEventsProviderRequest.from_json(json)
# print the JSON string representation of the object
print(SecurityEventsProviderRequest.to_json())

# convert the object into a dict
security_events_provider_request_dict = security_events_provider_request_instance.to_dict()
# create an instance of SecurityEventsProviderRequest from a dict
security_events_provider_request_from_dict = SecurityEventsProviderRequest.from_dict(security_events_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


