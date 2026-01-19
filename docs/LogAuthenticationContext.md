# LogAuthenticationContext

All authentication relies on validating one or more credentials that prove the authenticity of the actor's identity. Credentials are sometimes provided by the actor, as is the case with passwords, and at other times provided by a third party, and validated by the authentication provider.  The authenticationContext contains metadata about how the actor is authenticated. For example, an authenticationContext for an event, where a user authenticates with Integrated Windows Authentication (IWA), looks like the following: ``` {     \"authenticationProvider\": \"ACTIVE_DIRECTORY\",     \"authenticationStep\": 0,     \"credentialProvider\": null,     \"credentialType\": \"IWA\",     \"externalSessionId\": \"102N1EKyPFERROGvK9wizMAPQ\",     \"interface\": null,     \"issuer\": null } ``` In this case, the user enters an IWA credential to authenticate against an Active Directory instance. All of the user's future-generated events in this sign-in session are going to share the same `externalSessionId`.  Among other operations, this response object can be used to scan for suspicious sign-in activity or perform analytics on user authentication habits (for example, how often authentication scheme X is used versus authentication scheme Y).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_provider** | [**LogAuthenticationProvider**](LogAuthenticationProvider.md) |  | [optional] 
**authentication_step** | **int** | The zero-based step number in the authentication pipeline. Currently unused and always set to &#x60;0&#x60;. | [optional] [readonly] 
**credential_provider** | [**LogCredentialProvider**](LogCredentialProvider.md) |  | [optional] 
**credential_type** | [**LogCredentialType**](LogCredentialType.md) |  | [optional] 
**external_session_id** | **str** | A proxy for the actor&#39;s [session ID](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) | [optional] [readonly] 
**interface** | **str** | The third-party user interface that the actor authenticates through, if any. | [optional] [readonly] 
**issuer** | [**LogIssuer**](LogIssuer.md) |  | [optional] 

## Example

```python
from okta.models.log_authentication_context import LogAuthenticationContext

# TODO update the JSON string below
json = "{}"
# create an instance of LogAuthenticationContext from a JSON string
log_authentication_context_instance = LogAuthenticationContext.from_json(json)
# print the JSON string representation of the object
print(LogAuthenticationContext.to_json())

# convert the object into a dict
log_authentication_context_dict = log_authentication_context_instance.to_dict()
# create an instance of LogAuthenticationContext from a dict
log_authentication_context_from_dict = LogAuthenticationContext.from_dict(log_authentication_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


