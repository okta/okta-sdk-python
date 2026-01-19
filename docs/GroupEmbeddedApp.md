# GroupEmbeddedApp

If the group is sourced from an app, this object contains information about that app

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the &#x60;AppInstance&#x60; | [optional] 
**name** | **str** | The name of the &#x60;AppInstance&#x60; | [optional] 
**label** | **str** | The user-facing display name of the &#x60;AppInstance&#x60; | [optional] 
**sign_on_mode** | **str** | The configured sign-on mode for the &#x60;AppInstance&#x60; | [optional] 

## Example

```python
from okta.models.group_embedded_app import GroupEmbeddedApp

# TODO update the JSON string below
json = "{}"
# create an instance of GroupEmbeddedApp from a JSON string
group_embedded_app_instance = GroupEmbeddedApp.from_json(json)
# print the JSON string representation of the object
print(GroupEmbeddedApp.to_json())

# convert the object into a dict
group_embedded_app_dict = group_embedded_app_instance.to_dict()
# create an instance of GroupEmbeddedApp from a dict
group_embedded_app_from_dict = GroupEmbeddedApp.from_dict(group_embedded_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


