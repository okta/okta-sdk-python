# PolicySubject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** |  | [optional] 
**format** | **List[str]** |  | [optional] 
**match_attribute** | **str** |  | [optional] 
**match_type** | [**PolicySubjectMatchType**](PolicySubjectMatchType.md) |  | [optional] 
**user_name_template** | [**PolicyUserNameTemplate**](PolicyUserNameTemplate.md) |  | [optional] 

## Example

```python
from openapi_client.models.policy_subject import PolicySubject

# TODO update the JSON string below
json = "{}"
# create an instance of PolicySubject from a JSON string
policy_subject_instance = PolicySubject.from_json(json)
# print the JSON string representation of the object
print(PolicySubject.to_json())

# convert the object into a dict
policy_subject_dict = policy_subject_instance.to_dict()
# create an instance of PolicySubject from a dict
policy_subject_form_dict = policy_subject.from_dict(policy_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


