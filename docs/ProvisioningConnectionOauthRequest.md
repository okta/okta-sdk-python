# ProvisioningConnectionOauthRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**ProvisioningConnectionOauthRequestProfile**](ProvisioningConnectionOauthRequestProfile.md) |  | 

## Example

```python
from okta.models.provisioning_connection_oauth_request import ProvisioningConnectionOauthRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningConnectionOauthRequest from a JSON string
provisioning_connection_oauth_request_instance = ProvisioningConnectionOauthRequest.from_json(json)
# print the JSON string representation of the object
print(ProvisioningConnectionOauthRequest.to_json())

# convert the object into a dict
provisioning_connection_oauth_request_dict = provisioning_connection_oauth_request_instance.to_dict()
# create an instance of ProvisioningConnectionOauthRequest from a dict
provisioning_connection_oauth_request_from_dict = ProvisioningConnectionOauthRequest.from_dict(provisioning_connection_oauth_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


