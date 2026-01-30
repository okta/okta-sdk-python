# BaseTokenToken

The token

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lifetime** | [**BaseTokenTokenLifetime**](BaseTokenTokenLifetime.md) |  | [optional] 

## Example

```python
from okta.models.base_token_token import BaseTokenToken

# TODO update the JSON string below
json = "{}"
# create an instance of BaseTokenToken from a JSON string
base_token_token_instance = BaseTokenToken.from_json(json)
# print the JSON string representation of the object
print(BaseTokenToken.to_json())

# convert the object into a dict
base_token_token_dict = base_token_token_instance.to_dict()
# create an instance of BaseTokenToken from a dict
base_token_token_from_dict = BaseTokenToken.from_dict(base_token_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


