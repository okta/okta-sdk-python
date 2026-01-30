# EmailServerPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | Human-readable name for your SMTP server | 
**enabled** | **bool** | If &#x60;true&#x60;, routes all email traffic through your SMTP server | [optional] 
**host** | **str** | Hostname or IP address of your SMTP server | 
**port** | **int** | Port number of your SMTP server | 
**username** | **str** | Username used to access your SMTP server | 
**password** | **str** | Password used to access your SMTP server | 

## Example

```python
from okta.models.email_server_post import EmailServerPost

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


