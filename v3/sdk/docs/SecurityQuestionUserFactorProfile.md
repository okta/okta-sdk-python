# SecurityQuestionUserFactorProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer** | **str** |  | [optional] 
**question** | **str** |  | [optional] 
**question_text** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.security_question_user_factor_profile import SecurityQuestionUserFactorProfile

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityQuestionUserFactorProfile from a JSON string
security_question_user_factor_profile_instance = SecurityQuestionUserFactorProfile.from_json(json)
# print the JSON string representation of the object
print(SecurityQuestionUserFactorProfile.to_json())

# convert the object into a dict
security_question_user_factor_profile_dict = security_question_user_factor_profile_instance.to_dict()
# create an instance of SecurityQuestionUserFactorProfile from a dict
security_question_user_factor_profile_from_dict = SecurityQuestionUserFactorProfile.from_dict(security_question_user_factor_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


