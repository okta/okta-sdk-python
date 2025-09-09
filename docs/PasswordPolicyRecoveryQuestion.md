# PasswordPolicyRecoveryQuestion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**PasswordPolicyRecoveryQuestionProperties**](PasswordPolicyRecoveryQuestionProperties.md) |  | [optional] 
**status** | [**LifecycleStatus**](LifecycleStatus.md) |  | [optional] 

## Example

```python
from okta.models.password_policy_recovery_question import PasswordPolicyRecoveryQuestion

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyRecoveryQuestion from a JSON string
password_policy_recovery_question_instance = PasswordPolicyRecoveryQuestion.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicyRecoveryQuestion.to_json())

# convert the object into a dict
password_policy_recovery_question_dict = password_policy_recovery_question_instance.to_dict()
# create an instance of PasswordPolicyRecoveryQuestion from a dict
password_policy_recovery_question_from_dict = PasswordPolicyRecoveryQuestion.from_dict(password_policy_recovery_question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


