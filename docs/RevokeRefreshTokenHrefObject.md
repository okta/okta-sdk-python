# RevokeRefreshTokenHrefObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Link URI | [optional] 

## Example

```python
from okta.models.revoke_refresh_token_href_object import RevokeRefreshTokenHrefObject

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeRefreshTokenHrefObject from a JSON string
revoke_refresh_token_href_object_instance = RevokeRefreshTokenHrefObject.from_json(json)
# print the JSON string representation of the object
print(RevokeRefreshTokenHrefObject.to_json())

# convert the object into a dict
revoke_refresh_token_href_object_dict = revoke_refresh_token_href_object_instance.to_dict()
# create an instance of RevokeRefreshTokenHrefObject from a dict
revoke_refresh_token_href_object_from_dict = RevokeRefreshTokenHrefObject.from_dict(revoke_refresh_token_href_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


