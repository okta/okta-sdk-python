# ProfileEnrollmentPolicyRuleProfileAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.profile_enrollment_policy_rule_profile_attribute import ProfileEnrollmentPolicyRuleProfileAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileEnrollmentPolicyRuleProfileAttribute from a JSON string
profile_enrollment_policy_rule_profile_attribute_instance = ProfileEnrollmentPolicyRuleProfileAttribute.from_json(json)
# print the JSON string representation of the object
print(ProfileEnrollmentPolicyRuleProfileAttribute.to_json())

# convert the object into a dict
profile_enrollment_policy_rule_profile_attribute_dict = profile_enrollment_policy_rule_profile_attribute_instance.to_dict()
# create an instance of ProfileEnrollmentPolicyRuleProfileAttribute from a dict
profile_enrollment_policy_rule_profile_attribute_form_dict = profile_enrollment_policy_rule_profile_attribute.from_dict(profile_enrollment_policy_rule_profile_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


