# TokenHookResponseCommandsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | One of the supported commands:   &#x60;com.okta.identity.patch&#x60;: Modify an ID token   &#x60;com.okta.access.patch&#x60;: Modify an access token &gt; **Note:** The &#x60;commands&#x60; array should only contain commands that can be applied to the requested tokens. For example, if only an ID token is requested, the &#x60;commands&#x60; array shouldn&#39;t contain commands of the type &#x60;com.okta.access.patch&#x60;. | [optional] 
**value** | [**List[TokenHookResponseCommandsInnerValueInner]**](TokenHookResponseCommandsInnerValueInner.md) | The &#x60;value&#x60; object is where you specify the operation to perform. It&#39;s an array, which allows you to request more than one operation. | [optional] 

## Example

```python
from okta.models.token_hook_response_commands_inner import TokenHookResponseCommandsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TokenHookResponseCommandsInner from a JSON string
token_hook_response_commands_inner_instance = TokenHookResponseCommandsInner.from_json(json)
# print the JSON string representation of the object
print(TokenHookResponseCommandsInner.to_json())

# convert the object into a dict
token_hook_response_commands_inner_dict = token_hook_response_commands_inner_instance.to_dict()
# create an instance of TokenHookResponseCommandsInner from a dict
token_hook_response_commands_inner_from_dict = TokenHookResponseCommandsInner.from_dict(token_hook_response_commands_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


