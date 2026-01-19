# OAuth2Client


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Unique key for the client application. The &#x60;client_id&#x60; is immutable. | [optional] [readonly] 
**client_name** | **str** | Human-readable string name of the client application | [optional] [readonly] 
**client_uri** | **str** |  | [optional] [readonly] 
**logo_uri** | **str** | URL string that references a logo for the client consent dialog (not the sign-in dialog) | [optional] [readonly] 
**links** | [**OAuth2ClientLinks**](OAuth2ClientLinks.md) |  | [optional] 

## Example

```python
from okta.models.o_auth2_client import OAuth2Client

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


