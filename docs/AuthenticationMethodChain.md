# AuthenticationMethodChain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_methods** | [**List[AuthenticationMethod]**](AuthenticationMethod.md) |  | [optional] 
**next** | **List[object]** | The next steps of the authentication method chain. This is an array of &#x60;AuthenticationMethodChain&#x60;. Only supports one item in the array. | [optional] 
**reauthenticate_in** | **str** | Specifies how often the user is prompted for authentication using duration format for the time period. For example, &#x60;PT2H30M&#x60; for two and a half hours. This parameter can&#39;t be set at the same time as the &#x60;reauthenticateIn&#x60; property on the &#x60;verificationMethod&#x60;. | [optional] 

## Example

```python
from okta.models.authentication_method_chain import AuthenticationMethodChain

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationMethodChain from a JSON string
authentication_method_chain_instance = AuthenticationMethodChain.from_json(json)
# print the JSON string representation of the object
print(AuthenticationMethodChain.to_json())

# convert the object into a dict
authentication_method_chain_dict = authentication_method_chain_instance.to_dict()
# create an instance of AuthenticationMethodChain from a dict
authentication_method_chain_from_dict = AuthenticationMethodChain.from_dict(authentication_method_chain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


