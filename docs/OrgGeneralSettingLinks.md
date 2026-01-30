# OrgGeneralSettingLinks

Specifies link relations (see [Web Linking](https://www.rfc-editor.org/rfc/rfc8288)) available for the org using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contacts** | [**OrgGeneralSettingLinksContacts**](OrgGeneralSettingLinksContacts.md) |  | [optional] 
**logo** | [**OrgGeneralSettingLinksLogo**](OrgGeneralSettingLinksLogo.md) |  | [optional] 
**okta_communication** | [**OrgGeneralSettingLinksOktaCommunication**](OrgGeneralSettingLinksOktaCommunication.md) |  | [optional] 
**okta_support** | [**OrgGeneralSettingLinksOktaSupport**](OrgGeneralSettingLinksOktaSupport.md) |  | [optional] 
**preferences** | [**OrgGeneralSettingLinksPreferences**](OrgGeneralSettingLinksPreferences.md) |  | [optional] 
**upload_logo** | [**OrgGeneralSettingLinksUploadLogo**](OrgGeneralSettingLinksUploadLogo.md) |  | [optional] 

## Example

```python
from okta.models.org_general_setting_links import OrgGeneralSettingLinks

# TODO update the JSON string below
json = "{}"
# create an instance of OrgGeneralSettingLinks from a JSON string
org_general_setting_links_instance = OrgGeneralSettingLinks.from_json(json)
# print the JSON string representation of the object
print(OrgGeneralSettingLinks.to_json())

# convert the object into a dict
org_general_setting_links_dict = org_general_setting_links_instance.to_dict()
# create an instance of OrgGeneralSettingLinks from a dict
org_general_setting_links_from_dict = OrgGeneralSettingLinks.from_dict(org_general_setting_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


