# PasswordDictionaryCommon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude** | **bool** |  | [optional] [default to False]

## Example

```python
from okta.models.password_dictionary_common import PasswordDictionaryCommon

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordDictionaryCommon from a JSON string
password_dictionary_common_instance = PasswordDictionaryCommon.from_json(json)
# print the JSON string representation of the object
print(PasswordDictionaryCommon.to_json())

# convert the object into a dict
password_dictionary_common_dict = password_dictionary_common_instance.to_dict()
# create an instance of PasswordDictionaryCommon from a dict
password_dictionary_common_from_dict = PasswordDictionaryCommon.from_dict(password_dictionary_common_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


