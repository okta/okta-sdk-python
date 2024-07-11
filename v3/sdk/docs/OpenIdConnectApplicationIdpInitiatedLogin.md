# OpenIdConnectApplicationIdpInitiatedLogin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_scope** | **List[str]** |  | [optional] 
**mode** | **str** |  | [optional] 

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


