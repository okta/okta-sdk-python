# PersonalAppsBlockList

Defines a list of email domains with a subset of the properties for each domain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | **List[str]** | List of blocked email domains | [optional] 

## Example

```python
from okta.models.personal_apps_block_list import PersonalAppsBlockList

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalAppsBlockList from a JSON string
personal_apps_block_list_instance = PersonalAppsBlockList.from_json(json)
# print the JSON string representation of the object
print(PersonalAppsBlockList.to_json())

# convert the object into a dict
personal_apps_block_list_dict = personal_apps_block_list_instance.to_dict()
# create an instance of PersonalAppsBlockList from a dict
personal_apps_block_list_from_dict = PersonalAppsBlockList.from_dict(personal_apps_block_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


