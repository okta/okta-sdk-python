# PrivilegedResource

Base class for PrivilegedResourceRequest and PrivilegedResourceResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the object was created | [optional] [readonly] 
**credential_sync_info** | [**CredentialSyncInfo**](CredentialSyncInfo.md) |  | [optional] 
**id** | **str** | ID of the privileged resource | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the object was last updated | [optional] [readonly] 
**resource_type** | [**PrivilegedResourceType**](PrivilegedResourceType.md) |  | 
**status** | [**PrivilegedResourceStatus**](PrivilegedResourceStatus.md) |  | [optional] 

## Example

```python
from okta.models.privileged_resource import PrivilegedResource

# TODO update the JSON string below
json = "{}"
# create an instance of PrivilegedResource from a JSON string
privileged_resource_instance = PrivilegedResource.from_json(json)
# print the JSON string representation of the object
print(PrivilegedResource.to_json())

# convert the object into a dict
privileged_resource_dict = privileged_resource_instance.to_dict()
# create an instance of PrivilegedResource from a dict
privileged_resource_from_dict = PrivilegedResource.from_dict(privileged_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


