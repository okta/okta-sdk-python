# EmailServerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | A name to identify this configuration | [optional] 
**enabled** | **bool** | True if and only if all email traffic should be routed through this SMTP Server | [optional] 
**host** | **str** | The address of the SMTP Server | [optional] 
**port** | **int** | The port number of the SMTP Server | [optional] 
**username** | **str** | The username to use with your SMTP Server | [optional] 
**password** | **str** | The password to use with your SMTP server | [optional] 

## Example

```python
from openapi_client.models.email_server_request import EmailServerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmailServerRequest from a JSON string
email_server_request_instance = EmailServerRequest.from_json(json)
# print the JSON string representation of the object
print(EmailServerRequest.to_json())

# convert the object into a dict
email_server_request_dict = email_server_request_instance.to_dict()
# create an instance of EmailServerRequest from a dict
email_server_request_form_dict = email_server_request.from_dict(email_server_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


