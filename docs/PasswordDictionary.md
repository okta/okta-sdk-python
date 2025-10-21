# PasswordDictionary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common** | [**PasswordDictionaryCommon**](PasswordDictionaryCommon.md) |  | [optional] 

## Example

```python
from okta.models.password_dictionary import PasswordDictionary

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordDictionary from a JSON string
password_dictionary_instance = PasswordDictionary.from_json(json)
# print the JSON string representation of the object
print(PasswordDictionary.to_json())

# convert the object into a dict
password_dictionary_dict = password_dictionary_instance.to_dict()
# create an instance of PasswordDictionary from a dict
password_dictionary_from_dict = PasswordDictionary.from_dict(password_dictionary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


