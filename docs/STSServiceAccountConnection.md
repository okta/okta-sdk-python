# STSServiceAccountConnection

STS connection to a service account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**ManagedConnectionAppInstance**](ManagedConnectionAppInstance.md) |  | 
**connection_type** | **str** | Type of connection authentication method | 
**id** | **str** | Unique identifier for the managed connection. Only present for managed connections. | [optional] 
**orn** | **str** | The [ORN](https://developer.okta.com/docs/api/openapi/okta-management/guides/roles/#okta-resource-name-orn) of the managed connection | [optional] 
**protocol_type** | **str** | The authentication protocol type used for the connection | [optional] 
**resource_indicator** | **str** | Resource indicator used when requesting tokens. | 
**service_account** | [**ManagedConnectionServiceAccount**](ManagedConnectionServiceAccount.md) |  | 
**status** | [**ManagedConnectionStatus**](ManagedConnectionStatus.md) |  | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.sts_service_account_connection import STSServiceAccountConnection

# TODO update the JSON string below
json = "{}"
# create an instance of STSServiceAccountConnection from a JSON string
sts_service_account_connection_instance = STSServiceAccountConnection.from_json(json)
# print the JSON string representation of the object
print(STSServiceAccountConnection.to_json())

# convert the object into a dict
sts_service_account_connection_dict = sts_service_account_connection_instance.to_dict()
# create an instance of STSServiceAccountConnection from a dict
sts_service_account_connection_from_dict = STSServiceAccountConnection.from_dict(sts_service_account_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


