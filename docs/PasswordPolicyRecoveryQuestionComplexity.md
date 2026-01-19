# PasswordPolicyRecoveryQuestionComplexity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_length** | **int** | Minimum length of the password recovery question answer | [optional] [readonly] [default to 4]

## Example

```python
from okta.models.password_policy_recovery_question_complexity import PasswordPolicyRecoveryQuestionComplexity

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyRecoveryQuestionComplexity from a JSON string
password_policy_recovery_question_complexity_instance = PasswordPolicyRecoveryQuestionComplexity.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicyRecoveryQuestionComplexity.to_json())

# convert the object into a dict
password_policy_recovery_question_complexity_dict = password_policy_recovery_question_complexity_instance.to_dict()
# create an instance of PasswordPolicyRecoveryQuestionComplexity from a dict
password_policy_recovery_question_complexity_from_dict = PasswordPolicyRecoveryQuestionComplexity.from_dict(password_policy_recovery_question_complexity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


