# EmailServerListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_servers** | [**List[EmailServerResponse]**](EmailServerResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.email_server_list_response import EmailServerListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailServerListResponse from a JSON string
email_server_list_response_instance = EmailServerListResponse.from_json(json)
# print the JSON string representation of the object
print(EmailServerListResponse.to_json())

# convert the object into a dict
email_server_list_response_dict = email_server_list_response_instance.to_dict()
# create an instance of EmailServerListResponse from a dict
email_server_list_response_from_dict = EmailServerListResponse.from_dict(email_server_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


