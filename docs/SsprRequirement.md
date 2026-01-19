# SsprRequirement

<x-lifecycle class=\"oie\"></x-lifecycle> Describes the initial and secondary authenticator requirements a user needs to reset their password

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_control** | **str** | Determines which authentication requirements a user needs to perform self-service operations. &#x60;AUTH_POLICY&#x60; defers conditions and authentication requirements to the [Okta account management policy](https://developer.okta.com/docs/guides/okta-account-management-policy/main/). &#x60;LEGACY&#x60; refers to the requirements described by this rule. | [optional] 
**primary** | [**SsprPrimaryRequirement**](SsprPrimaryRequirement.md) |  | [optional] 
**step_up** | [**SsprStepUpRequirement**](SsprStepUpRequirement.md) |  | [optional] 

## Example

```python
from okta.models.sspr_requirement import SsprRequirement

# TODO update the JSON string below
json = "{}"
# create an instance of SsprRequirement from a JSON string
sspr_requirement_instance = SsprRequirement.from_json(json)
# print the JSON string representation of the object
print(SsprRequirement.to_json())

# convert the object into a dict
sspr_requirement_dict = sspr_requirement_instance.to_dict()
# create an instance of SsprRequirement from a dict
sspr_requirement_from_dict = SsprRequirement.from_dict(sspr_requirement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


