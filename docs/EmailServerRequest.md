# EmailServerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | Human-readable name for your SMTP server | [optional] 
**enabled** | **bool** | If &#x60;true&#x60;, routes all email traffic through your SMTP server | [optional] 
**host** | **str** | Hostname or IP address of your SMTP server | [optional] 
**port** | **int** | Port number of your SMTP server | [optional] 
**username** | **str** | Username used to access your SMTP server | [optional] 
**password** | **str** | Password used to access your SMTP server | [optional] 

## Example

```python
from okta.models.email_server_request import EmailServerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmailServerRequest from a JSON string
email_server_request_instance = EmailServerRequest.from_json(json)
# print the JSON string representation of the object
print(EmailServerRequest.to_json())

# convert the object into a dict
email_server_request_dict = email_server_request_instance.to_dict()
# create an instance of EmailServerRequest from a dict
email_server_request_from_dict = EmailServerRequest.from_dict(email_server_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


