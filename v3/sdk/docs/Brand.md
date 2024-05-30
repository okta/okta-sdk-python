# Brand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from openapi_client.models.brand import Brand

# TODO update the JSON string below
json = "{}"
# create an instance of Brand from a JSON string
brand_instance = Brand.from_json(json)
# print the JSON string representation of the object
print(Brand.to_json())

# convert the object into a dict
brand_dict = brand_instance.to_dict()
# create an instance of Brand from a dict
brand_form_dict = brand.from_dict(brand_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


