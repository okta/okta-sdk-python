# ProvisioningConnectionProfileOauth

The app provisioning connection profile used to configure the method of authentication and the credentials. Currently, token-based and OAuth 2.0-based authentication are supported. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_scheme** | [**ProvisioningConnectionOauthAuthScheme**](ProvisioningConnectionOauthAuthScheme.md) |  | 
**client_id** | **str** |  | [optional] 

## Example

```python
from okta.models.provisioning_connection_profile_oauth import ProvisioningConnectionProfileOauth

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningConnectionProfileOauth from a JSON string
provisioning_connection_profile_oauth_instance = ProvisioningConnectionProfileOauth.from_json(json)
# print the JSON string representation of the object
print(ProvisioningConnectionProfileOauth.to_json())

# convert the object into a dict
provisioning_connection_profile_oauth_dict = provisioning_connection_profile_oauth_instance.to_dict()
# create an instance of ProvisioningConnectionProfileOauth from a dict
provisioning_connection_profile_oauth_from_dict = ProvisioningConnectionProfileOauth.from_dict(provisioning_connection_profile_oauth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


