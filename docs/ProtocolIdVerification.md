# ProtocolIdVerification

Protocol settings for the IDV vendor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**IDVCredentials**](IDVCredentials.md) |  | [optional] 
**endpoints** | [**IDVEndpoints**](IDVEndpoints.md) |  | [optional] 
**scopes** | **List[str]** | IdP-defined permission bundles to request delegated access from the user. &gt; **Note:** The [identity provider type](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/IdentityProvider/#tag/IdentityProvider/operation/createIdentityProvider!path&#x3D;type&amp;t&#x3D;request) table lists the scopes that are supported for each IdP. | [optional] 
**type** | **str** | ID verification protocol | [optional] 

## Example

```python
from okta.models.protocol_id_verification import ProtocolIdVerification

# TODO update the JSON string below
json = "{}"
# create an instance of ProtocolIdVerification from a JSON string
protocol_id_verification_instance = ProtocolIdVerification.from_json(json)
# print the JSON string representation of the object
print(ProtocolIdVerification.to_json())

# convert the object into a dict
protocol_id_verification_dict = protocol_id_verification_instance.to_dict()
# create an instance of ProtocolIdVerification from a dict
protocol_id_verification_from_dict = ProtocolIdVerification.from_dict(protocol_id_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


