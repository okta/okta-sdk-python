# UserFactorSecurityQuestion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**UserFactorSecurityQuestionProfile**](UserFactorSecurityQuestionProfile.md) |  | [optional] 

## Example

```python
from okta.models.user_factor_security_question import UserFactorSecurityQuestion

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorSecurityQuestion from a JSON string
user_factor_security_question_instance = UserFactorSecurityQuestion.from_json(json)
# print the JSON string representation of the object
print(UserFactorSecurityQuestion.to_json())

# convert the object into a dict
user_factor_security_question_dict = user_factor_security_question_instance.to_dict()
# create an instance of UserFactorSecurityQuestion from a dict
user_factor_security_question_from_dict = UserFactorSecurityQuestion.from_dict(user_factor_security_question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


