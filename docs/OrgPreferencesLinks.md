# OrgPreferencesLinks

Specifies link relations (see [Web Linking](https://www.rfc-editor.org/rfc/rfc8288)) available for this object using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hide_end_user_footer** | [**OrgPreferencesLinksHideEndUserFooter**](OrgPreferencesLinksHideEndUserFooter.md) |  | [optional] 
**show_end_user_footer** | [**OrgPreferencesLinksShowEndUserFooter**](OrgPreferencesLinksShowEndUserFooter.md) |  | [optional] 

## Example

```python
from okta.models.org_preferences_links import OrgPreferencesLinks

# TODO update the JSON string below
json = "{}"
# create an instance of OrgPreferencesLinks from a JSON string
org_preferences_links_instance = OrgPreferencesLinks.from_json(json)
# print the JSON string representation of the object
print(OrgPreferencesLinks.to_json())

# convert the object into a dict
org_preferences_links_dict = org_preferences_links_instance.to_dict()
# create an instance of OrgPreferencesLinks from a dict
org_preferences_links_from_dict = OrgPreferencesLinks.from_dict(org_preferences_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


