# AgentJsonWebKeyRsaRequest

An RSA signing key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e** | **str** | The public exponent of the RSA key, represented as a Base64URL-encoded string.  This value is used in combination with the modulus (&#x60;n&#x60;) to verify signatures and encrypt data. | [optional] 
**kty** | **str** | Cryptographic algorithm family for the certificate&#39;s key pair | 
**n** | **str** | The modulus of the RSA public key, represented as a Base64URL-encoded string.  This is the primary component of the RSA key and, with the exponent (&#x60;e&#x60;), is used for cryptographic signature verification and encryption. | [optional] 
**kid** | **str** | Unique identifier of the JSON Web Key in the AI agent&#39;s JSON Web Key Set (JWKS) | [optional] 
**status** | **str** | Status of the AI agent JSON Web Key | [optional] [default to 'ACTIVE']
**alg** | **str** | Algorithm that&#39;s used in the JSON Web Key | [optional] 
**use** | **str** | Acceptable use of the JSON Web Key  You can only use signing keys for AI agents, so the value of &#x60;use&#x60; is always &#x60;sig&#x60;. | [optional] 

## Example

```python
from okta.models.agent_json_web_key_rsa_request import AgentJsonWebKeyRsaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentJsonWebKeyRsaRequest from a JSON string
agent_json_web_key_rsa_request_instance = AgentJsonWebKeyRsaRequest.from_json(json)
# print the JSON string representation of the object
print(AgentJsonWebKeyRsaRequest.to_json())

# convert the object into a dict
agent_json_web_key_rsa_request_dict = agent_json_web_key_rsa_request_instance.to_dict()
# create an instance of AgentJsonWebKeyRsaRequest from a dict
agent_json_web_key_rsa_request_from_dict = AgentJsonWebKeyRsaRequest.from_dict(agent_json_web_key_rsa_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


