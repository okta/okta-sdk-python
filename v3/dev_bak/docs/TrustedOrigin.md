# TrustedOrigin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] [readonly] 
**created_by** | **str** |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**last_updated** | **datetime** |  | [optional] [readonly] 
**last_updated_by** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**origin** | **str** |  | [optional] 
**scopes** | [**List[TrustedOriginScope]**](TrustedOriginScope.md) |  | [optional] 
**status** | **str** |  | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from openapi_client.models.trusted_origin import TrustedOrigin

# TODO update the JSON string below
json = "{}"
# create an instance of TrustedOrigin from a JSON string
trusted_origin_instance = TrustedOrigin.from_json(json)
# print the JSON string representation of the object
print(TrustedOrigin.to_json())

# convert the object into a dict
trusted_origin_dict = trusted_origin_instance.to_dict()
# create an instance of TrustedOrigin from a dict
trusted_origin_from_dict = TrustedOrigin.from_dict(trusted_origin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


