# LinksUserRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**HrefObjectUserLink**](HrefObjectUserLink.md) |  | [optional] 

## Example

```python
from okta.models.links_user_ref import LinksUserRef

# TODO update the JSON string below
json = "{}"
# create an instance of LinksUserRef from a JSON string
links_user_ref_instance = LinksUserRef.from_json(json)
# print the JSON string representation of the object
print(LinksUserRef.to_json())

# convert the object into a dict
links_user_ref_dict = links_user_ref_instance.to_dict()
# create an instance of LinksUserRef from a dict
links_user_ref_from_dict = LinksUserRef.from_dict(links_user_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


