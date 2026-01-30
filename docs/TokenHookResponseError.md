# TokenHookResponseError

When an error object is returned, it causes Okta to return an OAuth 2.0 error to the requester of the token. In the error response, the value of `error` is `server_error`, and the value of `error_description` is the string that you supplied in the `errorSummary` property of the `error` object that you returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_summary** | **str** | Human-readable summary of the error. If the error object doesn&#39;t include the &#x60;errorSummary&#x60; property defined, the following common default message is returned to the end user: &#x60;The callback service returned an error&#x60;. | [optional] 

## Example

```python
from okta.models.token_hook_response_error import TokenHookResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of TokenHookResponseError from a JSON string
token_hook_response_error_instance = TokenHookResponseError.from_json(json)
# print the JSON string representation of the object
print(TokenHookResponseError.to_json())

# convert the object into a dict
token_hook_response_error_dict = token_hook_response_error_instance.to_dict()
# create an instance of TokenHookResponseError from a dict
token_hook_response_error_from_dict = TokenHookResponseError.from_dict(token_hook_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


