# DomainLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**brand** | [**DomainLinksAllOfBrand**](DomainLinksAllOfBrand.md) |  | [optional] 
**certificate** | [**DomainLinksAllOfCertificate**](DomainLinksAllOfCertificate.md) |  | [optional] 
**verify** | [**DomainLinksAllOfVerify**](DomainLinksAllOfVerify.md) |  | [optional] 

## Example

```python
from openapi_client.models.domain_links import DomainLinks

# TODO update the JSON string below
json = "{}"
# create an instance of DomainLinks from a JSON string
domain_links_instance = DomainLinks.from_json(json)
# print the JSON string representation of the object
print(DomainLinks.to_json())

# convert the object into a dict
domain_links_dict = domain_links_instance.to_dict()
# create an instance of DomainLinks from a dict
domain_links_form_dict = domain_links.from_dict(domain_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


