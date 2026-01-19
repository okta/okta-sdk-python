# MtlsTrustCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | **str** | Not used | [optional] 
**issuer** | **str** | Description of the certificate issuer | [optional] 
**kid** | **str** | IdP key credential reference to the Okta X.509 signature certificate | [optional] 
**revocation** | [**MtlsTrustCredentialsRevocation**](MtlsTrustCredentialsRevocation.md) |  | [optional] 
**revocation_cache_lifetime** | **float** | Time in minutes to cache the certificate revocation information  &gt; **Note:** This property isn&#39;t supported. Okta now handles CRL caching automatically. As of October 8, 2025, in Preview orgs, and October 13, 2025, in Production orgs, this property is ignored if it&#39;s specified in any API requests. Specifying this property in your API requests doesn&#39;t cause errors since the property has no effect. &gt; &gt; See [Deprecation Notice - Smart Card IdP Legacy CRL Cache Setting](https://support.okta.com/help/s/article/deprecation-notice-smart-card-idp-legacy-crl-cache-setting?language&#x3D;en_US). | [optional] 

## Example

```python
from okta.models.mtls_trust_credentials import MtlsTrustCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of MtlsTrustCredentials from a JSON string
mtls_trust_credentials_instance = MtlsTrustCredentials.from_json(json)
# print the JSON string representation of the object
print(MtlsTrustCredentials.to_json())

# convert the object into a dict
mtls_trust_credentials_dict = mtls_trust_credentials_instance.to_dict()
# create an instance of MtlsTrustCredentials from a dict
mtls_trust_credentials_from_dict = MtlsTrustCredentials.from_dict(mtls_trust_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


