# OrgPreferencesLinksHideEndUserFooter


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
from okta.models.org_preferences_links_hide_end_user_footer import OrgPreferencesLinksHideEndUserFooter

# TODO update the JSON string below
json = "{}"
# create an instance of OrgPreferencesLinksHideEndUserFooter from a JSON string
org_preferences_links_hide_end_user_footer_instance = OrgPreferencesLinksHideEndUserFooter.from_json(json)
# print the JSON string representation of the object
print(OrgPreferencesLinksHideEndUserFooter.to_json())

# convert the object into a dict
org_preferences_links_hide_end_user_footer_dict = org_preferences_links_hide_end_user_footer_instance.to_dict()
# create an instance of OrgPreferencesLinksHideEndUserFooter from a dict
org_preferences_links_hide_end_user_footer_from_dict = OrgPreferencesLinksHideEndUserFooter.from_dict(org_preferences_links_hide_end_user_footer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


