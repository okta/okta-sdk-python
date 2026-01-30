# SAMLHookResponseCommandsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | One of the supported commands &#x60;com.okta.assertion.patch&#x60; | [optional] 
**value** | [**List[SAMLHookResponseCommandsInnerValueInner]**](SAMLHookResponseCommandsInnerValueInner.md) |  | [optional] 

## Example

```python
from okta.models.saml_hook_response_commands_inner import SAMLHookResponseCommandsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLHookResponseCommandsInner from a JSON string
saml_hook_response_commands_inner_instance = SAMLHookResponseCommandsInner.from_json(json)
# print the JSON string representation of the object
print(SAMLHookResponseCommandsInner.to_json())

# convert the object into a dict
saml_hook_response_commands_inner_dict = saml_hook_response_commands_inner_instance.to_dict()
# create an instance of SAMLHookResponseCommandsInner from a dict
saml_hook_response_commands_inner_from_dict = SAMLHookResponseCommandsInner.from_dict(saml_hook_response_commands_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


