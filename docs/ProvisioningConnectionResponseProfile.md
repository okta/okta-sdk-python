# ProvisioningConnectionResponseProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_scheme** | [**ProvisioningConnectionAuthScheme**](ProvisioningConnectionAuthScheme.md) |  | 
**signing** | [**Org2OrgProvisioningOAuthSigningSettings**](Org2OrgProvisioningOAuthSigningSettings.md) |  | [optional] 

## Example

```python
from okta.models.provisioning_connection_response_profile import ProvisioningConnectionResponseProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningConnectionResponseProfile from a JSON string
provisioning_connection_response_profile_instance = ProvisioningConnectionResponseProfile.from_json(json)
# print the JSON string representation of the object
print(ProvisioningConnectionResponseProfile.to_json())

# convert the object into a dict
provisioning_connection_response_profile_dict = provisioning_connection_response_profile_instance.to_dict()
# create an instance of ProvisioningConnectionResponseProfile from a dict
provisioning_connection_response_profile_from_dict = ProvisioningConnectionResponseProfile.from_dict(provisioning_connection_response_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


