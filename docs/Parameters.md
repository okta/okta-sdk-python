# Parameters

Attributes used for processing Active Directory group membership update

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The update action to take | [optional] 
**attribute** | **str** | The attribute that tracks group memberships in Active Directory. For Active Directory, use &#x60;member&#x60;. | [optional] 
**values** | **List[str]** | List of user IDs whose group memberships to update | [optional] 

## Example

```python
from okta.models.parameters import Parameters

# TODO update the JSON string below
json = "{}"
# create an instance of Parameters from a JSON string
parameters_instance = Parameters.from_json(json)
# print the JSON string representation of the object
print(Parameters.to_json())

# convert the object into a dict
parameters_dict = parameters_instance.to_dict()
# create an instance of Parameters from a dict
parameters_from_dict = Parameters.from_dict(parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


