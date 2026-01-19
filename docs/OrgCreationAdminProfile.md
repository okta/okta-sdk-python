# OrgCreationAdminProfile

Specifies the profile attributes for the first super admin user. The minimal set of required attributes are `email`, `firstName`, `lastName`, and `login`. See [profile](/openapi/okta-management/management/tag/User/#tag/User/operation/getUser!c=200&path=profile&t=response) for additional profile attributes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | Given name of the User (&#x60;givenName&#x60;) | 
**last_name** | **str** | The family name of the User (&#x60;familyName&#x60;) | 
**email** | **str** | The primary email address of the User. For validation, see [RFC 5322 Section 3.2.3](https://datatracker.ietf.org/doc/html/rfc5322#section-3.2.3). | 
**login** | **str** | The unique identifier for the User (&#x60;username&#x60;) | 

## Example

```python
from okta.models.org_creation_admin_profile import OrgCreationAdminProfile

# TODO update the JSON string below
json = "{}"
# create an instance of OrgCreationAdminProfile from a JSON string
org_creation_admin_profile_instance = OrgCreationAdminProfile.from_json(json)
# print the JSON string representation of the object
print(OrgCreationAdminProfile.to_json())

# convert the object into a dict
org_creation_admin_profile_dict = org_creation_admin_profile_instance.to_dict()
# create an instance of OrgCreationAdminProfile from a dict
org_creation_admin_profile_from_dict = OrgCreationAdminProfile.from_dict(org_creation_admin_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


