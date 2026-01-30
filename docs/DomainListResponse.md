# DomainListResponse

Defines a list of domains with a subset of the properties for each domain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | [**List[DomainResponse]**](DomainResponse.md) | Each element of the array defines an individual domain | [optional] 

## Example

```python
from okta.models.domain_list_response import DomainListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainListResponse from a JSON string
domain_list_response_instance = DomainListResponse.from_json(json)
# print the JSON string representation of the object
print(DomainListResponse.to_json())

# convert the object into a dict
domain_list_response_dict = domain_list_response_instance.to_dict()
# create an instance of DomainListResponse from a dict
domain_list_response_from_dict = DomainListResponse.from_dict(domain_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


