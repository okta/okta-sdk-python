# IdentitySourceSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**identity_source_id** | **str** |  | [optional] [readonly] 
**import_type** | **str** |  | [optional] [readonly] 
**last_updated** | **datetime** |  | [optional] [readonly] 
**status** | [**IdentitySourceSessionStatus**](IdentitySourceSessionStatus.md) |  | [optional] 

## Example

```python
from okta.models.identity_source_session import IdentitySourceSession

# TODO update the JSON string below
json = "{}"
# create an instance of IdentitySourceSession from a JSON string
identity_source_session_instance = IdentitySourceSession.from_json(json)
# print the JSON string representation of the object
print(IdentitySourceSession.to_json())

# convert the object into a dict
identity_source_session_dict = identity_source_session_instance.to_dict()
# create an instance of IdentitySourceSession from a dict
identity_source_session_from_dict = IdentitySourceSession.from_dict(identity_source_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


