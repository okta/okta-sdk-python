# RecoveryQuestionCredential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer** | **str** |  | [optional] 
**question** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.recovery_question_credential import RecoveryQuestionCredential

# TODO update the JSON string below
json = "{}"
# create an instance of RecoveryQuestionCredential from a JSON string
recovery_question_credential_instance = RecoveryQuestionCredential.from_json(json)
# print the JSON string representation of the object
print(RecoveryQuestionCredential.to_json())

# convert the object into a dict
recovery_question_credential_dict = recovery_question_credential_instance.to_dict()
# create an instance of RecoveryQuestionCredential from a dict
recovery_question_credential_form_dict = recovery_question_credential.from_dict(recovery_question_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


