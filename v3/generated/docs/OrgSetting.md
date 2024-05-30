# OrgSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] [readonly] 
**end_user_support_help_url** | **str** |  | [optional] 
**expires_at** | **datetime** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**last_updated** | **datetime** |  | [optional] [readonly] 
**phone_number** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**status** | **str** |  | [optional] [readonly] 
**subdomain** | **str** |  | [optional] [readonly] 
**support_phone_number** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from openapi_client.models.org_setting import OrgSetting

# TODO update the JSON string below
json = "{}"
# create an instance of OrgSetting from a JSON string
org_setting_instance = OrgSetting.from_json(json)
# print the JSON string representation of the object
print(OrgSetting.to_json())

# convert the object into a dict
org_setting_dict = org_setting_instance.to_dict()
# create an instance of OrgSetting from a dict
org_setting_form_dict = org_setting.from_dict(org_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


