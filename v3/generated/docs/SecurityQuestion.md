# SecurityQuestion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer** | **str** |  | [optional] 
**question** | **str** |  | [optional] 
**question_text** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.security_question import SecurityQuestion

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityQuestion from a JSON string
security_question_instance = SecurityQuestion.from_json(json)
# print the JSON string representation of the object
print(SecurityQuestion.to_json())

# convert the object into a dict
security_question_dict = security_question_instance.to_dict()
# create an instance of SecurityQuestion from a dict
security_question_form_dict = security_question.from_dict(security_question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


