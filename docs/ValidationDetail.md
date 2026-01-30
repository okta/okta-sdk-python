# ValidationDetail

Validation detail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Action identifier | 
**provider** | [**WorkflowsValidationDetailProvider**](WorkflowsValidationDetailProvider.md) |  | 

## Example

```python
from okta.models.validation_detail import ValidationDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationDetail from a JSON string
validation_detail_instance = ValidationDetail.from_json(json)
# print the JSON string representation of the object
print(ValidationDetail.to_json())

# convert the object into a dict
validation_detail_dict = validation_detail_instance.to_dict()
# create an instance of ValidationDetail from a dict
validation_detail_from_dict = ValidationDetail.from_dict(validation_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


