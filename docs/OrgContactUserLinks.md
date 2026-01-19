# OrgContactUserLinks

Specifies link relations (see [Web Linking](https://www.rfc-editor.org/rfc/rfc8288)) available for the contact type user object using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**HrefObjectUserLink**](HrefObjectUserLink.md) |  | [optional] 

## Example

```python
from okta.models.org_contact_user_links import OrgContactUserLinks

# TODO update the JSON string below
json = "{}"
# create an instance of OrgContactUserLinks from a JSON string
org_contact_user_links_instance = OrgContactUserLinks.from_json(json)
# print the JSON string representation of the object
print(OrgContactUserLinks.to_json())

# convert the object into a dict
org_contact_user_links_dict = org_contact_user_links_instance.to_dict()
# create an instance of OrgContactUserLinks from a dict
org_contact_user_links_from_dict = OrgContactUserLinks.from_dict(org_contact_user_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


