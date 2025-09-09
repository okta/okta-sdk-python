# WsFederationApplicationSettingsApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_statements** | **str** |  | [optional] 
**audience_restriction** | **str** |  | [optional] 
**authn_context_class_ref** | **str** |  | [optional] 
**group_filter** | **str** |  | [optional] 
**group_name** | **str** |  | [optional] 
**group_value_format** | **str** |  | [optional] 
**name_id_format** | **str** |  | [optional] 
**realm** | **str** |  | [optional] 
**site_url** | **str** |  | [optional] 
**username_attribute** | **str** |  | [optional] 
**w_reply_override** | **bool** |  | [optional] 
**w_reply_url** | **str** |  | [optional] 

## Example

```python
from okta.models.ws_federation_application_settings_application import WsFederationApplicationSettingsApplication

# TODO update the JSON string below
json = "{}"
# create an instance of WsFederationApplicationSettingsApplication from a JSON string
ws_federation_application_settings_application_instance = WsFederationApplicationSettingsApplication.from_json(json)
# print the JSON string representation of the object
print(WsFederationApplicationSettingsApplication.to_json())

# convert the object into a dict
ws_federation_application_settings_application_dict = ws_federation_application_settings_application_instance.to_dict()
# create an instance of WsFederationApplicationSettingsApplication from a dict
ws_federation_application_settings_application_from_dict = WsFederationApplicationSettingsApplication.from_dict(ws_federation_application_settings_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


