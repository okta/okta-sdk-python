# OpenIdConnectApplicationIdpInitiatedLogin

The type of IdP-initiated sign-in flow that the client supports

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_scope** | **List[str]** | The scopes to use for the request when &#x60;mode&#x60; is &#x60;OKTA&#x60; | [optional] 
**mode** | **str** | The mode to use for the IdP-initiated sign-in flow. For &#x60;OKTA&#x60; or &#x60;SPEC&#x60; modes, the client must have an &#x60;initiate_login_uri&#x60; registered. &gt; **Note:** For web and SPA apps, if the mode is &#x60;SPEC&#x60; or &#x60;OKTA&#x60;, you must set &#x60;grant_types&#x60; to &#x60;authorization_code&#x60;, &#x60;implicit&#x60;, or &#x60;interaction_code&#x60;.  | 

## Example

```python
from okta.models.open_id_connect_application_idp_initiated_login import OpenIdConnectApplicationIdpInitiatedLogin

# TODO update the JSON string below
json = "{}"
# create an instance of OpenIdConnectApplicationIdpInitiatedLogin from a JSON string
open_id_connect_application_idp_initiated_login_instance = OpenIdConnectApplicationIdpInitiatedLogin.from_json(json)
# print the JSON string representation of the object
print(OpenIdConnectApplicationIdpInitiatedLogin.to_json())

# convert the object into a dict
open_id_connect_application_idp_initiated_login_dict = open_id_connect_application_idp_initiated_login_instance.to_dict()
# create an instance of OpenIdConnectApplicationIdpInitiatedLogin from a dict
open_id_connect_application_idp_initiated_login_from_dict = OpenIdConnectApplicationIdpInitiatedLogin.from_dict(open_id_connect_application_idp_initiated_login_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


