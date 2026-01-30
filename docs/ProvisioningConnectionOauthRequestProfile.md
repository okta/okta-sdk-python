# ProvisioningConnectionOauthRequestProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_scheme** | [**ProvisioningConnectionOauthAuthScheme**](ProvisioningConnectionOauthAuthScheme.md) |  | 
**client_id** | **str** | Only used for the Okta Org2Org (&#x60;okta_org2org&#x60;) app. The unique client identifier for the OAuth 2.0 service app from the target org. | [optional] 
**settings** | [**Office365ProvisioningSettings**](Office365ProvisioningSettings.md) |  | [optional] 
**signing** | [**Org2OrgProvisioningOAuthSigningSettings**](Org2OrgProvisioningOAuthSigningSettings.md) |  | [optional] 

## Example

```python
from okta.models.provisioning_connection_oauth_request_profile import ProvisioningConnectionOauthRequestProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningConnectionOauthRequestProfile from a JSON string
provisioning_connection_oauth_request_profile_instance = ProvisioningConnectionOauthRequestProfile.from_json(json)
# print the JSON string representation of the object
print(ProvisioningConnectionOauthRequestProfile.to_json())

# convert the object into a dict
provisioning_connection_oauth_request_profile_dict = provisioning_connection_oauth_request_profile_instance.to_dict()
# create an instance of ProvisioningConnectionOauthRequestProfile from a dict
provisioning_connection_oauth_request_profile_from_dict = ProvisioningConnectionOauthRequestProfile.from_dict(provisioning_connection_oauth_request_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


