# LinkedObjectDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | [**LinkedObjectDetailsType**](LinkedObjectDetailsType.md) |  | [optional] 

## Example

```python
from openapi_client.models.linked_object_details import LinkedObjectDetails

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedObjectDetails from a JSON string
linked_object_details_instance = LinkedObjectDetails.from_json(json)
# print the JSON string representation of the object
print(LinkedObjectDetails.to_json())

# convert the object into a dict
linked_object_details_dict = linked_object_details_instance.to_dict()
# create an instance of LinkedObjectDetails from a dict
linked_object_details_from_dict = LinkedObjectDetails.from_dict(linked_object_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


