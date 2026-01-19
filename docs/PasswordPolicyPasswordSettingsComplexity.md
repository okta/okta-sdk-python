# PasswordPolicyPasswordSettingsComplexity

Complexity settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dictionary** | [**PasswordDictionary**](PasswordDictionary.md) |  | [optional] 
**exclude_attributes** | **List[str]** | The User profile attributes whose values must be excluded from the password: currently only supports &#x60;firstName&#x60; and &#x60;lastName&#x60; | [optional] [default to []]
**exclude_username** | **bool** | Indicates if the Username must be excluded from the password | [optional] [default to True]
**min_length** | **int** | Minimum password length | [optional] [default to 8]
**min_lower_case** | **int** | Indicates if a password must contain at least one lower case letter: &#x60;0&#x60; indicates no, &#x60;1&#x60; indicates yes | [optional] [default to 1]
**min_number** | **int** | Indicates if a password must contain at least one number: &#x60;0&#x60; indicates no, &#x60;1&#x60; indicates yes | [optional] [default to 1]
**min_symbol** | **int** | Indicates if a password must contain at least one symbol (For example: !@#$%^&amp;*): &#x60;0&#x60; indicates no, &#x60;1&#x60; indicates yes | [optional] [default to 1]
**min_upper_case** | **int** | Indicates if a password must contain at least one upper case letter: &#x60;0&#x60; indicates no, &#x60;1&#x60; indicates yes | [optional] [default to 1]
**oel_statement** | **str** | &lt;x-lifecycle-container&gt;&lt;x-lifecycle class&#x3D;\&quot;ea\&quot;&gt;&lt;/x-lifecycle&gt; &lt;x-lifecycle class&#x3D;\&quot;oie\&quot;&gt;&lt;/x-lifecycle&gt;&lt;/x-lifecycle-container&gt;Use an [Expression Language](https://developer.okta.com/docs/reference/okta-expression-language-in-identity-engine/) expression to block a word from being used in a password. You can only block one word per expression. Use the &#x60;OR&#x60; operator to connect multiple expressions to block multiple words. | [optional] 

## Example

```python
from okta.models.password_policy_password_settings_complexity import PasswordPolicyPasswordSettingsComplexity

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyPasswordSettingsComplexity from a JSON string
password_policy_password_settings_complexity_instance = PasswordPolicyPasswordSettingsComplexity.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicyPasswordSettingsComplexity.to_json())

# convert the object into a dict
password_policy_password_settings_complexity_dict = password_policy_password_settings_complexity_instance.to_dict()
# create an instance of PasswordPolicyPasswordSettingsComplexity from a dict
password_policy_password_settings_complexity_from_dict = PasswordPolicyPasswordSettingsComplexity.from_dict(password_policy_password_settings_complexity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


