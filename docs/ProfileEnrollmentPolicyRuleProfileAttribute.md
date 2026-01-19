# ProfileEnrollmentPolicyRuleProfileAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | A display-friendly label for this property | [optional] 
**name** | **str** | The name of a user profile property. Can be an existing property. | [optional] 
**required** | **bool** | (Optional, default &#x60;FALSE&#x60;) Indicates if this property is required for enrollment | [optional] [default to False]

## Example

```python
from okta.models.profile_enrollment_policy_rule_profile_attribute import ProfileEnrollmentPolicyRuleProfileAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileEnrollmentPolicyRuleProfileAttribute from a JSON string
profile_enrollment_policy_rule_profile_attribute_instance = ProfileEnrollmentPolicyRuleProfileAttribute.from_json(json)
# print the JSON string representation of the object
print(ProfileEnrollmentPolicyRuleProfileAttribute.to_json())

# convert the object into a dict
profile_enrollment_policy_rule_profile_attribute_dict = profile_enrollment_policy_rule_profile_attribute_instance.to_dict()
# create an instance of ProfileEnrollmentPolicyRuleProfileAttribute from a dict
profile_enrollment_policy_rule_profile_attribute_from_dict = ProfileEnrollmentPolicyRuleProfileAttribute.from_dict(profile_enrollment_policy_rule_profile_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


