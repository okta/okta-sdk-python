# AppleClientSigning

Information used to generate the secret JSON Web Token for the token requests to Apple IdP > **Note:** The `privateKey` property is required for a CREATE request. For an UPDATE request, it can be null and keeps the existing value if it's null. The `privateKey` property isn't returned for LIST and GET requests or UPDATE requests if it's null.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kid** | **str** | The key ID that you obtained from Apple when you created the private key for the client | [optional] 
**private_key** | **str** | The PKCS \\#8 encoded private key that you created for the client and downloaded from Apple | [optional] 
**team_id** | **str** | The Team ID associated with your Apple developer account | [optional] 

## Example

```python
from okta.models.apple_client_signing import AppleClientSigning

# TODO update the JSON string below
json = "{}"
# create an instance of AppleClientSigning from a JSON string
apple_client_signing_instance = AppleClientSigning.from_json(json)
# print the JSON string representation of the object
print(AppleClientSigning.to_json())

# convert the object into a dict
apple_client_signing_dict = apple_client_signing_instance.to_dict()
# create an instance of AppleClientSigning from a dict
apple_client_signing_from_dict = AppleClientSigning.from_dict(apple_client_signing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


