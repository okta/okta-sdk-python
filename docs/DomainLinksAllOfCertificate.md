# DomainLinksAllOfCertificate


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
from okta.models.domain_links_all_of_certificate import DomainLinksAllOfCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of DomainLinksAllOfCertificate from a JSON string
domain_links_all_of_certificate_instance = DomainLinksAllOfCertificate.from_json(json)
# print the JSON string representation of the object
print(DomainLinksAllOfCertificate.to_json())

# convert the object into a dict
domain_links_all_of_certificate_dict = domain_links_all_of_certificate_instance.to_dict()
# create an instance of DomainLinksAllOfCertificate from a dict
domain_links_all_of_certificate_from_dict = DomainLinksAllOfCertificate.from_dict(domain_links_all_of_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


