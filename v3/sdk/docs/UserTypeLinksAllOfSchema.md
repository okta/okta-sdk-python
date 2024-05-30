# UserTypeLinksAllOfSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hints** | [**HrefObjectHints**](HrefObjectHints.md) |  | [optional] 
**href** | **str** | Link URI | 
**name** | **str** | Link name | [optional] 
**type** | **str** | The media type of the link. If omitted, it is implicitly &#x60;application/json&#x60;. | [optional] 
**templated** | **bool** | Indicates whether the Link Object&#39;s \&quot;href\&quot; property is a URI Template. | [optional] 

## Example

```python
from openapi_client.models.user_type_links_all_of_schema import UserTypeLinksAllOfSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UserTypeLinksAllOfSchema from a JSON string
user_type_links_all_of_schema_instance = UserTypeLinksAllOfSchema.from_json(json)
# print the JSON string representation of the object
print(UserTypeLinksAllOfSchema.to_json())

# convert the object into a dict
user_type_links_all_of_schema_dict = user_type_links_all_of_schema_instance.to_dict()
# create an instance of UserTypeLinksAllOfSchema from a dict
user_type_links_all_of_schema_form_dict = user_type_links_all_of_schema.from_dict(user_type_links_all_of_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


