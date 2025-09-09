# AuthorizationServer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audiences** | **List[str]** |  | [optional] 
**created** | **datetime** |  | [optional] [readonly] 
**credentials** | [**AuthorizationServerCredentials**](AuthorizationServerCredentials.md) |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**issuer** | **str** |  | [optional] 
**issuer_mode** | [**IssuerMode**](IssuerMode.md) |  | [optional] 
**last_updated** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**status** | [**LifecycleStatus**](LifecycleStatus.md) |  | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.authorization_server import AuthorizationServer

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationServer from a JSON string
authorization_server_instance = AuthorizationServer.from_json(json)
# print the JSON string representation of the object
print(AuthorizationServer.to_json())

# convert the object into a dict
authorization_server_dict = authorization_server_instance.to_dict()
# create an instance of AuthorizationServer from a dict
authorization_server_from_dict = AuthorizationServer.from_dict(authorization_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


