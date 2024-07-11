# ProvisioningConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_scheme** | [**ProvisioningConnectionAuthScheme**](ProvisioningConnectionAuthScheme.md) |  | 
**profile** | [**ProvisioningConnectionProfile**](ProvisioningConnectionProfile.md) |  | [optional] 
**status** | [**ProvisioningConnectionStatus**](ProvisioningConnectionStatus.md) |  | [default to ProvisioningConnectionStatus.DISABLED]
**links** | [**LinksSelfAndLifecycle**](LinksSelfAndLifecycle.md) |  | [optional] 

## Example

```python
from okta.models.provisioning_connection import ProvisioningConnection

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningConnection from a JSON string
provisioning_connection_instance = ProvisioningConnection.from_json(json)
# print the JSON string representation of the object
print(ProvisioningConnection.to_json())

# convert the object into a dict
provisioning_connection_dict = provisioning_connection_instance.to_dict()
# create an instance of ProvisioningConnection from a dict
provisioning_connection_from_dict = ProvisioningConnection.from_dict(provisioning_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


