# STSServiceAccountConnectionCreatable

Create an STS connection for a service account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**IdentityAssertionAppInstanceConnectionCreatableApp**](IdentityAssertionAppInstanceConnectionCreatableApp.md) |  | 
**connection_type** | **str** | Type of connection authentication method | 
**protocol_type** | **str** | The authentication protocol type used for the connection | [optional] 
**resource_indicator** | **str** | Resource indicator used when requesting tokens. Defaults to the service account&#39;s ORN if not specified. | [optional] 
**service_account** | [**STSServiceAccountConnectionCreatableServiceAccount**](STSServiceAccountConnectionCreatableServiceAccount.md) |  | 

## Example

```python
from okta.models.sts_service_account_connection_creatable import STSServiceAccountConnectionCreatable

# TODO update the JSON string below
json = "{}"
# create an instance of STSServiceAccountConnectionCreatable from a JSON string
sts_service_account_connection_creatable_instance = STSServiceAccountConnectionCreatable.from_json(json)
# print the JSON string representation of the object
print(STSServiceAccountConnectionCreatable.to_json())

# convert the object into a dict
sts_service_account_connection_creatable_dict = sts_service_account_connection_creatable_instance.to_dict()
# create an instance of STSServiceAccountConnectionCreatable from a dict
sts_service_account_connection_creatable_from_dict = STSServiceAccountConnectionCreatable.from_dict(sts_service_account_connection_creatable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


