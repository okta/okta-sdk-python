# OrgSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** | Primary address of the organization associated with the org | [optional] 
**address2** | **str** | Secondary address of the organization associated with the org | [optional] 
**city** | **str** | City of the organization associated with the org | [optional] 
**company_name** | **str** | Name of org | [optional] 
**country** | **str** | County of the organization associated with the org | [optional] 
**created** | **datetime** | When org was created | [optional] [readonly] 
**end_user_support_help_url** | **str** | Support link of org | [optional] 
**expires_at** | **datetime** | Expiration of org | [optional] [readonly] 
**id** | **str** | Org ID | [optional] [readonly] 
**last_updated** | **datetime** | When org was last updated | [optional] [readonly] 
**phone_number** | **str** | Phone number of the organization associated with the org | [optional] 
**postal_code** | **str** | Postal code of the organization associated with the org | [optional] 
**state** | **str** | State of the organization associated with the org | [optional] 
**status** | **str** | Status of org | [optional] [readonly] 
**subdomain** | **str** | Subdomain of org | [optional] [readonly] 
**support_phone_number** | **str** | Support help phone of the organization associated with the org | [optional] 
**website** | **str** | Website of the organization associated with the org | [optional] 
**links** | [**OrgGeneralSettingLinks**](OrgGeneralSettingLinks.md) |  | [optional] 

## Example

```python
from okta.models.org_setting import OrgSetting

# TODO update the JSON string below
json = "{}"
# create an instance of OrgSetting from a JSON string
org_setting_instance = OrgSetting.from_json(json)
# print the JSON string representation of the object
print(OrgSetting.to_json())

# convert the object into a dict
org_setting_dict = org_setting_instance.to_dict()
# create an instance of OrgSetting from a dict
org_setting_from_dict = OrgSetting.from_dict(org_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


