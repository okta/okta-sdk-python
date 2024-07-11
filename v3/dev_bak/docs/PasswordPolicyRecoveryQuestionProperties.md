# PasswordPolicyRecoveryQuestionProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complexity** | [**PasswordPolicyRecoveryQuestionComplexity**](PasswordPolicyRecoveryQuestionComplexity.md) |  | [optional] 

## Example

```python
from openapi_client.models.password_policy_recovery_question_properties import PasswordPolicyRecoveryQuestionProperties

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyRecoveryQuestionProperties from a JSON string
password_policy_recovery_question_properties_instance = PasswordPolicyRecoveryQuestionProperties.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicyRecoveryQuestionProperties.to_json())

# convert the object into a dict
password_policy_recovery_question_properties_dict = password_policy_recovery_question_properties_instance.to_dict()
# create an instance of PasswordPolicyRecoveryQuestionProperties from a dict
password_policy_recovery_question_properties_from_dict = PasswordPolicyRecoveryQuestionProperties.from_dict(password_policy_recovery_question_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


