# MultifactorEnrollmentPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**PolicyRuleConditions**](PolicyRuleConditions.md) |  | [optional] 
**settings** | [**MultifactorEnrollmentPolicySettings**](MultifactorEnrollmentPolicySettings.md) |  | [optional] 

## Example

```python
from openapi_client.models.multifactor_enrollment_policy import MultifactorEnrollmentPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of MultifactorEnrollmentPolicy from a JSON string
multifactor_enrollment_policy_instance = MultifactorEnrollmentPolicy.from_json(json)
# print the JSON string representation of the object
print(MultifactorEnrollmentPolicy.to_json())

# convert the object into a dict
multifactor_enrollment_policy_dict = multifactor_enrollment_policy_instance.to_dict()
# create an instance of MultifactorEnrollmentPolicy from a dict
multifactor_enrollment_policy_from_dict = MultifactorEnrollmentPolicy.from_dict(multifactor_enrollment_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


