# BaseEmailServer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | Human-readable name for your SMTP server | [optional] 
**enabled** | **bool** | If &#x60;true&#x60;, routes all email traffic through your SMTP server | [optional] 
**host** | **str** | Hostname or IP address of your SMTP server | [optional] 
**port** | **int** | Port number of your SMTP server | [optional] 
**username** | **str** | Username used to access your SMTP server | [optional] 

## Example

```python
from okta.models.base_email_server import BaseEmailServer

# TODO update the JSON string below
json = "{}"
# create an instance of BaseEmailServer from a JSON string
base_email_server_instance = BaseEmailServer.from_json(json)
# print the JSON string representation of the object
print(BaseEmailServer.to_json())

# convert the object into a dict
base_email_server_dict = base_email_server_instance.to_dict()
# create an instance of BaseEmailServer from a dict
base_email_server_from_dict = BaseEmailServer.from_dict(base_email_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


