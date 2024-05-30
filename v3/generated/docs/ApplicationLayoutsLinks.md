# ApplicationLayoutsLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general** | [**List[HrefObject]**](HrefObject.md) |  | [optional] 
**sign_on** | [**List[HrefObject]**](HrefObject.md) |  | [optional] 
**provisioning** | [**List[HrefObject]**](HrefObject.md) |  | [optional] 

## Example

```python
from openapi_client.models.application_layouts_links import ApplicationLayoutsLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationLayoutsLinks from a JSON string
application_layouts_links_instance = ApplicationLayoutsLinks.from_json(json)
# print the JSON string representation of the object
print(ApplicationLayoutsLinks.to_json())

# convert the object into a dict
application_layouts_links_dict = application_layouts_links_instance.to_dict()
# create an instance of ApplicationLayoutsLinks from a dict
application_layouts_links_form_dict = application_layouts_links.from_dict(application_layouts_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


