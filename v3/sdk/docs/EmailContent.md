# EmailContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The email&#39;s HTML body. May contain [variable references](https://velocity.apache.org/engine/1.7/user-guide.html#references). | 
**subject** | **str** | The email&#39;s subject. May contain [variable references](https://velocity.apache.org/engine/1.7/user-guide.html#references). | 

## Example

```python
from okta.models.email_content import EmailContent

# TODO update the JSON string below
json = "{}"
# create an instance of EmailContent from a JSON string
email_content_instance = EmailContent.from_json(json)
# print the JSON string representation of the object
print(EmailContent.to_json())

# convert the object into a dict
email_content_dict = email_content_instance.to_dict()
# create an instance of EmailContent from a dict
email_content_from_dict = EmailContent.from_dict(email_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


