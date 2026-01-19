# CredentialSyncInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** | The error code for the type of error | [optional] [readonly] 
**error_reason** | **str** | A short description of the error | [optional] [readonly] 
**secret_version_id** | **str** | The version ID of the password secret from the OPA vault. | [optional] 
**sync_state** | [**CredentialSyncState**](CredentialSyncState.md) |  | [optional] 
**sync_time** | **datetime** | Timestamp when the credential was changed | [optional] [readonly] 

## Example

```python
from okta.models.credential_sync_info import CredentialSyncInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialSyncInfo from a JSON string
credential_sync_info_instance = CredentialSyncInfo.from_json(json)
# print the JSON string representation of the object
print(CredentialSyncInfo.to_json())

# convert the object into a dict
credential_sync_info_dict = credential_sync_info_instance.to_dict()
# create an instance of CredentialSyncInfo from a dict
credential_sync_info_from_dict = CredentialSyncInfo.from_dict(credential_sync_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


