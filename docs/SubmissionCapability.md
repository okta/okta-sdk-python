# SubmissionCapability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capability** | [**Capability**](Capability.md) |  | 
**supported_protocols** | [**List[Protocol]**](Protocol.md) |  | 

## Example

```python
from okta.models.submission_capability import SubmissionCapability

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionCapability from a JSON string
submission_capability_instance = SubmissionCapability.from_json(json)
# print the JSON string representation of the object
print(SubmissionCapability.to_json())

# convert the object into a dict
submission_capability_dict = submission_capability_instance.to_dict()
# create an instance of SubmissionCapability from a dict
submission_capability_from_dict = SubmissionCapability.from_dict(submission_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


