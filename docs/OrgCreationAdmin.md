# OrgCreationAdmin

Profile and credential information for the first super admin user of the child org. If you plan to configure and manage the org programmatically, create a system user with a dedicated email address and a strong password. > **Note:** If you don't provide `credentials`, the super admin user is prompted to set up their credentials when they sign in to the org for the first time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**OrgCreationAdminCredentials**](OrgCreationAdminCredentials.md) |  | [optional] 
**profile** | [**OrgCreationAdminProfile**](OrgCreationAdminProfile.md) |  | 

## Example

```python
from okta.models.org_creation_admin import OrgCreationAdmin

# TODO update the JSON string below
json = "{}"
# create an instance of OrgCreationAdmin from a JSON string
org_creation_admin_instance = OrgCreationAdmin.from_json(json)
# print the JSON string representation of the object
print(OrgCreationAdmin.to_json())

# convert the object into a dict
org_creation_admin_dict = org_creation_admin_instance.to_dict()
# create an instance of OrgCreationAdmin from a dict
org_creation_admin_from_dict = OrgCreationAdmin.from_dict(org_creation_admin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


