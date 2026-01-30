# IdentityProviderProperties

The properties in the IdP `properties` object vary depending on the IdP type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aal_value** | **str** | The [authentication assurance level](https://developers.login.gov/oidc/#aal-values) (AAL) value for the Login.gov IdP. See [Add a Login.gov IdP](https://developer.okta.com/docs/guides/add-logingov-idp/). Applies to &#x60;LOGINGOV&#x60; and &#x60;LOGINGOV_SANDBOX&#x60; IdP types. | [optional] 
**additional_amr** | **List[str]** | The additional Assurance Methods References (AMR) values for Smart Card IdPs. Applies to &#x60;X509&#x60; IdP type. | [optional] 
**ial_value** | **str** | The [type of identity verification](https://developers.login.gov/oidc/#ial-values) (IAL) value for the Login.gov IdP. See [Add a Login.gov IdP](https://developer.okta.com/docs/guides/add-logingov-idp/). Applies to &#x60;LOGINGOV&#x60; and &#x60;LOGINGOV_SANDBOX&#x60; IdP types. | [optional] 
**idv_metadata** | [**IdentityProviderPropertiesIdvMetadata**](IdentityProviderPropertiesIdvMetadata.md) |  | [optional] 
**inquiry_template_id** | **str** | The ID of the inquiry template from your Persona dashboard. The inquiry template always starts with &#x60;itmpl&#x60;. Applies to the &#x60;IDV_PERSONA&#x60; IdP type. | 

## Example

```python
from okta.models.identity_provider_properties import IdentityProviderProperties

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProviderProperties from a JSON string
identity_provider_properties_instance = IdentityProviderProperties.from_json(json)
# print the JSON string representation of the object
print(IdentityProviderProperties.to_json())

# convert the object into a dict
identity_provider_properties_dict = identity_provider_properties_instance.to_dict()
# create an instance of IdentityProviderProperties from a dict
identity_provider_properties_from_dict = IdentityProviderProperties.from_dict(identity_provider_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


