# ThirdPartyAdminSetting

The third-party admin setting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**third_party_admin** | **bool** | Indicates if the third-party admin functionality is enabled | [optional] 

## Example

```python
from okta.models.third_party_admin_setting import ThirdPartyAdminSetting

# TODO update the JSON string below
json = "{}"
# create an instance of ThirdPartyAdminSetting from a JSON string
third_party_admin_setting_instance = ThirdPartyAdminSetting.from_json(json)
# print the JSON string representation of the object
print(ThirdPartyAdminSetting.to_json())

# convert the object into a dict
third_party_admin_setting_dict = third_party_admin_setting_instance.to_dict()
# create an instance of ThirdPartyAdminSetting from a dict
third_party_admin_setting_from_dict = ThirdPartyAdminSetting.from_dict(third_party_admin_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


