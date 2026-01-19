# SAMLHookResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commands** | [**List[SAMLHookResponseCommandsInner]**](SAMLHookResponseCommandsInner.md) | The &#x60;commands&#x60; object is where you tell Okta to add additional claims to the assertion or to modify the existing assertion statements.  &#x60;commands&#x60; is an array, allowing you to send multiple commands. In each array element, include a &#x60;type&#x60; property and a &#x60;value&#x60; property. The &#x60;type&#x60; property is where you specify which of the supported commands you want to execute, and &#x60;value&#x60; is where you supply an operand for that command. In the case of the SAML assertion inline hook, the &#x60;value&#x60; property is itself a nested object, in which you specify a particular operation, a path to act on, and a value. | [optional] 
**error** | [**SAMLHookResponseError**](SAMLHookResponseError.md) |  | [optional] 

## Example

```python
from okta.models.saml_hook_response import SAMLHookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLHookResponse from a JSON string
saml_hook_response_instance = SAMLHookResponse.from_json(json)
# print the JSON string representation of the object
print(SAMLHookResponse.to_json())

# convert the object into a dict
saml_hook_response_dict = saml_hook_response_instance.to_dict()
# create an instance of SAMLHookResponse from a dict
saml_hook_response_from_dict = SAMLHookResponse.from_dict(saml_hook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


