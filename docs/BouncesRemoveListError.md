# BouncesRemoveListError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_address** | **str** | An email address with a validation error | [optional] 
**reason** | **str** | Validation error reason | [optional] 

## Example

```python
from okta.models.bounces_remove_list_error import BouncesRemoveListError

# TODO update the JSON string below
json = "{}"
# create an instance of BouncesRemoveListError from a JSON string
bounces_remove_list_error_instance = BouncesRemoveListError.from_json(json)
# print the JSON string representation of the object
print(BouncesRemoveListError.to_json())

# convert the object into a dict
bounces_remove_list_error_dict = bounces_remove_list_error_instance.to_dict()
# create an instance of BouncesRemoveListError from a dict
bounces_remove_list_error_from_dict = BouncesRemoveListError.from_dict(bounces_remove_list_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


