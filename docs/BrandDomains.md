# BrandDomains

Defines a list of domains with a subset of the properties for each domain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | [**List[DomainResponse]**](DomainResponse.md) | Each element of the array defines an individual domain | [optional] 

## Example

```python
from okta.models.brand_domains import BrandDomains

# TODO update the JSON string below
json = "{}"
# create an instance of BrandDomains from a JSON string
brand_domains_instance = BrandDomains.from_json(json)
# print the JSON string representation of the object
print(BrandDomains.to_json())

# convert the object into a dict
brand_domains_dict = brand_domains_instance.to_dict()
# create an instance of BrandDomains from a dict
brand_domains_from_dict = BrandDomains.from_dict(brand_domains_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


