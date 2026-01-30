# AgentJsonWebKeyECRequest

An EC signing key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crv** | **str** | The cryptographic curve that&#39;s used for the key pair | [optional] 
**kty** | **str** | Cryptographic algorithm family for the certificate&#39;s key pair | 
**x** | **str** | The public x coordinate for the elliptic curve point | [optional] 
**y** | **str** | The public y coordinate for the elliptic curve point | [optional] 
**kid** | **str** | Unique identifier of the JSON Web Key in the AI agent&#39;s JSON Web Key Set (JWKS) | [optional] 
**status** | **str** | Status of the AI agent JSON Web Key | [optional] [default to 'ACTIVE']
**alg** | **str** | Algorithm that&#39;s used in the JSON Web Key | [optional] 
**use** | **str** | Acceptable use of the JSON Web Key  You can only use signing keys for AI agents, so the value of &#x60;use&#x60; is always &#x60;sig&#x60;. | [optional] 

## Example

```python
from okta.models.agent_json_web_key_ec_request import AgentJsonWebKeyECRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentJsonWebKeyECRequest from a JSON string
agent_json_web_key_ec_request_instance = AgentJsonWebKeyECRequest.from_json(json)
# print the JSON string representation of the object
print(AgentJsonWebKeyECRequest.to_json())

# convert the object into a dict
agent_json_web_key_ec_request_dict = agent_json_web_key_ec_request_instance.to_dict()
# create an instance of AgentJsonWebKeyECRequest from a dict
agent_json_web_key_ec_request_from_dict = AgentJsonWebKeyECRequest.from_dict(agent_json_web_key_ec_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


