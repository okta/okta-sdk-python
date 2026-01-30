# ProvisioningConnectionTokenRequestProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_scheme** | [**ProvisioningConnectionTokenAuthScheme**](ProvisioningConnectionTokenAuthScheme.md) |  | 
**token** | **str** | Token used to authenticate with the app | [optional] 

## Example

```python
from okta.models.provisioning_connection_token_request_profile import ProvisioningConnectionTokenRequestProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningConnectionTokenRequestProfile from a JSON string
provisioning_connection_token_request_profile_instance = ProvisioningConnectionTokenRequestProfile.from_json(json)
# print the JSON string representation of the object
print(ProvisioningConnectionTokenRequestProfile.to_json())

# convert the object into a dict
provisioning_connection_token_request_profile_dict = provisioning_connection_token_request_profile_instance.to_dict()
# create an instance of ProvisioningConnectionTokenRequestProfile from a dict
provisioning_connection_token_request_profile_from_dict = ProvisioningConnectionTokenRequestProfile.from_dict(provisioning_connection_token_request_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


