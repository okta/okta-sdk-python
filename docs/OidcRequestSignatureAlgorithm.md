# OidcRequestSignatureAlgorithm

Signature Algorithm settings for signing authorization requests sent to the IdP > **Note:**  The `algorithm` property is ignored when you disable request signatures (`scope` set as `NONE`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | [**OidcSigningAlgorithm**](OidcSigningAlgorithm.md) |  | [optional] 
**scope** | [**ProtocolAlgorithmRequestScope**](ProtocolAlgorithmRequestScope.md) |  | [optional] 

## Example

```python
from okta.models.oidc_request_signature_algorithm import OidcRequestSignatureAlgorithm

# TODO update the JSON string below
json = "{}"
# create an instance of OidcRequestSignatureAlgorithm from a JSON string
oidc_request_signature_algorithm_instance = OidcRequestSignatureAlgorithm.from_json(json)
# print the JSON string representation of the object
print(OidcRequestSignatureAlgorithm.to_json())

# convert the object into a dict
oidc_request_signature_algorithm_dict = oidc_request_signature_algorithm_instance.to_dict()
# create an instance of OidcRequestSignatureAlgorithm from a dict
oidc_request_signature_algorithm_from_dict = OidcRequestSignatureAlgorithm.from_dict(oidc_request_signature_algorithm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


