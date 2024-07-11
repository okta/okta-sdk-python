# ContentSecurityPolicySetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | [optional] 
**report_uri** | **str** |  | [optional] 
**src_list** | **List[str]** |  | [optional] 

## Example

```python
from okta.models.content_security_policy_setting import ContentSecurityPolicySetting

# TODO update the JSON string below
json = "{}"
# create an instance of ContentSecurityPolicySetting from a JSON string
content_security_policy_setting_instance = ContentSecurityPolicySetting.from_json(json)
# print the JSON string representation of the object
print(ContentSecurityPolicySetting.to_json())

# convert the object into a dict
content_security_policy_setting_dict = content_security_policy_setting_instance.to_dict()
# create an instance of ContentSecurityPolicySetting from a dict
content_security_policy_setting_from_dict = ContentSecurityPolicySetting.from_dict(content_security_policy_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


