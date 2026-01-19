# SubmissionActions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[SubmissionAction]**](SubmissionAction.md) |  | [optional] 

## Example

```python
from okta.models.submission_actions import SubmissionActions

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionActions from a JSON string
submission_actions_instance = SubmissionActions.from_json(json)
# print the JSON string representation of the object
print(SubmissionActions.to_json())

# convert the object into a dict
submission_actions_dict = submission_actions_instance.to_dict()
# create an instance of SubmissionActions from a dict
submission_actions_from_dict = SubmissionActions.from_dict(submission_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


