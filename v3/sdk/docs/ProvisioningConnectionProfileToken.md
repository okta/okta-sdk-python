# ProvisioningConnectionProfileToken

The app provisioning connection profile used to configure the method of authentication and the credentials. Currently, token-based and OAuth 2.0-based authentication are supported. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Token used to authenticate with the app | 

## Example

```python
from openapi_client.models.provisioning_connection_profile_token import ProvisioningConnectionProfileToken

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningConnectionProfileToken from a JSON string
provisioning_connection_profile_token_instance = ProvisioningConnectionProfileToken.from_json(json)
# print the JSON string representation of the object
print(ProvisioningConnectionProfileToken.to_json())

# convert the object into a dict
provisioning_connection_profile_token_dict = provisioning_connection_profile_token_instance.to_dict()
# create an instance of ProvisioningConnectionProfileToken from a dict
provisioning_connection_profile_token_form_dict = provisioning_connection_profile_token.from_dict(provisioning_connection_profile_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


