# TokenHookResponse

For the token inline hook, the `commands` and `error` objects that you can return in the JSON payload of your response are defined in the following sections. > **Note:** The size of your response payload must be less than 256 KB.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commands** | [**List[TokenHookResponseCommandsInner]**](TokenHookResponseCommandsInner.md) | You can use the &#x60;commands&#x60; object to provide commands to Okta. It&#39;s where you can tell Okta to add more claims to the token. The &#x60;commands&#x60; object is an array, allowing you to send multiple commands. In each array element, there needs to be a &#x60;type&#x60; property and &#x60;value&#x60; property. The &#x60;type&#x60; property is where you specify which of the supported commands you want to execute, and &#x60;value&#x60; is where you supply an operand for that command. In the case of the token hook type, the &#x60;value&#x60; property is itself a nested object in which you specify a particular operation, a path to act on, and a value. | [optional] 
**error** | [**TokenHookResponseError**](TokenHookResponseError.md) |  | [optional] 

## Example

```python
from okta.models.token_hook_response import TokenHookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenHookResponse from a JSON string
token_hook_response_instance = TokenHookResponse.from_json(json)
# print the JSON string representation of the object
print(TokenHookResponse.to_json())

# convert the object into a dict
token_hook_response_dict = token_hook_response_instance.to_dict()
# create an instance of TokenHookResponse from a dict
token_hook_response_from_dict = TokenHookResponse.from_dict(token_hook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


