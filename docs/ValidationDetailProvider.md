# ValidationDetailProvider

Action provider validation details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | The unique identifier of the action flow in the provider system | 
**type** | [**ActionProviderPayloadType**](ActionProviderPayloadType.md) |  | 

## Example

```python
from okta.models.validation_detail_provider import ValidationDetailProvider

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationDetailProvider from a JSON string
validation_detail_provider_instance = ValidationDetailProvider.from_json(json)
# print the JSON string representation of the object
print(ValidationDetailProvider.to_json())

# convert the object into a dict
validation_detail_provider_dict = validation_detail_provider_instance.to_dict()
# create an instance of ValidationDetailProvider from a dict
validation_detail_provider_from_dict = ValidationDetailProvider.from_dict(validation_detail_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


