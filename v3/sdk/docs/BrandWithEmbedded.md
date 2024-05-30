# BrandWithEmbedded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | **object** |  | [optional] [readonly] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 
**agree_to_custom_privacy_policy** | **bool** |  | [optional] 
**custom_privacy_policy_url** | **str** |  | [optional] 
**default_app** | [**DefaultApp**](DefaultApp.md) |  | [optional] 
**email_domain_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**is_default** | **bool** |  | [optional] [readonly] 
**locale** | **str** | The language specified as an [IETF BCP 47 language tag](https://datatracker.ietf.org/doc/html/rfc5646) | [optional] 
**name** | **str** |  | [optional] 
**remove_powered_by_okta** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.brand_with_embedded import BrandWithEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of BrandWithEmbedded from a JSON string
brand_with_embedded_instance = BrandWithEmbedded.from_json(json)
# print the JSON string representation of the object
print(BrandWithEmbedded.to_json())

# convert the object into a dict
brand_with_embedded_dict = brand_with_embedded_instance.to_dict()
# create an instance of BrandWithEmbedded from a dict
brand_with_embedded_form_dict = brand_with_embedded.from_dict(brand_with_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


