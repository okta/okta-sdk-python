# ProvisioningConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**ProvisioningConnectionProfile**](ProvisioningConnectionProfile.md) |  | 

## Example

```python
from openapi_client.models.provisioning_connection_request import ProvisioningConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningConnectionRequest from a JSON string
provisioning_connection_request_instance = ProvisioningConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(ProvisioningConnectionRequest.to_json())

# convert the object into a dict
provisioning_connection_request_dict = provisioning_connection_request_instance.to_dict()
# create an instance of ProvisioningConnectionRequest from a dict
provisioning_connection_request_form_dict = provisioning_connection_request.from_dict(provisioning_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


