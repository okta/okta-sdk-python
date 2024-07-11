# LinkedObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated** | [**LinkedObjectDetails**](LinkedObjectDetails.md) |  | [optional] 
**primary** | [**LinkedObjectDetails**](LinkedObjectDetails.md) |  | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.linked_object import LinkedObject

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedObject from a JSON string
linked_object_instance = LinkedObject.from_json(json)
# print the JSON string representation of the object
print(LinkedObject.to_json())

# convert the object into a dict
linked_object_dict = linked_object_instance.to_dict()
# create an instance of LinkedObject from a dict
linked_object_from_dict = LinkedObject.from_dict(linked_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


