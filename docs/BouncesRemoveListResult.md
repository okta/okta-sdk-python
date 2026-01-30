# BouncesRemoveListResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[BouncesRemoveListError]**](BouncesRemoveListError.md) | A list of emails that wasn&#39;t added to the email-bounced remove list and the error reason | [optional] 

## Example

```python
from okta.models.bounces_remove_list_result import BouncesRemoveListResult

# TODO update the JSON string below
json = "{}"
# create an instance of BouncesRemoveListResult from a JSON string
bounces_remove_list_result_instance = BouncesRemoveListResult.from_json(json)
# print the JSON string representation of the object
print(BouncesRemoveListResult.to_json())

# convert the object into a dict
bounces_remove_list_result_dict = bounces_remove_list_result_instance.to_dict()
# create an instance of BouncesRemoveListResult from a dict
bounces_remove_list_result_from_dict = BouncesRemoveListResult.from_dict(bounces_remove_list_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


