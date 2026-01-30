# SAMLHookResponseCommandsInnerValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** | The name of one of the supported ops: &#x60;add&#x60;:  Add a new claim to the assertion &#x60;replace&#x60;: Modify any element of the assertion  &gt; **Note:** If a response to the SAML assertion inline hook request isn&#39;t received from your external service within three seconds, a timeout occurs. In this scenario, the Okta process flow continues with the original SAML assertion returned. | [optional] 
**path** | **str** | Location, within the assertion, to apply the operation | [optional] 
**value** | [**SAMLHookResponseCommandsInnerValueInnerValue**](SAMLHookResponseCommandsInnerValueInnerValue.md) |  | [optional] 

## Example

```python
from okta.models.saml_hook_response_commands_inner_value_inner import SAMLHookResponseCommandsInnerValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLHookResponseCommandsInnerValueInner from a JSON string
saml_hook_response_commands_inner_value_inner_instance = SAMLHookResponseCommandsInnerValueInner.from_json(json)
# print the JSON string representation of the object
print(SAMLHookResponseCommandsInnerValueInner.to_json())

# convert the object into a dict
saml_hook_response_commands_inner_value_inner_dict = saml_hook_response_commands_inner_value_inner_instance.to_dict()
# create an instance of SAMLHookResponseCommandsInnerValueInner from a dict
saml_hook_response_commands_inner_value_inner_from_dict = SAMLHookResponseCommandsInnerValueInner.from_dict(saml_hook_response_commands_inner_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


