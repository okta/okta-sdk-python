# RotatePasswordRequest

Rotate password request for the privileged resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | The password associated with the privileged resource | 
**secret_version_id** | **str** | The version ID of the password secret from the OPA vault | 

## Example

```python
from okta.models.rotate_password_request import RotatePasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RotatePasswordRequest from a JSON string
rotate_password_request_instance = RotatePasswordRequest.from_json(json)
# print the JSON string representation of the object
print(RotatePasswordRequest.to_json())

# convert the object into a dict
rotate_password_request_dict = rotate_password_request_instance.to_dict()
# create an instance of RotatePasswordRequest from a dict
rotate_password_request_from_dict = RotatePasswordRequest.from_dict(rotate_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


