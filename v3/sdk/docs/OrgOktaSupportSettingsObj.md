# OrgOktaSupportSettingsObj


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiration** | **datetime** |  | [optional] [readonly] 
**support** | [**OrgOktaSupportSetting**](OrgOktaSupportSetting.md) |  | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from openapi_client.models.org_okta_support_settings_obj import OrgOktaSupportSettingsObj

# TODO update the JSON string below
json = "{}"
# create an instance of OrgOktaSupportSettingsObj from a JSON string
org_okta_support_settings_obj_instance = OrgOktaSupportSettingsObj.from_json(json)
# print the JSON string representation of the object
print(OrgOktaSupportSettingsObj.to_json())

# convert the object into a dict
org_okta_support_settings_obj_dict = org_okta_support_settings_obj_instance.to_dict()
# create an instance of OrgOktaSupportSettingsObj from a dict
org_okta_support_settings_obj_from_dict = OrgOktaSupportSettingsObj.from_dict(org_okta_support_settings_obj_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


