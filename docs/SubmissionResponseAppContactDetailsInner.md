# SubmissionResponseAppContactDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_type** | **str** | Type of contact * &#x60;CUSTOMER_SUPPORT&#x60; - Public support contact details visible on your OIN catalog page for end users needing assistance with your integration. * &#x60;ESCALATION_SUPPORT&#x60; - Private support contact used by Okta to reach your organization during emergencies or escalations post-publication of the app (not shared with customers).  | 
**contact_value_type** | **str** | Format of the contact value | 
**contact** | **str** | The contact value (email, phone, or URL) | 

## Example

```python
from okta.models.submission_response_app_contact_details_inner import SubmissionResponseAppContactDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionResponseAppContactDetailsInner from a JSON string
submission_response_app_contact_details_inner_instance = SubmissionResponseAppContactDetailsInner.from_json(json)
# print the JSON string representation of the object
print(SubmissionResponseAppContactDetailsInner.to_json())

# convert the object into a dict
submission_response_app_contact_details_inner_dict = submission_response_app_contact_details_inner_instance.to_dict()
# create an instance of SubmissionResponseAppContactDetailsInner from a dict
submission_response_app_contact_details_inner_from_dict = SubmissionResponseAppContactDetailsInner.from_dict(submission_response_app_contact_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


