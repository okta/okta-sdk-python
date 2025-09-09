# IamRoleLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**permissions** | [**HrefObject**](HrefObject.md) |  | [optional] 

## Example

```python
from okta.models.iam_role_links import IamRoleLinks

# TODO update the JSON string below
json = "{}"
# create an instance of IamRoleLinks from a JSON string
iam_role_links_instance = IamRoleLinks.from_json(json)
# print the JSON string representation of the object
print(IamRoleLinks.to_json())

# convert the object into a dict
iam_role_links_dict = iam_role_links_instance.to_dict()
# create an instance of IamRoleLinks from a dict
iam_role_links_from_dict = IamRoleLinks.from_dict(iam_role_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


