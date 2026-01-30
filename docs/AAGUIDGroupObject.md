# AAGUIDGroupObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aaguids** | **List[str]** | A list of YubiKey hardware FIDO2 AAGUIDs. The available [AAGUIDs](https://support.yubico.com/hc/en-us/articles/360016648959-YubiKey-Hardware-FIDO2-AAGUIDs) are provided by the FIDO Alliance Metadata Service. | [optional] 
**name** | **str** | A name to identify the group of YubiKey hardware FIDO2 AAGUIDs | [optional] 

## Example

```python
from okta.models.aaguid_group_object import AAGUIDGroupObject

# TODO update the JSON string below
json = "{}"
# create an instance of AAGUIDGroupObject from a JSON string
aaguid_group_object_instance = AAGUIDGroupObject.from_json(json)
# print the JSON string representation of the object
print(AAGUIDGroupObject.to_json())

# convert the object into a dict
aaguid_group_object_dict = aaguid_group_object_instance.to_dict()
# create an instance of AAGUIDGroupObject from a dict
aaguid_group_object_from_dict = AAGUIDGroupObject.from_dict(aaguid_group_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


