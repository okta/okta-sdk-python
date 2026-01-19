# IdentitySourceSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | The timestamp when the identity source session was created | [optional] [readonly] 
**id** | **str** | The ID of the identity source session | [optional] [readonly] 
**identity_source_id** | **str** | The ID of the custom identity source for which the session is created | [optional] [readonly] 
**import_type** | **str** | The type of import.  All imports are &#x60;INCREMENTAL&#x60; imports. | [optional] [readonly] 
**last_updated** | **datetime** | The timestamp when the identity source session was created | [optional] [readonly] 
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


