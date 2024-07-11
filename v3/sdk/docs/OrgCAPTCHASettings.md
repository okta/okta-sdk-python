# OrgCAPTCHASettings



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**captcha_id** | **str** | The unique key of the associated CAPTCHA instance | [optional] 
**enabled_pages** | [**List[EnabledPagesType]**](EnabledPagesType.md) | An array of pages that have CAPTCHA enabled | [optional] 
**links** | [**OrgCAPTCHASettingsLinks**](OrgCAPTCHASettingsLinks.md) |  | [optional] 

## Example

```python
from okta.models.org_captcha_settings import OrgCAPTCHASettings

# TODO update the JSON string below
json = "{}"
# create an instance of OrgCAPTCHASettings from a JSON string
org_captcha_settings_instance = OrgCAPTCHASettings.from_json(json)
# print the JSON string representation of the object
print(OrgCAPTCHASettings.to_json())

# convert the object into a dict
org_captcha_settings_dict = org_captcha_settings_instance.to_dict()
# create an instance of OrgCAPTCHASettings from a dict
org_captcha_settings_from_dict = OrgCAPTCHASettings.from_dict(org_captcha_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


