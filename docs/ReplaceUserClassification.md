# ReplaceUserClassification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ClassificationType**](ClassificationType.md) |  | [optional] 

## Example

```python
from okta.models.replace_user_classification import ReplaceUserClassification

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceUserClassification from a JSON string
replace_user_classification_instance = ReplaceUserClassification.from_json(json)
# print the JSON string representation of the object
print(ReplaceUserClassification.to_json())

# convert the object into a dict
replace_user_classification_dict = replace_user_classification_instance.to_dict()
# create an instance of ReplaceUserClassification from a dict
replace_user_classification_from_dict = ReplaceUserClassification.from_dict(replace_user_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


