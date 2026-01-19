# BrandWithEmbedded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | **object** |  | [optional] [readonly] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 
**agree_to_custom_privacy_policy** | **bool** | Consent for updating the custom privacy URL. Not required when resetting the URL. | [optional] 
**custom_privacy_policy_url** | **str** | Custom privacy policy URL | [optional] 
**default_app** | [**DefaultApp**](DefaultApp.md) |  | [optional] 
**email_domain_id** | **str** | The ID of the email domain | [optional] 
**id** | **str** | The Brand ID | [optional] [readonly] 
**is_default** | **bool** | If &#x60;true&#x60;, the Brand is used for the Okta subdomain | [optional] [readonly] 
**locale** | **str** | The language specified as an [IETF BCP 47 language tag](https://datatracker.ietf.org/doc/html/rfc5646) | [optional] 
**name** | **str** | The name of the Brand | [optional] 
**remove_powered_by_okta** | **bool** | Removes \&quot;Powered by Okta\&quot; from the sign-in page in redirect authentication deployments, and \&quot;© [current year] Okta, Inc.\&quot; from the Okta End-User Dashboard | [optional] [default to False]

## Example

```python
from okta.models.brand_with_embedded import BrandWithEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of BrandWithEmbedded from a JSON string
brand_with_embedded_instance = BrandWithEmbedded.from_json(json)
# print the JSON string representation of the object
print(BrandWithEmbedded.to_json())

# convert the object into a dict
brand_with_embedded_dict = brand_with_embedded_instance.to_dict()
# create an instance of BrandWithEmbedded from a dict
brand_with_embedded_from_dict = BrandWithEmbedded.from_dict(brand_with_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


