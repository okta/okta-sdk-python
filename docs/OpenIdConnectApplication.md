# OpenIdConnectApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**OAuthApplicationCredentials**](OAuthApplicationCredentials.md) |  | 
**name** | **str** | &#x60;oidc_client&#x60; is the key name for an OAuth 2.0 client app instance | [default to 'oidc_client']
**settings** | [**OpenIdConnectApplicationSettings**](OpenIdConnectApplicationSettings.md) |  | 

## Example

```python
from okta.models.open_id_connect_application import OpenIdConnectApplication

# TODO update the JSON string below
json = "{}"
# create an instance of OpenIdConnectApplication from a JSON string
open_id_connect_application_instance = OpenIdConnectApplication.from_json(json)
# print the JSON string representation of the object
print(OpenIdConnectApplication.to_json())

# convert the object into a dict
open_id_connect_application_dict = open_id_connect_application_instance.to_dict()
# create an instance of OpenIdConnectApplication from a dict
open_id_connect_application_from_dict = OpenIdConnectApplication.from_dict(open_id_connect_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


