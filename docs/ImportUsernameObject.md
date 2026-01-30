# ImportUsernameObject

Determines the Okta username for the imported user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name_expression** | **str** | For &#x60;usernameFormat&#x3D;CUSTOM&#x60;, specifies the Okta Expression Language statement for a username format that imported users use to sign in to Okta | [optional] 
**username_format** | **str** | Determines the username format when users sign in to Okta | [default to 'EMAIL']

## Example

```python
from okta.models.import_username_object import ImportUsernameObject

# TODO update the JSON string below
json = "{}"
# create an instance of ImportUsernameObject from a JSON string
import_username_object_instance = ImportUsernameObject.from_json(json)
# print the JSON string representation of the object
print(ImportUsernameObject.to_json())

# convert the object into a dict
import_username_object_dict = import_username_object_instance.to_dict()
# create an instance of ImportUsernameObject from a dict
import_username_object_from_dict = ImportUsernameObject.from_dict(import_username_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


