# EmailTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of this email template | [optional] [readonly] 
**embedded** | [**EmailTemplateEmbedded**](EmailTemplateEmbedded.md) |  | [optional] 
**links** | [**EmailTemplateLinks**](EmailTemplateLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.email_template import EmailTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of EmailTemplate from a JSON string
email_template_instance = EmailTemplate.from_json(json)
# print the JSON string representation of the object
print(EmailTemplate.to_json())

# convert the object into a dict
email_template_dict = email_template_instance.to_dict()
# create an instance of EmailTemplate from a dict
email_template_from_dict = EmailTemplate.from_dict(email_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


