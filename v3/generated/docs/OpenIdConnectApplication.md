# OpenIdConnectApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**OAuthApplicationCredentials**](OAuthApplicationCredentials.md) |  | [optional] 
**name** | **str** |  | [optional] [default to 'oidc_client']
**settings** | [**OpenIdConnectApplicationSettings**](OpenIdConnectApplicationSettings.md) |  | [optional] 

## Example

```python
from openapi_client.models.open_id_connect_application import OpenIdConnectApplication

# TODO update the JSON string below
json = "{}"
# create an instance of OpenIdConnectApplication from a JSON string
open_id_connect_application_instance = OpenIdConnectApplication.from_json(json)
# print the JSON string representation of the object
print(OpenIdConnectApplication.to_json())

# convert the object into a dict
open_id_connect_application_dict = open_id_connect_application_instance.to_dict()
# create an instance of OpenIdConnectApplication from a dict
open_id_connect_application_form_dict = open_id_connect_application.from_dict(open_id_connect_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


