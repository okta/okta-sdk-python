# BaseTokenTokenLifetime

Lifetime of the token

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiration** | **int** | Time in seconds until the token expires | [optional] 

## Example

```python
from okta.models.base_token_token_lifetime import BaseTokenTokenLifetime

# TODO update the JSON string below
json = "{}"
# create an instance of BaseTokenTokenLifetime from a JSON string
base_token_token_lifetime_instance = BaseTokenTokenLifetime.from_json(json)
# print the JSON string representation of the object
print(BaseTokenTokenLifetime.to_json())

# convert the object into a dict
base_token_token_lifetime_dict = base_token_token_lifetime_instance.to_dict()
# create an instance of BaseTokenTokenLifetime from a dict
base_token_token_lifetime_from_dict = BaseTokenTokenLifetime.from_dict(base_token_token_lifetime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


