# PrivilegedResourceAccountAppRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_details** | [**AppAccountContainerDetails**](AppAccountContainerDetails.md) |  | [optional] 
**credentials** | [**PrivilegedResourceCredentials**](PrivilegedResourceCredentials.md) |  | [optional] 

## Example

```python
from okta.models.privileged_resource_account_app_request import PrivilegedResourceAccountAppRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrivilegedResourceAccountAppRequest from a JSON string
privileged_resource_account_app_request_instance = PrivilegedResourceAccountAppRequest.from_json(json)
# print the JSON string representation of the object
print(PrivilegedResourceAccountAppRequest.to_json())

# convert the object into a dict
privileged_resource_account_app_request_dict = privileged_resource_account_app_request_instance.to_dict()
# create an instance of PrivilegedResourceAccountAppRequest from a dict
privileged_resource_account_app_request_from_dict = PrivilegedResourceAccountAppRequest.from_dict(privileged_resource_account_app_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


