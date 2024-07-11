# BrandRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agree_to_custom_privacy_policy** | **bool** |  | [optional] 
**custom_privacy_policy_url** | **str** |  | [optional] 
**default_app** | [**DefaultApp**](DefaultApp.md) |  | [optional] 
**email_domain_id** | **str** |  | [optional] 
**locale** | **str** | The language specified as an [IETF BCP 47 language tag](https://datatracker.ietf.org/doc/html/rfc5646) | [optional] 
**name** | **str** |  | [optional] 
**remove_powered_by_okta** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.brand_request import BrandRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BrandRequest from a JSON string
brand_request_instance = BrandRequest.from_json(json)
# print the JSON string representation of the object
print(BrandRequest.to_json())

# convert the object into a dict
brand_request_dict = brand_request_instance.to_dict()
# create an instance of BrandRequest from a dict
brand_request_from_dict = BrandRequest.from_dict(brand_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


