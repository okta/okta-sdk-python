# PasswordImportRequestDataAction

This object specifies the default action Okta is set to take. Okta takes this action if your external service sends an empty HTTP 204 response. You can override the default action by returning a commands object in your response specifying the action to take.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential** | **str** | The status of the user credential, either &#x60;UNVERIFIED&#x60; or &#x60;VERIFIED&#x60; | [optional] [default to 'UNVERIFIED']

## Example

```python
from okta.models.password_import_request_data_action import PasswordImportRequestDataAction

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordImportRequestDataAction from a JSON string
password_import_request_data_action_instance = PasswordImportRequestDataAction.from_json(json)
# print the JSON string representation of the object
print(PasswordImportRequestDataAction.to_json())

# convert the object into a dict
password_import_request_data_action_dict = password_import_request_data_action_instance.to_dict()
# create an instance of PasswordImportRequestDataAction from a dict
password_import_request_data_action_from_dict = PasswordImportRequestDataAction.from_dict(password_import_request_data_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


