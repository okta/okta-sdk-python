# EmailTemplateResponseLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**settings** | [**HrefObject**](HrefObject.md) |  | [optional] 
**default_content** | [**HrefObject**](HrefObject.md) |  | [optional] 
**customizations** | [**HrefObject**](HrefObject.md) |  | [optional] 
**test** | [**HrefObject**](HrefObject.md) |  | [optional] 

## Example

```python
from okta.models.email_template_response_links import EmailTemplateResponseLinks

# TODO update the JSON string below
json = "{}"
# create an instance of EmailTemplateResponseLinks from a JSON string
email_template_response_links_instance = EmailTemplateResponseLinks.from_json(json)
# print the JSON string representation of the object
print(EmailTemplateResponseLinks.to_json())

# convert the object into a dict
email_template_response_links_dict = email_template_response_links_instance.to_dict()
# create an instance of EmailTemplateResponseLinks from a dict
email_template_response_links_from_dict = EmailTemplateResponseLinks.from_dict(email_template_response_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


