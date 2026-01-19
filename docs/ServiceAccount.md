# ServiceAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_type** | [**ServiceAccountType**](ServiceAccountType.md) |  | 
**created** | **datetime** | Timestamp when the service account was created | [optional] [readonly] 
**description** | **str** | The description of the service account | [optional] 
**id** | **str** | The UUID of the service account | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the service account was last updated | [optional] [readonly] 
**name** | **str** | The user-defined name for the service account | 
**owner_group_ids** | **List[str]** | A list of IDs of the Okta groups that own the service account | [optional] 
**owner_user_ids** | **List[str]** | A list of IDs of the Okta users that own the service account | [optional] 
**status** | [**ServiceAccountStatus**](ServiceAccountStatus.md) |  | [optional] 
**status_detail** | [**ServiceAccountStatusDetail**](ServiceAccountStatusDetail.md) |  | [optional] 

## Example

```python
from okta.models.service_account import ServiceAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccount from a JSON string
service_account_instance = ServiceAccount.from_json(json)
# print the JSON string representation of the object
print(ServiceAccount.to_json())

# convert the object into a dict
service_account_dict = service_account_instance.to_dict()
# create an instance of ServiceAccount from a dict
service_account_from_dict = ServiceAccount.from_dict(service_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


