# OrgContactUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | Contact user ID | [optional] 
**links** | [**OrgContactUserLinks**](OrgContactUserLinks.md) |  | [optional] 

## Example

```python
from okta.models.org_contact_user import OrgContactUser

# TODO update the JSON string below
json = "{}"
# create an instance of OrgContactUser from a JSON string
org_contact_user_instance = OrgContactUser.from_json(json)
# print the JSON string representation of the object
print(OrgContactUser.to_json())

# convert the object into a dict
org_contact_user_dict = org_contact_user_instance.to_dict()
# create an instance of OrgContactUser from a dict
org_contact_user_from_dict = OrgContactUser.from_dict(org_contact_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


