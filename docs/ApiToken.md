# ApiToken

An API token for an Okta User. This token is NOT scoped any further and can be used for any API the user has permissions to call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_name** | **str** |  | [optional] [readonly] 
**created** | **datetime** |  | [optional] [readonly] 
**expires_at** | **datetime** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**last_updated** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | 
**network** | [**ApiTokenNetwork**](ApiTokenNetwork.md) |  | [optional] 
**token_window** | **str** | A time duration specified as an [ISO 8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations). | [optional] 
**user_id** | **str** |  | [optional] 
**link** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.api_token import ApiToken

# TODO update the JSON string below
json = "{}"
# create an instance of ApiToken from a JSON string
api_token_instance = ApiToken.from_json(json)
# print the JSON string representation of the object
print(ApiToken.to_json())

# convert the object into a dict
api_token_dict = api_token_instance.to_dict()
# create an instance of ApiToken from a dict
api_token_from_dict = ApiToken.from_dict(api_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


