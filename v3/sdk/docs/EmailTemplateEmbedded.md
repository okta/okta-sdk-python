# EmailTemplateEmbedded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**EmailSettings**](EmailSettings.md) |  | [optional] 
**customization_count** | **int** |  | [optional] 

## Example

```python
from okta.models.email_template_embedded import EmailTemplateEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of EmailTemplateEmbedded from a JSON string
email_template_embedded_instance = EmailTemplateEmbedded.from_json(json)
# print the JSON string representation of the object
print(EmailTemplateEmbedded.to_json())

# convert the object into a dict
email_template_embedded_dict = email_template_embedded_instance.to_dict()
# create an instance of EmailTemplateEmbedded from a dict
email_template_embedded_from_dict = EmailTemplateEmbedded.from_dict(email_template_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


