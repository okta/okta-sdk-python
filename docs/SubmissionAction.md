# SubmissionAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Action identifier | 
**provider** | [**WorkflowActionProvider**](WorkflowActionProvider.md) |  | 

## Example

```python
from okta.models.submission_action import SubmissionAction

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionAction from a JSON string
submission_action_instance = SubmissionAction.from_json(json)
# print the JSON string representation of the object
print(SubmissionAction.to_json())

# convert the object into a dict
submission_action_dict = submission_action_instance.to_dict()
# create an instance of SubmissionAction from a dict
submission_action_from_dict = SubmissionAction.from_dict(submission_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


