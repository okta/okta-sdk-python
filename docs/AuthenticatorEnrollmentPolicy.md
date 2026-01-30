# AuthenticatorEnrollmentPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**AuthenticatorEnrollmentPolicyConditions**](AuthenticatorEnrollmentPolicyConditions.md) |  | [optional] 
**settings** | [**AuthenticatorEnrollmentPolicySettings**](AuthenticatorEnrollmentPolicySettings.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_enrollment_policy import AuthenticatorEnrollmentPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorEnrollmentPolicy from a JSON string
authenticator_enrollment_policy_instance = AuthenticatorEnrollmentPolicy.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorEnrollmentPolicy.to_json())

# convert the object into a dict
authenticator_enrollment_policy_dict = authenticator_enrollment_policy_instance.to_dict()
# create an instance of AuthenticatorEnrollmentPolicy from a dict
authenticator_enrollment_policy_from_dict = AuthenticatorEnrollmentPolicy.from_dict(authenticator_enrollment_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


