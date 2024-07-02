# IamRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the role was created | [optional] [readonly] 
**description** | **str** | Description of the role | 
**id** | **str** | Unique key for the role | [optional] [readonly] 
**label** | **str** | Unique label for the role | 
**last_updated** | **datetime** | Timestamp when the role was last updated | [optional] [readonly] 
**links** | [**IamRoleLinks**](IamRoleLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.iam_role import IamRole

# TODO update the JSON string below
json = "{}"
# create an instance of IamRole from a JSON string
iam_role_instance = IamRole.from_json(json)
# print the JSON string representation of the object
print(IamRole.to_json())

# convert the object into a dict
iam_role_dict = iam_role_instance.to_dict()
# create an instance of IamRole from a dict
iam_role_from_dict = IamRole.from_dict(iam_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


