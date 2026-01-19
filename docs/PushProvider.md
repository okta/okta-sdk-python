# PushProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique key for the Push Provider | [optional] [readonly] 
**last_updated_date** | **str** | Timestamp when the Push Provider was last modified | [optional] [readonly] 
**name** | **str** | Display name of the push provider | [optional] 
**provider_type** | [**ProviderType**](ProviderType.md) |  | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.push_provider import PushProvider

# TODO update the JSON string below
json = "{}"
# create an instance of PushProvider from a JSON string
push_provider_instance = PushProvider.from_json(json)
# print the JSON string representation of the object
print(PushProvider.to_json())

# convert the object into a dict
push_provider_dict = push_provider_instance.to_dict()
# create an instance of PushProvider from a dict
push_provider_from_dict = PushProvider.from_dict(push_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


