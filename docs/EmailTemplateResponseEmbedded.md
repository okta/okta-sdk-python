# EmailTemplateResponseEmbedded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**EmailSettingsResponse**](EmailSettingsResponse.md) |  | [optional] 
**customization_count** | **int** |  | [optional] 

## Example

```python
from okta.models.email_template_response_embedded import EmailTemplateResponseEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of EmailTemplateResponseEmbedded from a JSON string
email_template_response_embedded_instance = EmailTemplateResponseEmbedded.from_json(json)
# print the JSON string representation of the object
print(EmailTemplateResponseEmbedded.to_json())

# convert the object into a dict
email_template_response_embedded_dict = email_template_response_embedded_instance.to_dict()
# create an instance of EmailTemplateResponseEmbedded from a dict
email_template_response_embedded_from_dict = EmailTemplateResponseEmbedded.from_dict(email_template_response_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


