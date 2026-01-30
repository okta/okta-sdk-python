# BrandRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agree_to_custom_privacy_policy** | **bool** | Consent for updating the custom privacy URL. Not required when resetting the URL. | [optional] 
**custom_privacy_policy_url** | **str** | Custom privacy policy URL | [optional] 
**default_app** | [**DefaultApp**](DefaultApp.md) |  | [optional] 
**email_domain_id** | **str** | The ID of the email domain | [optional] 
**locale** | **str** | The language specified as an [IETF BCP 47 language tag](https://datatracker.ietf.org/doc/html/rfc5646) | [optional] 
**name** | **str** | The name of the brand  &gt; **Note:** You can&#39;t use the reserved &#x60;DRAPP_DOMAIN_BRAND&#x60; name. | 
**remove_powered_by_okta** | **bool** | Removes \&quot;Powered by Okta\&quot; from the sign-in page in redirect authentication deployments, and \&quot;© [current year] Okta, Inc.\&quot; from the Okta End-User Dashboard | [optional] [default to False]

## Example

```python
from okta.models.brand_request import BrandRequest

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


