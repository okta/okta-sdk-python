# ScimScimServerConfigPatch

PATCH operation options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported** | **bool** | Specifies if the PATCH operation is supported | [optional] [default to False]

## Example

```python
from okta.models.scim_scim_server_config_patch import ScimScimServerConfigPatch

# TODO update the JSON string below
json = "{}"
# create an instance of ScimScimServerConfigPatch from a JSON string
scim_scim_server_config_patch_instance = ScimScimServerConfigPatch.from_json(json)
# print the JSON string representation of the object
print(ScimScimServerConfigPatch.to_json())

# convert the object into a dict
scim_scim_server_config_patch_dict = scim_scim_server_config_patch_instance.to_dict()
# create an instance of ScimScimServerConfigPatch from a dict
scim_scim_server_config_patch_from_dict = ScimScimServerConfigPatch.from_dict(scim_scim_server_config_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


