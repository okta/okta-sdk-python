# OAuth2Client


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | [optional] [readonly] 
**client_name** | **str** |  | [optional] [readonly] 
**client_uri** | **str** |  | [optional] [readonly] 
**logo_uri** | **str** |  | [optional] [readonly] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from openapi_client.models.o_auth2_client import OAuth2Client

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2Client from a JSON string
o_auth2_client_instance = OAuth2Client.from_json(json)
# print the JSON string representation of the object
print(OAuth2Client.to_json())

# convert the object into a dict
o_auth2_client_dict = o_auth2_client_instance.to_dict()
# create an instance of OAuth2Client from a dict
o_auth2_client_from_dict = OAuth2Client.from_dict(o_auth2_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


