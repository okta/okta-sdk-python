# SecurityQuestionUserFactor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**SecurityQuestionUserFactorProfile**](SecurityQuestionUserFactorProfile.md) |  | [optional] 

## Example

```python
from openapi_client.models.security_question_user_factor import SecurityQuestionUserFactor

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityQuestionUserFactor from a JSON string
security_question_user_factor_instance = SecurityQuestionUserFactor.from_json(json)
# print the JSON string representation of the object
print(SecurityQuestionUserFactor.to_json())

# convert the object into a dict
security_question_user_factor_dict = security_question_user_factor_instance.to_dict()
# create an instance of SecurityQuestionUserFactor from a dict
security_question_user_factor_form_dict = security_question_user_factor.from_dict(security_question_user_factor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


