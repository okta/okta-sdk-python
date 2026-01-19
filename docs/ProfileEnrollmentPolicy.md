# ProfileEnrollmentPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | **str** | Policy conditions aren&#39;t supported for this policy type | [optional] 

## Example

```python
from okta.models.profile_enrollment_policy import ProfileEnrollmentPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileEnrollmentPolicy from a JSON string
profile_enrollment_policy_instance = ProfileEnrollmentPolicy.from_json(json)
# print the JSON string representation of the object
print(ProfileEnrollmentPolicy.to_json())

# convert the object into a dict
profile_enrollment_policy_dict = profile_enrollment_policy_instance.to_dict()
# create an instance of ProfileEnrollmentPolicy from a dict
profile_enrollment_policy_from_dict = ProfileEnrollmentPolicy.from_dict(profile_enrollment_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


