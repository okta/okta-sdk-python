# OrgOktaCommunicationSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opt_out_email_users** | **bool** |  | [optional] [readonly] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.org_okta_communication_setting import OrgOktaCommunicationSetting

# TODO update the JSON string below
json = "{}"
# create an instance of OrgOktaCommunicationSetting from a JSON string
org_okta_communication_setting_instance = OrgOktaCommunicationSetting.from_json(json)
# print the JSON string representation of the object
print(OrgOktaCommunicationSetting.to_json())

# convert the object into a dict
org_okta_communication_setting_dict = org_okta_communication_setting_instance.to_dict()
# create an instance of OrgOktaCommunicationSetting from a dict
org_okta_communication_setting_from_dict = OrgOktaCommunicationSetting.from_dict(org_okta_communication_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


