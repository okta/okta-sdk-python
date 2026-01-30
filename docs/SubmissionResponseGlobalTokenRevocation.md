# SubmissionResponseGlobalTokenRevocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | URL of the authorization server&#39;s global token revocation endpoint | 
**subject_format** | **str** | The format of the subject | 
**auth_method** | **str** | Authentication method &lt;br&gt; **Note:** Currently, only the &#x60;SIGNED_JWT&#x60; method is supported. | 
**partial_logout** | **bool** | Allow partial support for Universal Logout | [optional] [default to False]

## Example

```python
from okta.models.submission_response_global_token_revocation import SubmissionResponseGlobalTokenRevocation

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionResponseGlobalTokenRevocation from a JSON string
submission_response_global_token_revocation_instance = SubmissionResponseGlobalTokenRevocation.from_json(json)
# print the JSON string representation of the object
print(SubmissionResponseGlobalTokenRevocation.to_json())

# convert the object into a dict
submission_response_global_token_revocation_dict = submission_response_global_token_revocation_instance.to_dict()
# create an instance of SubmissionResponseGlobalTokenRevocation from a dict
submission_response_global_token_revocation_from_dict = SubmissionResponseGlobalTokenRevocation.from_dict(submission_response_global_token_revocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


