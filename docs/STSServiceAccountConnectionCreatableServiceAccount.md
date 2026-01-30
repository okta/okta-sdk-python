# STSServiceAccountConnectionCreatableServiceAccount

Reference to a service account in [ORN](/openapi/okta-management/guides/roles/#okta-resource-name-orn) format

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orn** | **str** | The [ORN](https://developer.okta.com/docs/api/openapi/okta-management/guides/roles/#okta-resource-name-orn) of the service account | 

## Example

```python
from okta.models.sts_service_account_connection_creatable_service_account import STSServiceAccountConnectionCreatableServiceAccount

# TODO update the JSON string below
json = "{}"
# create an instance of STSServiceAccountConnectionCreatableServiceAccount from a JSON string
sts_service_account_connection_creatable_service_account_instance = STSServiceAccountConnectionCreatableServiceAccount.from_json(json)
# print the JSON string representation of the object
print(STSServiceAccountConnectionCreatableServiceAccount.to_json())

# convert the object into a dict
sts_service_account_connection_creatable_service_account_dict = sts_service_account_connection_creatable_service_account_instance.to_dict()
# create an instance of STSServiceAccountConnectionCreatableServiceAccount from a dict
sts_service_account_connection_creatable_service_account_from_dict = STSServiceAccountConnectionCreatableServiceAccount.from_dict(sts_service_account_connection_creatable_service_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


