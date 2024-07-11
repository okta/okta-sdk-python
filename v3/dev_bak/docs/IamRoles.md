# IamRoles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | [**List[IamRole]**](IamRole.md) |  | [optional] 
**links** | [**LinksNext**](LinksNext.md) |  | [optional] 

## Example

```python
from openapi_client.models.iam_roles import IamRoles

# TODO update the JSON string below
json = "{}"
# create an instance of IamRoles from a JSON string
iam_roles_instance = IamRoles.from_json(json)
# print the JSON string representation of the object
print(IamRoles.to_json())

# convert the object into a dict
iam_roles_dict = iam_roles_instance.to_dict()
# create an instance of IamRoles from a dict
iam_roles_from_dict = IamRoles.from_dict(iam_roles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


