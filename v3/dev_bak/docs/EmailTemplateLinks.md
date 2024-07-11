# EmailTemplateLinks


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
from openapi_client.models.email_template_links import EmailTemplateLinks

# TODO update the JSON string below
json = "{}"
# create an instance of EmailTemplateLinks from a JSON string
email_template_links_instance = EmailTemplateLinks.from_json(json)
# print the JSON string representation of the object
print(EmailTemplateLinks.to_json())

# convert the object into a dict
email_template_links_dict = email_template_links_instance.to_dict()
# create an instance of EmailTemplateLinks from a dict
email_template_links_from_dict = EmailTemplateLinks.from_dict(email_template_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


