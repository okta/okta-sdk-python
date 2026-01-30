# Scim

SCIM configuration details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_mode** | **str** | The authentication mode for requests to your SCIM server  | authMode | Description | | -------- | ----------- | | &#x60;header&#x60; | Uses authorization header with a customer-provided token value in the following format: &#x60;Authorization: {API token}&#x60; | | &#x60;bearer&#x60; | Uses authorization header with a customer-provided bearer token in the following format: &#x60;Authorization: Bearer {API token}&#x60; | | {authModeId} | The ID of the auth mode object that contains OAuth 2.0 credentials. &lt;br&gt; **Note:** Use the &#x60;/integrations/api/v1/internal/authModes&#x60; endpoint to create the auth mode object. | | 
**base_uri** | **str** | The base URL that Okta uses to send outbound calls to your SCIM server. Only the HTTPS protocol is supported. You can use the app-level variables defined in the &#x60;config&#x60; array for the base URL. For example, if you have a &#x60;subdomain&#x60; variable defined in the &#x60;config&#x60; array and the URL to retrieve SCIM users for your integration is &#x60;https://${subdomain}.example.com/scim/v2/Users&#x60;, then specify the following base URL: &#x60;&#39;https://&#39; + app.subdomain + &#39;.example.com/scim/v2&#39;&#x60;. | 
**entitlement_types** | [**List[EntitlementTypesInner]**](EntitlementTypesInner.md) | List of supported entitlement types | [optional] 
**scim_server_config** | [**ScimScimServerConfig**](ScimScimServerConfig.md) |  | 
**setup_instructions_uri** | **str** | The URL to your customer-facing instructions for configuring your SCIM integration. See [Customer configuration document guidelines](https://developer.okta.com/docs/guides/submit-app-prereq/main/#customer-configuration-document-guidelines). | 

## Example

```python
from okta.models.scim import Scim

# TODO update the JSON string below
json = "{}"
# create an instance of Scim from a JSON string
scim_instance = Scim.from_json(json)
# print the JSON string representation of the object
print(Scim.to_json())

# convert the object into a dict
scim_dict = scim_instance.to_dict()
# create an instance of Scim from a dict
scim_from_dict = Scim.from_dict(scim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


