# UserImportRequestDataAction

The object that specifies the default action Okta is set to take

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** | The current default action that results when Okta imports a user. The two possible values are &#x60;CREATE_USER&#x60; and &#x60;LINK_USER&#x60;. You can change the action that is taken by means of the commands object you return. | [optional] 

## Example

```python
from okta.models.user_import_request_data_action import UserImportRequestDataAction

# TODO update the JSON string below
json = "{}"
# create an instance of UserImportRequestDataAction from a JSON string
user_import_request_data_action_instance = UserImportRequestDataAction.from_json(json)
# print the JSON string representation of the object
print(UserImportRequestDataAction.to_json())

# convert the object into a dict
user_import_request_data_action_dict = user_import_request_data_action_instance.to_dict()
# create an instance of UserImportRequestDataAction from a dict
user_import_request_data_action_from_dict = UserImportRequestDataAction.from_dict(user_import_request_data_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


