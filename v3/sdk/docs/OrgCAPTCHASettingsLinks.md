# OrgCAPTCHASettingsLinks

Link relations for the CAPTCHA settings object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObject**](HrefObject.md) |  | [optional] 

## Example

```python
from okta.models.org_captcha_settings_links import OrgCAPTCHASettingsLinks

# TODO update the JSON string below
json = "{}"
# create an instance of OrgCAPTCHASettingsLinks from a JSON string
org_captcha_settings_links_instance = OrgCAPTCHASettingsLinks.from_json(json)
# print the JSON string representation of the object
print(OrgCAPTCHASettingsLinks.to_json())

# convert the object into a dict
org_captcha_settings_links_dict = org_captcha_settings_links_instance.to_dict()
# create an instance of OrgCAPTCHASettingsLinks from a dict
org_captcha_settings_links_from_dict = OrgCAPTCHASettingsLinks.from_dict(org_captcha_settings_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


