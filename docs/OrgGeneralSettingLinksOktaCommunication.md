# OrgGeneralSettingLinksOktaCommunication


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
from okta.models.org_general_setting_links_okta_communication import OrgGeneralSettingLinksOktaCommunication

# TODO update the JSON string below
json = "{}"
# create an instance of OrgGeneralSettingLinksOktaCommunication from a JSON string
org_general_setting_links_okta_communication_instance = OrgGeneralSettingLinksOktaCommunication.from_json(json)
# print the JSON string representation of the object
print(OrgGeneralSettingLinksOktaCommunication.to_json())

# convert the object into a dict
org_general_setting_links_okta_communication_dict = org_general_setting_links_okta_communication_instance.to_dict()
# create an instance of OrgGeneralSettingLinksOktaCommunication from a dict
org_general_setting_links_okta_communication_from_dict = OrgGeneralSettingLinksOktaCommunication.from_dict(org_general_setting_links_okta_communication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


