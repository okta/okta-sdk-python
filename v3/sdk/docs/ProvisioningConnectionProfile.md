# ProvisioningConnectionProfile

The profile used to configure the connection method of authentication and the credentials. Currently, token-based and OAuth 2.0-based authentication are supported. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_scheme** | [**ProvisioningConnectionAuthScheme**](ProvisioningConnectionAuthScheme.md) |  | [optional] 

## Example

```python
from openapi_client.models.provisioning_connection_profile import ProvisioningConnectionProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningConnectionProfile from a JSON string
provisioning_connection_profile_instance = ProvisioningConnectionProfile.from_json(json)
# print the JSON string representation of the object
print(ProvisioningConnectionProfile.to_json())

# convert the object into a dict
provisioning_connection_profile_dict = provisioning_connection_profile_instance.to_dict()
# create an instance of ProvisioningConnectionProfile from a dict
provisioning_connection_profile_form_dict = provisioning_connection_profile.from_dict(provisioning_connection_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


