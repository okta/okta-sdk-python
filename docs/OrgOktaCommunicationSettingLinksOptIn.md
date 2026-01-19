# OrgOktaCommunicationSettingLinksOptIn


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
from okta.models.org_okta_communication_setting_links_opt_in import OrgOktaCommunicationSettingLinksOptIn

# TODO update the JSON string below
json = "{}"
# create an instance of OrgOktaCommunicationSettingLinksOptIn from a JSON string
org_okta_communication_setting_links_opt_in_instance = OrgOktaCommunicationSettingLinksOptIn.from_json(json)
# print the JSON string representation of the object
print(OrgOktaCommunicationSettingLinksOptIn.to_json())

# convert the object into a dict
org_okta_communication_setting_links_opt_in_dict = org_okta_communication_setting_links_opt_in_instance.to_dict()
# create an instance of OrgOktaCommunicationSettingLinksOptIn from a dict
org_okta_communication_setting_links_opt_in_from_dict = OrgOktaCommunicationSettingLinksOptIn.from_dict(org_okta_communication_setting_links_opt_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


