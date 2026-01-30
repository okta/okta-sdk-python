# OrgOktaCommunicationSettingLinksOptOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hints** | [**HrefHints**](HrefHints.md) |  | [optional] 
**href** | **str** | Link URI | 
**name** | **str** | Link name | [optional] [readonly] 
**templated** | **bool** | Indicates whether the link object&#39;s &#x60;href&#x60; property is a URI template. | [optional] [readonly] 
**type** | **str** | The media type of the link. If omitted, it is implicitly &#x60;application/json&#x60;. | [optional] [readonly] 

## Example

```python
from okta.models.org_okta_communication_setting_links_opt_out import OrgOktaCommunicationSettingLinksOptOut

# TODO update the JSON string below
json = "{}"
# create an instance of OrgOktaCommunicationSettingLinksOptOut from a JSON string
org_okta_communication_setting_links_opt_out_instance = OrgOktaCommunicationSettingLinksOptOut.from_json(json)
# print the JSON string representation of the object
print(OrgOktaCommunicationSettingLinksOptOut.to_json())

# convert the object into a dict
org_okta_communication_setting_links_opt_out_dict = org_okta_communication_setting_links_opt_out_instance.to_dict()
# create an instance of OrgOktaCommunicationSettingLinksOptOut from a dict
org_okta_communication_setting_links_opt_out_from_dict = OrgOktaCommunicationSettingLinksOptOut.from_dict(org_okta_communication_setting_links_opt_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


