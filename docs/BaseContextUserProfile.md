# BaseContextUserProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** | The username used to identify the user. This is often the user&#39;s email address. | [optional] 
**first_name** | **str** | The first name of the user | [optional] 
**last_name** | **str** | The last name of the user | [optional] 
**locale** | **str** | The user&#39;s default location for purposes of localizing items such as currency, date time format, numerical representations, and so on. A locale value is a concatenation of the [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) two-letter language code, an underscore, and the [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) two-letter country code. For example, &#x60;en_US&#x60; specifies the language English and country US. This value is &#x60;en_US&#x60; by default. | [optional] 
**time_zone** | **str** | The user&#39;s timezone | [optional] 

## Example

```python
from okta.models.base_context_user_profile import BaseContextUserProfile

# TODO update the JSON string below
json = "{}"
# create an instance of BaseContextUserProfile from a JSON string
base_context_user_profile_instance = BaseContextUserProfile.from_json(json)
# print the JSON string representation of the object
print(BaseContextUserProfile.to_json())

# convert the object into a dict
base_context_user_profile_dict = base_context_user_profile_instance.to_dict()
# create an instance of BaseContextUserProfile from a dict
base_context_user_profile_from_dict = BaseContextUserProfile.from_dict(base_context_user_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


