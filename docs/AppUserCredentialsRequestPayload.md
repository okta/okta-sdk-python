# AppUserCredentialsRequestPayload

Updates the assigned user credentials

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**AppUserCredentials**](AppUserCredentials.md) |  | [optional] 

## Example

```python
from okta.models.app_user_credentials_request_payload import AppUserCredentialsRequestPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AppUserCredentialsRequestPayload from a JSON string
app_user_credentials_request_payload_instance = AppUserCredentialsRequestPayload.from_json(json)
# print the JSON string representation of the object
print(AppUserCredentialsRequestPayload.to_json())

# convert the object into a dict
app_user_credentials_request_payload_dict = app_user_credentials_request_payload_instance.to_dict()
# create an instance of AppUserCredentialsRequestPayload from a dict
app_user_credentials_request_payload_from_dict = AppUserCredentialsRequestPayload.from_dict(app_user_credentials_request_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


