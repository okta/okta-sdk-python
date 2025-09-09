# DomainLinksAllOfBrand


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
from okta.models.domain_links_all_of_brand import DomainLinksAllOfBrand

# TODO update the JSON string below
json = "{}"
# create an instance of DomainLinksAllOfBrand from a JSON string
domain_links_all_of_brand_instance = DomainLinksAllOfBrand.from_json(json)
# print the JSON string representation of the object
print(DomainLinksAllOfBrand.to_json())

# convert the object into a dict
domain_links_all_of_brand_dict = domain_links_all_of_brand_instance.to_dict()
# create an instance of DomainLinksAllOfBrand from a dict
domain_links_all_of_brand_from_dict = DomainLinksAllOfBrand.from_dict(domain_links_all_of_brand_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


