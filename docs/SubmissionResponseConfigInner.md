# SubmissionResponseConfigInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Display name of the variable in the Admin Console | [optional] 
**name** | **str** | Name of the variable | [optional] 

## Example

```python
from okta.models.submission_response_config_inner import SubmissionResponseConfigInner

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionResponseConfigInner from a JSON string
submission_response_config_inner_instance = SubmissionResponseConfigInner.from_json(json)
# print the JSON string representation of the object
print(SubmissionResponseConfigInner.to_json())

# convert the object into a dict
submission_response_config_inner_dict = submission_response_config_inner_instance.to_dict()
# create an instance of SubmissionResponseConfigInner from a dict
submission_response_config_inner_from_dict = SubmissionResponseConfigInner.from_dict(submission_response_config_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


