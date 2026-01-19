# OrgOktaCommunicationSettingLinks

Specifies link relations (see [Web Linking](https://www.rfc-editor.org/rfc/rfc8288)) available for this object using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opt_in** | [**OrgOktaCommunicationSettingLinksOptIn**](OrgOktaCommunicationSettingLinksOptIn.md) |  | [optional] 
**opt_out** | [**OrgOktaCommunicationSettingLinksOptOut**](OrgOktaCommunicationSettingLinksOptOut.md) |  | [optional] 

## Example

```python
from okta.models.org_okta_communication_setting_links import OrgOktaCommunicationSettingLinks

# TODO update the JSON string below
json = "{}"
# create an instance of OrgOktaCommunicationSettingLinks from a JSON string
org_okta_communication_setting_links_instance = OrgOktaCommunicationSettingLinks.from_json(json)
# print the JSON string representation of the object
print(OrgOktaCommunicationSettingLinks.to_json())

# convert the object into a dict
org_okta_communication_setting_links_dict = org_okta_communication_setting_links_instance.to_dict()
# create an instance of OrgOktaCommunicationSettingLinks from a dict
org_okta_communication_setting_links_from_dict = OrgOktaCommunicationSettingLinks.from_dict(org_okta_communication_setting_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


