# PrivilegedResourceUpdateRequest

Update request for a privileged resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | **Dict[str, object]** | Specific profile properties for the privileged resource | [optional] [readonly] 
**user_name** | **str** | The username associated with the privileged resource | [optional] 

## Example

```python
from okta.models.privileged_resource_update_request import PrivilegedResourceUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrivilegedResourceUpdateRequest from a JSON string
privileged_resource_update_request_instance = PrivilegedResourceUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PrivilegedResourceUpdateRequest.to_json())

# convert the object into a dict
privileged_resource_update_request_dict = privileged_resource_update_request_instance.to_dict()
# create an instance of PrivilegedResourceUpdateRequest from a dict
privileged_resource_update_request_from_dict = PrivilegedResourceUpdateRequest.from_dict(privileged_resource_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


