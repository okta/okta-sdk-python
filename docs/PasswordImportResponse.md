# PasswordImportResponse

Password import inline hook response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commands** | [**List[PasswordImportResponseCommandsInner]**](PasswordImportResponseCommandsInner.md) | The &#x60;commands&#x60; object specifies whether Okta accepts the end user&#39;s sign-in credentials as valid or not. For the password import inline hook, you typically only return one &#x60;commands&#x60; object with one array element in it. | [optional] 

## Example

```python
from okta.models.password_import_response import PasswordImportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordImportResponse from a JSON string
password_import_response_instance = PasswordImportResponse.from_json(json)
# print the JSON string representation of the object
print(PasswordImportResponse.to_json())

# convert the object into a dict
password_import_response_dict = password_import_response_instance.to_dict()
# create an instance of PasswordImportResponse from a dict
password_import_response_from_dict = PasswordImportResponse.from_dict(password_import_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


