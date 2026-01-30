# OktaUserGroupProfile

Profile for any group that is not imported from Active Directory. Specifies the standard and custom profile properties for a group.  The `objectClass` for these groups is `okta:user_group`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the group | [optional] 
**name** | **str** | Name of the group | [optional] 
**object_class** | **str** | The object class type | [optional] [readonly] 

## Example

```python
from okta.models.okta_user_group_profile import OktaUserGroupProfile

# TODO update the JSON string below
json = "{}"
# create an instance of OktaUserGroupProfile from a JSON string
okta_user_group_profile_instance = OktaUserGroupProfile.from_json(json)
# print the JSON string representation of the object
print(OktaUserGroupProfile.to_json())

# convert the object into a dict
okta_user_group_profile_dict = okta_user_group_profile_instance.to_dict()
# create an instance of OktaUserGroupProfile from a dict
okta_user_group_profile_from_dict = OktaUserGroupProfile.from_dict(okta_user_group_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


