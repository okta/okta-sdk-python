# UserImportResponseCommandsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The command types supported for the import inline hook. When using the &#x60;com.okta.action.update&#x60; command to specify that the user should be treated as a match, you need to also provide a &#x60;com.okta.user.update&#x60; command that sets the ID of the Okta user. | [optional] 
**value** | **Dict[str, str]** | The &#x60;value&#x60; object is the parameter to pass to the command. In the case of the &#x60;com.okta.appUser.profile.update&#x60; and &#x60;com.okta.user.profile.update&#x60; commands, the parameter should be a list of one or more profile attributes and the values you wish to set them to. In the case of the &#x60;com.okta.action.update&#x60; command, the parameter should be a &#x60;result&#x60; property set to either &#x60;CREATE_USER&#x60; or &#x60;LINK_USER&#x60;. | [optional] 

## Example

```python
from okta.models.user_import_response_commands_inner import UserImportResponseCommandsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UserImportResponseCommandsInner from a JSON string
user_import_response_commands_inner_instance = UserImportResponseCommandsInner.from_json(json)
# print the JSON string representation of the object
print(UserImportResponseCommandsInner.to_json())

# convert the object into a dict
user_import_response_commands_inner_dict = user_import_response_commands_inner_instance.to_dict()
# create an instance of UserImportResponseCommandsInner from a dict
user_import_response_commands_inner_from_dict = UserImportResponseCommandsInner.from_dict(user_import_response_commands_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


