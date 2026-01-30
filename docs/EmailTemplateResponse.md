# EmailTemplateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of this email template | [optional] [readonly] 
**embedded** | [**EmailTemplateResponseEmbedded**](EmailTemplateResponseEmbedded.md) |  | [optional] 
**links** | [**EmailTemplateResponseLinks**](EmailTemplateResponseLinks.md) |  | [optional] 

## Example

```python
from okta.models.email_template_response import EmailTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailTemplateResponse from a JSON string
email_template_response_instance = EmailTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(EmailTemplateResponse.to_json())

# convert the object into a dict
email_template_response_dict = email_template_response_instance.to_dict()
# create an instance of EmailTemplateResponse from a dict
email_template_response_from_dict = EmailTemplateResponse.from_dict(email_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


