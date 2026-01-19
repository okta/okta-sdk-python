# SubmissionCapabilities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | [**List[SubmissionCapability]**](SubmissionCapability.md) |  | 

## Example

```python
from okta.models.submission_capabilities import SubmissionCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionCapabilities from a JSON string
submission_capabilities_instance = SubmissionCapabilities.from_json(json)
# print the JSON string representation of the object
print(SubmissionCapabilities.to_json())

# convert the object into a dict
submission_capabilities_dict = submission_capabilities_instance.to_dict()
# create an instance of SubmissionCapabilities from a dict
submission_capabilities_from_dict = SubmissionCapabilities.from_dict(submission_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


