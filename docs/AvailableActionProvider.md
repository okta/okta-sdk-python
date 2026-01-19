# AvailableActionProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_name** | **str** | The name of the action flow | 
**external_id** | **str** | The unique identifier of the action flow in the provider system | 
**type** | [**ActionProviderPayloadType**](ActionProviderPayloadType.md) |  | 
**url** | **str** | The URL to the action flow | 

## Example

```python
from okta.models.available_action_provider import AvailableActionProvider

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableActionProvider from a JSON string
available_action_provider_instance = AvailableActionProvider.from_json(json)
# print the JSON string representation of the object
print(AvailableActionProvider.to_json())

# convert the object into a dict
available_action_provider_dict = available_action_provider_instance.to_dict()
# create an instance of AvailableActionProvider from a dict
available_action_provider_from_dict = AvailableActionProvider.from_dict(available_action_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


