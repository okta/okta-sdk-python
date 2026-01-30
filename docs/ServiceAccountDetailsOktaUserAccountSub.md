# ServiceAccountDetailsOktaUserAccountSub

Details for managing an Okta user as a service account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**OktaUserServiceAccountCredentials**](OktaUserServiceAccountCredentials.md) |  | [optional] 
**email** | **str** | The email address for the Okta user | [optional] [readonly] 
**okta_user_id** | **str** | The ID of the Okta user to manage as a service account | 

## Example

```python
from okta.models.service_account_details_okta_user_account_sub import ServiceAccountDetailsOktaUserAccountSub

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountDetailsOktaUserAccountSub from a JSON string
service_account_details_okta_user_account_sub_instance = ServiceAccountDetailsOktaUserAccountSub.from_json(json)
# print the JSON string representation of the object
print(ServiceAccountDetailsOktaUserAccountSub.to_json())

# convert the object into a dict
service_account_details_okta_user_account_sub_dict = service_account_details_okta_user_account_sub_instance.to_dict()
# create an instance of ServiceAccountDetailsOktaUserAccountSub from a dict
service_account_details_okta_user_account_sub_from_dict = ServiceAccountDetailsOktaUserAccountSub.from_dict(service_account_details_okta_user_account_sub_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


