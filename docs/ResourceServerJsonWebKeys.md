# ResourceServerJsonWebKeys

<x-lifecycle-container><x-lifecycle class=\"ea\"></x-lifecycle></x-lifecycle-container>A [JSON Web Key Set](https://tools.ietf.org/html/rfc7517#section-5) for encrypting JWTs minted by the custom authorization server

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**List[ResourceServerJsonWebKey]**](ResourceServerJsonWebKey.md) |  | [optional] 

## Example

```python
from okta.models.resource_server_json_web_keys import ResourceServerJsonWebKeys

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceServerJsonWebKeys from a JSON string
resource_server_json_web_keys_instance = ResourceServerJsonWebKeys.from_json(json)
# print the JSON string representation of the object
print(ResourceServerJsonWebKeys.to_json())

# convert the object into a dict
resource_server_json_web_keys_dict = resource_server_json_web_keys_instance.to_dict()
# create an instance of ResourceServerJsonWebKeys from a dict
resource_server_json_web_keys_from_dict = ResourceServerJsonWebKeys.from_dict(resource_server_json_web_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


