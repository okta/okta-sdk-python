# CatalogApplicationLinks

Specifies link relations (see [Web Linking](https://www.rfc-editor.org/rfc/rfc8288)) available using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logo** | [**List[HrefObjectLogoLink]**](HrefObjectLogoLink.md) | List of app logo resources | [optional] 
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 

## Example

```python
from okta.models.catalog_application_links import CatalogApplicationLinks

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogApplicationLinks from a JSON string
catalog_application_links_instance = CatalogApplicationLinks.from_json(json)
# print the JSON string representation of the object
print(CatalogApplicationLinks.to_json())

# convert the object into a dict
catalog_application_links_dict = catalog_application_links_instance.to_dict()
# create an instance of CatalogApplicationLinks from a dict
catalog_application_links_from_dict = CatalogApplicationLinks.from_dict(catalog_application_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


