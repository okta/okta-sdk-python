# SAMLHookResponseError

An object to return an error. Returning an error causes Okta to record a failure event in the Okta System Log. The string supplied in the `errorSummary` property is recorded in the System Log event. > **Note:** If the error object doesn't include the defined `errorSummary` property, the following common default message is returned to the end user: `The callback service returned an error`.  > **Note:** If a response to a SAML inline hook request isn't received from your external service within three seconds, a timeout occurs. In this scenario, the Okta SAML inline hook process continues, and the user is created.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_summary** | **str** | A human-readable summary of the error | [optional] 

## Example

```python
from okta.models.saml_hook_response_error import SAMLHookResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLHookResponseError from a JSON string
saml_hook_response_error_instance = SAMLHookResponseError.from_json(json)
# print the JSON string representation of the object
print(SAMLHookResponseError.to_json())

# convert the object into a dict
saml_hook_response_error_dict = saml_hook_response_error_instance.to_dict()
# create an instance of SAMLHookResponseError from a dict
saml_hook_response_error_from_dict = SAMLHookResponseError.from_dict(saml_hook_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


