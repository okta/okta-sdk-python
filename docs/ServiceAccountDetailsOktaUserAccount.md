# ServiceAccountDetailsOktaUserAccount

Details for managing an Okta user as a service account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**ServiceAccountDetailsOktaUserAccountSub**](ServiceAccountDetailsOktaUserAccountSub.md) |  | 

## Example

```python
from okta.models.service_account_details_okta_user_account import ServiceAccountDetailsOktaUserAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountDetailsOktaUserAccount from a JSON string
service_account_details_okta_user_account_instance = ServiceAccountDetailsOktaUserAccount.from_json(json)
# print the JSON string representation of the object
print(ServiceAccountDetailsOktaUserAccount.to_json())

# convert the object into a dict
service_account_details_okta_user_account_dict = service_account_details_okta_user_account_instance.to_dict()
# create an instance of ServiceAccountDetailsOktaUserAccount from a dict
service_account_details_okta_user_account_from_dict = ServiceAccountDetailsOktaUserAccount.from_dict(service_account_details_okta_user_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


