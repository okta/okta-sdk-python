# OktaActiveDirectoryGroupProfile

Profile for a group that is imported from Active Directory.  The `objectClass` for such groups is `okta:windows_security_principal`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the Windows group | [optional] 
**dn** | **str** | The distinguished name of the Windows group | [optional] 
**external_id** | **str** | Base-64 encoded GUID (&#x60;objectGUID&#x60;) of the Windows group | [optional] 
**group_scope** | **str** | The scope of the Windows group (DomainLocal, Global, or Universal) | [optional] 
**group_type** | **str** | The type of the Windows group (Security or Distribution) | [optional] 
**managed_by** | **str** | Distinguished name of the group that manages this group | [optional] 
**name** | **str** | Name of the Windows group | [optional] 
**object_class** | **str** | The object class type | [optional] [readonly] 
**object_sid** | **str** | The Windows Security Identifier (SID) for the group | [optional] 
**sam_account_name** | **str** | Pre-Windows 2000 name of the Windows group | [optional] 
**windows_domain_qualified_name** | **str** | Fully qualified name of the Windows group | [optional] 

## Example

```python
from okta.models.okta_active_directory_group_profile import OktaActiveDirectoryGroupProfile

# TODO update the JSON string below
json = "{}"
# create an instance of OktaActiveDirectoryGroupProfile from a JSON string
okta_active_directory_group_profile_instance = OktaActiveDirectoryGroupProfile.from_json(json)
# print the JSON string representation of the object
print(OktaActiveDirectoryGroupProfile.to_json())

# convert the object into a dict
okta_active_directory_group_profile_dict = okta_active_directory_group_profile_instance.to_dict()
# create an instance of OktaActiveDirectoryGroupProfile from a dict
okta_active_directory_group_profile_from_dict = OktaActiveDirectoryGroupProfile.from_dict(okta_active_directory_group_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


