# SAMLHookResponseCommandsInnerValueInnerValue

The value of the claim that you add or replace, and can also include other attributes. If adding to a claim, add another `value` attribute residing within an array called `attributeValues`.  See the following examples:  #### Simple value (integer or string)  `\"value\": 300` or `\"value\": \"replacementString\"`  #### Attribute value (object)  ` \"value\": {     \"authContextClassRef\": \"replacementValue\"   }`  #### AttributeValues array value (object)  ` \"value\": {     \"attributes\": {       \"NameFormat\": \"urn:oasis:names:tc:SAML:2.0:attrname-format:basic\"     },     \"attributeValues\": [       {\"attributes\": {         \"xsi:type\": \"xs:string\"       },       \"value\": \"4321\"}       ]     }`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from okta.models.saml_hook_response_commands_inner_value_inner_value import SAMLHookResponseCommandsInnerValueInnerValue

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLHookResponseCommandsInnerValueInnerValue from a JSON string
saml_hook_response_commands_inner_value_inner_value_instance = SAMLHookResponseCommandsInnerValueInnerValue.from_json(json)
# print the JSON string representation of the object
print(SAMLHookResponseCommandsInnerValueInnerValue.to_json())

# convert the object into a dict
saml_hook_response_commands_inner_value_inner_value_dict = saml_hook_response_commands_inner_value_inner_value_instance.to_dict()
# create an instance of SAMLHookResponseCommandsInnerValueInnerValue from a dict
saml_hook_response_commands_inner_value_inner_value_from_dict = SAMLHookResponseCommandsInnerValueInnerValue.from_dict(saml_hook_response_commands_inner_value_inner_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


