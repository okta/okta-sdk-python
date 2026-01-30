# UserTypeLinksAllOfSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hints** | [**HrefHints**](HrefHints.md) |  | [optional] 
**href** | **str** | Link URI | 
**name** | **str** | Link name | [optional] [readonly] 
**templated** | **bool** | Indicates whether the link object&#39;s &#x60;href&#x60; property is a URI template. | [optional] [readonly] 
**type** | **str** | The media type of the link. If omitted, it is implicitly &#x60;application/json&#x60;. | [optional] [readonly] 

## Example

```python
from okta.models.user_type_links_all_of_schema import UserTypeLinksAllOfSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UserTypeLinksAllOfSchema from a JSON string
user_type_links_all_of_schema_instance = UserTypeLinksAllOfSchema.from_json(json)
# print the JSON string representation of the object
print(UserTypeLinksAllOfSchema.to_json())

# convert the object into a dict
user_type_links_all_of_schema_dict = user_type_links_all_of_schema_instance.to_dict()
# create an instance of UserTypeLinksAllOfSchema from a dict
user_type_links_all_of_schema_from_dict = UserTypeLinksAllOfSchema.from_dict(user_type_links_all_of_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


