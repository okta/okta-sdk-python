# UserFactorSecurityQuestionProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer** | **str** | Answer to the question | [optional] 
**question** | **str** | Unique key for the question | [optional] 
**question_text** | **str** | Human-readable text that&#39;s displayed to the user | [optional] [readonly] 

## Example

```python
from okta.models.user_factor_security_question_profile import UserFactorSecurityQuestionProfile

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorSecurityQuestionProfile from a JSON string
user_factor_security_question_profile_instance = UserFactorSecurityQuestionProfile.from_json(json)
# print the JSON string representation of the object
print(UserFactorSecurityQuestionProfile.to_json())

# convert the object into a dict
user_factor_security_question_profile_dict = user_factor_security_question_profile_instance.to_dict()
# create an instance of UserFactorSecurityQuestionProfile from a dict
user_factor_security_question_profile_from_dict = UserFactorSecurityQuestionProfile.from_dict(user_factor_security_question_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


