# JsonWebKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**e** | **str** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**key_ops** | **List[str]** |  | [optional] 
**kid** | **str** |  | [optional] 
**kty** | **str** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 
**n** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**use** | **str** |  | [optional] 
**x5c** | **List[str]** |  | [optional] 
**x5t** | **str** |  | [optional] 
**x5t_s256** | **str** |  | [optional] 
**x5u** | **str** |  | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from openapi_client.models.json_web_key import JsonWebKey

# TODO update the JSON string below
json = "{}"
# create an instance of JsonWebKey from a JSON string
json_web_key_instance = JsonWebKey.from_json(json)
# print the JSON string representation of the object
print(JsonWebKey.to_json())

# convert the object into a dict
json_web_key_dict = json_web_key_instance.to_dict()
# create an instance of JsonWebKey from a dict
json_web_key_from_dict = JsonWebKey.from_dict(json_web_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


