# PrivilegedResourceAccountAppResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**PrivilegedResourceCredentials**](PrivilegedResourceCredentials.md) |  | [optional] 
**profile** | **Dict[str, object]** | Specific profile properties for the privileged resource | [optional] [readonly] 

## Example

```python
from okta.models.privileged_resource_account_app_response import PrivilegedResourceAccountAppResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PrivilegedResourceAccountAppResponse from a JSON string
privileged_resource_account_app_response_instance = PrivilegedResourceAccountAppResponse.from_json(json)
# print the JSON string representation of the object
print(PrivilegedResourceAccountAppResponse.to_json())

# convert the object into a dict
privileged_resource_account_app_response_dict = privileged_resource_account_app_response_instance.to_dict()
# create an instance of PrivilegedResourceAccountAppResponse from a dict
privileged_resource_account_app_response_from_dict = PrivilegedResourceAccountAppResponse.from_dict(privileged_resource_account_app_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


