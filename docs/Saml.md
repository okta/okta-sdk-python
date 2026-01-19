# Saml

SAML configuration details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acs** | [**List[SamlAcsInner]**](SamlAcsInner.md) | List of Assertion Consumer Service (ACS) URLs. The default ACS URL is required and is indicated by a null &#x60;index&#x60; value. You can use the org-level variables you defined in the &#x60;config&#x60; array in the URL. For example: &#x60;https://${org.subdomain}.example.com/saml/login&#x60; | 
**claims** | [**List[SamlClaimsInner]**](SamlClaimsInner.md) | Attribute statements to appear in the Okta SAML assertion | [optional] 
**doc** | **str** | The URL to your customer-facing instructions for configuring your SAML integration. See [Customer configuration document guidelines](https://developer.okta.com/docs/guides/submit-app-prereq/main/#customer-configuration-document-guidelines). | 
**entity_id** | **str** | Globally unique name for your SAML entity. For instance, your Identity Provider (IdP) or Service Provider (SP) URL. | 
**groups** | **List[str]** | Defines the group attribute names for the SAML assertion statement. Okta inserts the list of Okta user groups into the attribute names in the statement. | [optional] 

## Example

```python
from okta.models.saml import Saml

# TODO update the JSON string below
json = "{}"
# create an instance of Saml from a JSON string
saml_instance = Saml.from_json(json)
# print the JSON string representation of the object
print(Saml.to_json())

# convert the object into a dict
saml_dict = saml_instance.to_dict()
# create an instance of Saml from a dict
saml_from_dict = Saml.from_dict(saml_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


