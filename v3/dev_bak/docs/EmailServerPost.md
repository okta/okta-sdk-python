# EmailServerPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | A name to identify this configuration | 
**enabled** | **bool** | True if and only if all email traffic should be routed through this SMTP Server | [optional] 
**host** | **str** | The address of the SMTP Server | 
**port** | **int** | The port number of the SMTP Server | 
**username** | **str** | The username to use with your SMTP Server | 
**password** | **str** | The password to use with your SMTP server | 

## Example

```python
from openapi_client.models.email_server_post import EmailServerPost

# TODO update the JSON string below
json = "{}"
# create an instance of EmailServerPost from a JSON string
email_server_post_instance = EmailServerPost.from_json(json)
# print the JSON string representation of the object
print(EmailServerPost.to_json())

# convert the object into a dict
email_server_post_dict = email_server_post_instance.to_dict()
# create an instance of EmailServerPost from a dict
email_server_post_from_dict = EmailServerPost.from_dict(email_server_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


