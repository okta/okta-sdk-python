# EnrollmentPolicyAuthenticatorGracePeriod

<x-lifecycle-container><x-lifecycle class=\"oie\"></x-lifecycle></x-lifecycle-container>Specifies the time period required to complete an authenticator enrollment or setup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Grace period type | [optional] 

## Example

```python
from okta.models.enrollment_policy_authenticator_grace_period import EnrollmentPolicyAuthenticatorGracePeriod

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentPolicyAuthenticatorGracePeriod from a JSON string
enrollment_policy_authenticator_grace_period_instance = EnrollmentPolicyAuthenticatorGracePeriod.from_json(json)
# print the JSON string representation of the object
print(EnrollmentPolicyAuthenticatorGracePeriod.to_json())

# convert the object into a dict
enrollment_policy_authenticator_grace_period_dict = enrollment_policy_authenticator_grace_period_instance.to_dict()
# create an instance of EnrollmentPolicyAuthenticatorGracePeriod from a dict
enrollment_policy_authenticator_grace_period_from_dict = EnrollmentPolicyAuthenticatorGracePeriod.from_dict(enrollment_policy_authenticator_grace_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


