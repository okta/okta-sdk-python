# SsprPrimaryRequirement

Defines the authenticators permitted for the initial authentication step of password recovery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**methods** | **List[str]** | Authenticator methods allowed for the initial authentication step of password recovery | [optional] 
**method_constraints** | [**List[AuthenticatorMethodConstraint]**](AuthenticatorMethodConstraint.md) | Constraints on the values specified in the &#x60;methods&#x60; array. Specifying a constraint limits methods to specific authenticator(s). Currently, Google OTP is the only accepted constraint. | [optional] 

## Example

```python
from okta.models.sspr_primary_requirement import SsprPrimaryRequirement

# TODO update the JSON string below
json = "{}"
# create an instance of SsprPrimaryRequirement from a JSON string
sspr_primary_requirement_instance = SsprPrimaryRequirement.from_json(json)
# print the JSON string representation of the object
print(SsprPrimaryRequirement.to_json())

# convert the object into a dict
sspr_primary_requirement_dict = sspr_primary_requirement_instance.to_dict()
# create an instance of SsprPrimaryRequirement from a dict
sspr_primary_requirement_from_dict = SsprPrimaryRequirement.from_dict(sspr_primary_requirement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


