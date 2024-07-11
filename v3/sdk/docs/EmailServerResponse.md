# EmailServerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | A name to identify this configuration | [optional] 
**enabled** | **bool** | True if and only if all email traffic should be routed through this SMTP Server | [optional] 
**host** | **str** | The address of the SMTP Server | [optional] 
**port** | **int** | The port number of the SMTP Server | [optional] 
**username** | **str** | The username to use with your SMTP Server | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from okta.models.email_server_response import EmailServerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailServerResponse from a JSON string
email_server_response_instance = EmailServerResponse.from_json(json)
# print the JSON string representation of the object
print(EmailServerResponse.to_json())

# convert the object into a dict
email_server_response_dict = email_server_response_instance.to_dict()
# create an instance of EmailServerResponse from a dict
email_server_response_from_dict = EmailServerResponse.from_dict(email_server_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


