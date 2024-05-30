# UserTypeLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**var_schema** | [**UserTypeLinksAllOfSchema**](UserTypeLinksAllOfSchema.md) |  | [optional] 

## Example

```python
from openapi_client.models.user_type_links import UserTypeLinks

# TODO update the JSON string below
json = "{}"
# create an instance of UserTypeLinks from a JSON string
user_type_links_instance = UserTypeLinks.from_json(json)
# print the JSON string representation of the object
print(UserTypeLinks.to_json())

# convert the object into a dict
user_type_links_dict = user_type_links_instance.to_dict()
# create an instance of UserTypeLinks from a dict
user_type_links_form_dict = user_type_links.from_dict(user_type_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


