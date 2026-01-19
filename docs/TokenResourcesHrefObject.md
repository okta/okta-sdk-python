# TokenResourcesHrefObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Link URI | [optional] 

## Example

```python
from okta.models.token_resources_href_object import TokenResourcesHrefObject

# TODO update the JSON string below
json = "{}"
# create an instance of TokenResourcesHrefObject from a JSON string
token_resources_href_object_instance = TokenResourcesHrefObject.from_json(json)
# print the JSON string representation of the object
print(TokenResourcesHrefObject.to_json())

# convert the object into a dict
token_resources_href_object_dict = token_resources_href_object_instance.to_dict()
# create an instance of TokenResourcesHrefObject from a dict
token_resources_href_object_from_dict = TokenResourcesHrefObject.from_dict(token_resources_href_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


