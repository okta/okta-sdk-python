# OrgPreferences


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**show_end_user_footer** | **bool** |  | [optional] [readonly] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.org_preferences import OrgPreferences

# TODO update the JSON string below
json = "{}"
# create an instance of OrgPreferences from a JSON string
org_preferences_instance = OrgPreferences.from_json(json)
# print the JSON string representation of the object
print(OrgPreferences.to_json())

# convert the object into a dict
org_preferences_dict = org_preferences_instance.to_dict()
# create an instance of OrgPreferences from a dict
org_preferences_from_dict = OrgPreferences.from_dict(org_preferences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


