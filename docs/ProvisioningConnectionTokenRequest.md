# ProvisioningConnectionTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_url** | **str** | Only used for the Zscaler 2.0 (&#x60;zscalerbyz&#x60;) app. The base URL for the Zscaler 2.0 target app, which also contains the Zscaler ID. | [optional] 
**profile** | [**ProvisioningConnectionTokenRequestProfile**](ProvisioningConnectionTokenRequestProfile.md) |  | 

## Example

```python
from okta.models.provisioning_connection_token_request import ProvisioningConnectionTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningConnectionTokenRequest from a JSON string
provisioning_connection_token_request_instance = ProvisioningConnectionTokenRequest.from_json(json)
# print the JSON string representation of the object
print(ProvisioningConnectionTokenRequest.to_json())

# convert the object into a dict
provisioning_connection_token_request_dict = provisioning_connection_token_request_instance.to_dict()
# create an instance of ProvisioningConnectionTokenRequest from a dict
provisioning_connection_token_request_from_dict = ProvisioningConnectionTokenRequest.from_dict(provisioning_connection_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


