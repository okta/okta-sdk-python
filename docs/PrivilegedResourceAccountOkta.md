# PrivilegedResourceAccountOkta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The user ID associated with the Okta privileged resource | [optional] 
**credentials** | [**PrivilegedResourceCredentials**](PrivilegedResourceCredentials.md) |  | [optional] 
**profile** | **Dict[str, object]** | Specific profile properties for the privileged resource | [optional] [readonly] 

## Example

```python
from okta.models.privileged_resource_account_okta import PrivilegedResourceAccountOkta

# TODO update the JSON string below
json = "{}"
# create an instance of PrivilegedResourceAccountOkta from a JSON string
privileged_resource_account_okta_instance = PrivilegedResourceAccountOkta.from_json(json)
# print the JSON string representation of the object
print(PrivilegedResourceAccountOkta.to_json())

# convert the object into a dict
privileged_resource_account_okta_dict = privileged_resource_account_okta_instance.to_dict()
# create an instance of PrivilegedResourceAccountOkta from a dict
privileged_resource_account_okta_from_dict = PrivilegedResourceAccountOkta.from_dict(privileged_resource_account_okta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


