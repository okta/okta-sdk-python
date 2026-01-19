# AuthenticationMethodChainMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chains** | [**List[AuthenticationMethodChain]**](AuthenticationMethodChain.md) | Authentication method chains. Only supports 5 items in the array. Each chain can support maximum 3 steps. | [optional] 
**reauthenticate_in** | **str** | Specifies how often the user is prompted for authentication using duration format for the time period. For example, &#x60;PT2H30M&#x60; for two and a half hours. Don&#39;t set this parameter if you&#39;re setting the &#x60;reauthenticateIn&#x60; parameter in &#x60;chains&#x60;. | [optional] 

## Example

```python
from okta.models.authentication_method_chain_method import AuthenticationMethodChainMethod

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationMethodChainMethod from a JSON string
authentication_method_chain_method_instance = AuthenticationMethodChainMethod.from_json(json)
# print the JSON string representation of the object
print(AuthenticationMethodChainMethod.to_json())

# convert the object into a dict
authentication_method_chain_method_dict = authentication_method_chain_method_instance.to_dict()
# create an instance of AuthenticationMethodChainMethod from a dict
authentication_method_chain_method_from_dict = AuthenticationMethodChainMethod.from_dict(authentication_method_chain_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


