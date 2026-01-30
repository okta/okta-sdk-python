# ActionProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | The unique identifier of the action flow in the provider system | 
**type** | [**ActionProviderPayloadType**](ActionProviderPayloadType.md) |  | 
**url** | **str** | The URL to the action flow | 

## Example

```python
from okta.models.action_provider import ActionProvider

# TODO update the JSON string below
json = "{}"
# create an instance of ActionProvider from a JSON string
action_provider_instance = ActionProvider.from_json(json)
# print the JSON string representation of the object
print(ActionProvider.to_json())

# convert the object into a dict
action_provider_dict = action_provider_instance.to_dict()
# create an instance of ActionProvider from a dict
action_provider_from_dict = ActionProvider.from_dict(action_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


