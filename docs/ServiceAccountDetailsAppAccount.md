# ServiceAccountDetailsAppAccount

Details for a SaaS app account, which will be managed as a service account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**ServiceAccountDetailsAppAccountSub**](ServiceAccountDetailsAppAccountSub.md) |  | 

## Example

```python
from okta.models.service_account_details_app_account import ServiceAccountDetailsAppAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountDetailsAppAccount from a JSON string
service_account_details_app_account_instance = ServiceAccountDetailsAppAccount.from_json(json)
# print the JSON string representation of the object
print(ServiceAccountDetailsAppAccount.to_json())

# convert the object into a dict
service_account_details_app_account_dict = service_account_details_app_account_instance.to_dict()
# create an instance of ServiceAccountDetailsAppAccount from a dict
service_account_details_app_account_from_dict = ServiceAccountDetailsAppAccount.from_dict(service_account_details_app_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


