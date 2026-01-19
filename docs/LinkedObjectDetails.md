# LinkedObjectDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the &#x60;primary&#x60; or the &#x60;associated&#x60; relationship | [optional] 
**name** | **str** | API name of the &#x60;primary&#x60; or the &#x60;associated&#x60; link. The &#x60;name&#x60; parameter can&#39;t start with a number and can only contain the following characters: &#x60;a-z&#x60;, &#x60;A-Z&#x60;,&#x60; 0-9&#x60;, and &#x60;_&#x60;. | 
**title** | **str** | Display name of the &#x60;primary&#x60; or the &#x60;associated&#x60; link | 
**type** | [**LinkedObjectDetailsType**](LinkedObjectDetailsType.md) |  | 

## Example

```python
from okta.models.linked_object_details import LinkedObjectDetails

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


