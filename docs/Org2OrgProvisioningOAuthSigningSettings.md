# Org2OrgProvisioningOAuthSigningSettings

Only used for the Okta Org2Org (`okta_org2org`) app.  The signing key rotation setting.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rotation_mode** | [**ConnectionsSigningRotationMode**](ConnectionsSigningRotationMode.md) |  | 

## Example

```python
from okta.models.org2_org_provisioning_o_auth_signing_settings import Org2OrgProvisioningOAuthSigningSettings

# TODO update the JSON string below
json = "{}"
# create an instance of Org2OrgProvisioningOAuthSigningSettings from a JSON string
org2_org_provisioning_o_auth_signing_settings_instance = Org2OrgProvisioningOAuthSigningSettings.from_json(json)
# print the JSON string representation of the object
print(Org2OrgProvisioningOAuthSigningSettings.to_json())

# convert the object into a dict
org2_org_provisioning_o_auth_signing_settings_dict = org2_org_provisioning_o_auth_signing_settings_instance.to_dict()
# create an instance of Org2OrgProvisioningOAuthSigningSettings from a dict
org2_org_provisioning_o_auth_signing_settings_from_dict = Org2OrgProvisioningOAuthSigningSettings.from_dict(org2_org_provisioning_o_auth_signing_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


