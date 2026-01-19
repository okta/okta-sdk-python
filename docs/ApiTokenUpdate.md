# ApiTokenUpdate

An API Token Update Object for an Okta user. This token is NOT scoped any further and can be used for any API that the user has permissions to call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_name** | **str** | The client name associated with the API Token | [optional] [readonly] 
**created** | **datetime** | The creation date of the API Token | [optional] [readonly] 
**name** | **str** | The name associated with the API Token | [optional] 
**network** | [**ApiTokenNetwork**](ApiTokenNetwork.md) |  | [optional] 
**user_id** | **str** | The userId of the user who created the API Token | [optional] 

## Example

```python
from okta.models.api_token_update import ApiTokenUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTokenUpdate from a JSON string
api_token_update_instance = ApiTokenUpdate.from_json(json)
# print the JSON string representation of the object
print(ApiTokenUpdate.to_json())

# convert the object into a dict
api_token_update_dict = api_token_update_instance.to_dict()
# create an instance of ApiTokenUpdate from a dict
api_token_update_from_dict = ApiTokenUpdate.from_dict(api_token_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


