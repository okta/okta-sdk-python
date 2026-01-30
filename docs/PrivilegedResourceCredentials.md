# PrivilegedResourceCredentials

Credentials for the privileged resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | The password associated with the privileged resource | [optional] 
**user_name** | **str** | The username associated with the privileged resource | 

## Example

```python
from okta.models.privileged_resource_credentials import PrivilegedResourceCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of PrivilegedResourceCredentials from a JSON string
privileged_resource_credentials_instance = PrivilegedResourceCredentials.from_json(json)
# print the JSON string representation of the object
print(PrivilegedResourceCredentials.to_json())

# convert the object into a dict
privileged_resource_credentials_dict = privileged_resource_credentials_instance.to_dict()
# create an instance of PrivilegedResourceCredentials from a dict
privileged_resource_credentials_from_dict = PrivilegedResourceCredentials.from_dict(privileged_resource_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


