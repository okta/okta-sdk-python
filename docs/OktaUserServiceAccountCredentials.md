# OktaUserServiceAccountCredentials

Credentials for an Okta user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | The username associated with the service account | [optional] [readonly] 

## Example

```python
from okta.models.okta_user_service_account_credentials import OktaUserServiceAccountCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of OktaUserServiceAccountCredentials from a JSON string
okta_user_service_account_credentials_instance = OktaUserServiceAccountCredentials.from_json(json)
# print the JSON string representation of the object
print(OktaUserServiceAccountCredentials.to_json())

# convert the object into a dict
okta_user_service_account_credentials_dict = okta_user_service_account_credentials_instance.to_dict()
# create an instance of OktaUserServiceAccountCredentials from a dict
okta_user_service_account_credentials_from_dict = OktaUserServiceAccountCredentials.from_dict(okta_user_service_account_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


