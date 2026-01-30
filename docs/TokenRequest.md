# TokenRequest

Token inline hook request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_event_version** | **str** | The inline hook cloud version | [optional] 
**content_type** | **str** | The inline hook request header content | [optional] 
**event_id** | **str** | The individual inline hook request ID | [optional] 
**event_time** | **str** | The time the inline hook request was sent | [optional] 
**event_type_version** | **str** | The inline hook version | [optional] 
**data** | [**TokenPayLoadData**](TokenPayLoadData.md) |  | [optional] 
**event_type** | **str** | The type of inline hook. The token inline hook type is &#x60;com.okta.oauth2.tokens.transform&#x60;. | [optional] 
**source** | **str** | The URL of the token inline hook | [optional] 

## Example

```python
from okta.models.token_request import TokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenRequest from a JSON string
token_request_instance = TokenRequest.from_json(json)
# print the JSON string representation of the object
print(TokenRequest.to_json())

# convert the object into a dict
token_request_dict = token_request_instance.to_dict()
# create an instance of TokenRequest from a dict
token_request_from_dict = TokenRequest.from_dict(token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


