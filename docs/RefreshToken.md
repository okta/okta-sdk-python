# RefreshToken

The refresh token

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jti** | **str** | The refresh token ID | [optional] 

## Example

```python
from okta.models.refresh_token import RefreshToken

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshToken from a JSON string
refresh_token_instance = RefreshToken.from_json(json)
# print the JSON string representation of the object
print(RefreshToken.to_json())

# convert the object into a dict
refresh_token_dict = refresh_token_instance.to_dict()
# create an instance of RefreshToken from a dict
refresh_token_from_dict = RefreshToken.from_dict(refresh_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


