# OktaPersonalAdminFeatureSettings

Defines a list of Okta Personal settings that can be enabled or disabled for the org

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_enduser_entry_points** | **bool** | Allow entry points for an Okta Personal account in a Workforce org | [optional] 
**enable_export_apps** | **bool** | Allow users to migrate apps from a Workforce account to an Okta Personal account | [optional] 

## Example

```python
from okta.models.okta_personal_admin_feature_settings import OktaPersonalAdminFeatureSettings

# TODO update the JSON string below
json = "{}"
# create an instance of OktaPersonalAdminFeatureSettings from a JSON string
okta_personal_admin_feature_settings_instance = OktaPersonalAdminFeatureSettings.from_json(json)
# print the JSON string representation of the object
print(OktaPersonalAdminFeatureSettings.to_json())

# convert the object into a dict
okta_personal_admin_feature_settings_dict = okta_personal_admin_feature_settings_instance.to_dict()
# create an instance of OktaPersonalAdminFeatureSettings from a dict
okta_personal_admin_feature_settings_from_dict = OktaPersonalAdminFeatureSettings.from_dict(okta_personal_admin_feature_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


