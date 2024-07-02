# OAuth2Actor

User that created the object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | User ID | [optional] [readonly] 
**type** | **str** | Type of user | [optional] 

## Example

```python
from openapi_client.models.o_auth2_actor import OAuth2Actor

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2Actor from a JSON string
o_auth2_actor_instance = OAuth2Actor.from_json(json)
# print the JSON string representation of the object
print(OAuth2Actor.to_json())

# convert the object into a dict
o_auth2_actor_dict = o_auth2_actor_instance.to_dict()
# create an instance of OAuth2Actor from a dict
o_auth2_actor_from_dict = OAuth2Actor.from_dict(o_auth2_actor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


