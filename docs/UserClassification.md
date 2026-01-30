# UserClassification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_updated** | **datetime** | The timestamp when the user classification was last updated | [optional] [readonly] 
**type** | [**ClassificationType**](ClassificationType.md) |  | [optional] 

## Example

```python
from okta.models.user_classification import UserClassification

# TODO update the JSON string below
json = "{}"
# create an instance of UserClassification from a JSON string
user_classification_instance = UserClassification.from_json(json)
# print the JSON string representation of the object
print(UserClassification.to_json())

# convert the object into a dict
user_classification_dict = user_classification_instance.to_dict()
# create an instance of UserClassification from a dict
user_classification_from_dict = UserClassification.from_dict(user_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


