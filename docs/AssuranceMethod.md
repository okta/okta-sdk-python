# AssuranceMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraints** | [**List[AccessPolicyConstraints]**](AccessPolicyConstraints.md) | Specifies constraints for the authenticator. Constraints are logically evaluated such that only one constraint object needs to be satisfied. But, within a constraint object, each constraint property must be satisfied. | [optional] 
**factor_mode** | [**AssuranceMethodFactorMode**](AssuranceMethodFactorMode.md) |  | [optional] 
**inactivity_period** | **str** | The inactivity duration after which the user must re-authenticate. Use the ISO 8601 period format (for example, PT2H). | [optional] 
**reauthenticate_in** | **str** | The duration after which the user must re-authenticate, regardless of user activity. Keep in mind that the re-authentication intervals for constraints take precedent over this value. Use the ISO 8601 period format for recurring time intervals (for example, PT2H, PT0S, PT43800H, and so on). | [optional] 

## Example

```python
from okta.models.assurance_method import AssuranceMethod

# TODO update the JSON string below
json = "{}"
# create an instance of AssuranceMethod from a JSON string
assurance_method_instance = AssuranceMethod.from_json(json)
# print the JSON string representation of the object
print(AssuranceMethod.to_json())

# convert the object into a dict
assurance_method_dict = assurance_method_instance.to_dict()
# create an instance of AssuranceMethod from a dict
assurance_method_from_dict = AssuranceMethod.from_dict(assurance_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


