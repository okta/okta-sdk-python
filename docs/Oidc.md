# Oidc

OIDC configuration details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc** | **str** | The URL to your customer-facing instructions for configuring your OIDC integration. See [Customer configuration document guidelines](https://developer.okta.com/docs/guides/submit-app-prereq/main/#customer-configuration-document-guidelines). | 
**initiate_login_uri** | **str** | The URL to redirect users when they click on your app from their Okta End-User Dashboard | [optional] 
**post_logout_uris** | **List[str]** | The sign-out redirect URIs for your app. You can send a request to &#x60;/v1/logout&#x60; to sign the user out and redirect them to one of these URIs. | [optional] 
**redirect_uris** | **List[str]** | List of sign-in redirect URIs | 

## Example

```python
from okta.models.oidc import Oidc

# TODO update the JSON string below
json = "{}"
# create an instance of Oidc from a JSON string
oidc_instance = Oidc.from_json(json)
# print the JSON string representation of the object
print(Oidc.to_json())

# convert the object into a dict
oidc_dict = oidc_instance.to_dict()
# create an instance of Oidc from a dict
oidc_from_dict = Oidc.from_dict(oidc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


