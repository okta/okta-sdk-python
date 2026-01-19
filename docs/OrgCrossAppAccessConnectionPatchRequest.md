# OrgCrossAppAccessConnectionPatchRequest

Patch request object for Cross App Access Connections

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Requested value of Cross App Access connection status | 

## Example

```python
from okta.models.org_cross_app_access_connection_patch_request import OrgCrossAppAccessConnectionPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrgCrossAppAccessConnectionPatchRequest from a JSON string
org_cross_app_access_connection_patch_request_instance = OrgCrossAppAccessConnectionPatchRequest.from_json(json)
# print the JSON string representation of the object
print(OrgCrossAppAccessConnectionPatchRequest.to_json())

# convert the object into a dict
org_cross_app_access_connection_patch_request_dict = org_cross_app_access_connection_patch_request_instance.to_dict()
# create an instance of OrgCrossAppAccessConnectionPatchRequest from a dict
org_cross_app_access_connection_patch_request_from_dict = OrgCrossAppAccessConnectionPatchRequest.from_dict(org_cross_app_access_connection_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


