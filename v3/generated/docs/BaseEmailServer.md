# BaseEmailServer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | A name to identify this configuration | [optional] 
**enabled** | **bool** | True if and only if all email traffic should be routed through this SMTP Server | [optional] 
**host** | **str** | The address of the SMTP Server | [optional] 
**port** | **int** | The port number of the SMTP Server | [optional] 
**username** | **str** | The username to use with your SMTP Server | [optional] 

## Example

```python
from openapi_client.models.base_email_server import BaseEmailServer

# TODO update the JSON string below
json = "{}"
# create an instance of BaseEmailServer from a JSON string
base_email_server_instance = BaseEmailServer.from_json(json)
# print the JSON string representation of the object
print(BaseEmailServer.to_json())

# convert the object into a dict
base_email_server_dict = base_email_server_instance.to_dict()
# create an instance of BaseEmailServer from a dict
base_email_server_form_dict = base_email_server.from_dict(base_email_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


