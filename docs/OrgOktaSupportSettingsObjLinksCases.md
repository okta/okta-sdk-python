# OrgOktaSupportSettingsObjLinksCases


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
from okta.models.org_okta_support_settings_obj_links_cases import OrgOktaSupportSettingsObjLinksCases

# TODO update the JSON string below
json = "{}"
# create an instance of OrgOktaSupportSettingsObjLinksCases from a JSON string
org_okta_support_settings_obj_links_cases_instance = OrgOktaSupportSettingsObjLinksCases.from_json(json)
# print the JSON string representation of the object
print(OrgOktaSupportSettingsObjLinksCases.to_json())

# convert the object into a dict
org_okta_support_settings_obj_links_cases_dict = org_okta_support_settings_obj_links_cases_instance.to_dict()
# create an instance of OrgOktaSupportSettingsObjLinksCases from a dict
org_okta_support_settings_obj_links_cases_from_dict = OrgOktaSupportSettingsObjLinksCases.from_dict(org_okta_support_settings_obj_links_cases_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


