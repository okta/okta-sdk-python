# SsprStepUpRequirement

Defines the secondary authenticators needed for password reset if `required` is true. The following are three valid configurations: * `required`=false * `required`=true with no methods to use any SSO authenticator * `required`=true with `security_question` as the method

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**methods** | **List[str]** | Authenticator methods required for secondary authentication step of password recovery. Specify this value only when &#x60;required&#x60; is true and &#x60;security_question&#x60; is permitted for the secondary authentication. | [optional] 
**required** | **bool** |  | [optional] 

## Example

```python
from okta.models.sspr_step_up_requirement import SsprStepUpRequirement

# TODO update the JSON string below
json = "{}"
# create an instance of SsprStepUpRequirement from a JSON string
sspr_step_up_requirement_instance = SsprStepUpRequirement.from_json(json)
# print the JSON string representation of the object
print(SsprStepUpRequirement.to_json())

# convert the object into a dict
sspr_step_up_requirement_dict = sspr_step_up_requirement_instance.to_dict()
# create an instance of SsprStepUpRequirement from a dict
sspr_step_up_requirement_from_dict = SsprStepUpRequirement.from_dict(sspr_step_up_requirement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


