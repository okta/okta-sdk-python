# ProvisioningConnectionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_scheme** | [**ProvisioningConnectionTokenAuthScheme**](ProvisioningConnectionTokenAuthScheme.md) |  | [optional] 
**base_url** | **str** | Base URL | [optional] 
**profile** | [**ProvisioningConnectionResponseProfile**](ProvisioningConnectionResponseProfile.md) |  | 
**status** | [**ProvisioningConnectionStatus**](ProvisioningConnectionStatus.md) |  | [default to ProvisioningConnectionStatus.DISABLED]
**links** | [**LinksSelfLifecycleAndAuthorize**](LinksSelfLifecycleAndAuthorize.md) |  | [optional] 

## Example

```python
from okta.models.provisioning_connection_response import ProvisioningConnectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningConnectionResponse from a JSON string
provisioning_connection_response_instance = ProvisioningConnectionResponse.from_json(json)
# print the JSON string representation of the object
print(ProvisioningConnectionResponse.to_json())

# convert the object into a dict
provisioning_connection_response_dict = provisioning_connection_response_instance.to_dict()
# create an instance of ProvisioningConnectionResponse from a dict
provisioning_connection_response_from_dict = ProvisioningConnectionResponse.from_dict(provisioning_connection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


