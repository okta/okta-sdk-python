# GroupProfile

Specifies required and optional properties for a group. The `objectClass` of a group determines which additional properties are available.  You can extend group profiles with custom properties, but you must first add the properties to the group profile schema before you can reference them. Use the Profile Editor in the Admin Console or the [Schemas API](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Schema/) to manage schema extensions.  Custom properties can contain HTML tags. It is the client's responsibility to escape or encode this data before displaying it. Use [best-practices](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html) to prevent cross-site scripting.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the Windows group | [optional] 
**name** | **str** | Name of the Windows group | [optional] 
**object_class** | **str** | The object class type | [optional] [readonly] 
**dn** | **str** | The distinguished name of the Windows group | [optional] 
**external_id** | **str** | Base-64 encoded GUID (&#x60;objectGUID&#x60;) of the Windows group | [optional] 
**group_scope** | **str** | The scope of the Windows group (DomainLocal, Global, or Universal) | [optional] 
**group_type** | **str** | The type of the Windows group (Security or Distribution) | [optional] 
**managed_by** | **str** | Distinguished name of the group that manages this group | [optional] 
**object_sid** | **str** | The Windows Security Identifier (SID) for the group | [optional] 
**sam_account_name** | **str** | Pre-Windows 2000 name of the Windows group | [optional] 
**windows_domain_qualified_name** | **str** | Fully qualified name of the Windows group | [optional] 

## Example

```python
from okta.models.group_profile import GroupProfile

# TODO update the JSON string below
json = "{}"
# create an instance of GroupProfile from a JSON string
group_profile_instance = GroupProfile.from_json(json)
# print the JSON string representation of the object
print(GroupProfile.to_json())

# convert the object into a dict
group_profile_dict = group_profile_instance.to_dict()
# create an instance of GroupProfile from a dict
group_profile_from_dict = GroupProfile.from_dict(group_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


