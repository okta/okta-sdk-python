# LogAuthenticationContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_provider** | [**LogAuthenticationProvider**](LogAuthenticationProvider.md) |  | [optional] 
**authentication_step** | **int** |  | [optional] [readonly] 
**credential_provider** | [**LogCredentialProvider**](LogCredentialProvider.md) |  | [optional] 
**credential_type** | [**LogCredentialType**](LogCredentialType.md) |  | [optional] 
**external_session_id** | **str** |  | [optional] [readonly] 
**interface** | **str** |  | [optional] [readonly] 
**issuer** | [**LogIssuer**](LogIssuer.md) |  | [optional] 

## Example

```python
from openapi_client.models.log_authentication_context import LogAuthenticationContext

# TODO update the JSON string below
json = "{}"
# create an instance of LogAuthenticationContext from a JSON string
log_authentication_context_instance = LogAuthenticationContext.from_json(json)
# print the JSON string representation of the object
print(LogAuthenticationContext.to_json())

# convert the object into a dict
log_authentication_context_dict = log_authentication_context_instance.to_dict()
# create an instance of LogAuthenticationContext from a dict
log_authentication_context_form_dict = log_authentication_context.from_dict(log_authentication_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


