# EmailPreviewLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**content_source** | [**HrefObject**](HrefObject.md) |  | [optional] 
**template** | [**HrefObject**](HrefObject.md) |  | [optional] 
**test** | [**HrefObject**](HrefObject.md) |  | [optional] 
**default_content** | [**HrefObject**](HrefObject.md) |  | [optional] 

## Example

```python
from openapi_client.models.email_preview_links import EmailPreviewLinks

# TODO update the JSON string below
json = "{}"
# create an instance of EmailPreviewLinks from a JSON string
email_preview_links_instance = EmailPreviewLinks.from_json(json)
# print the JSON string representation of the object
print(EmailPreviewLinks.to_json())

# convert the object into a dict
email_preview_links_dict = email_preview_links_instance.to_dict()
# create an instance of EmailPreviewLinks from a dict
email_preview_links_form_dict = email_preview_links.from_dict(email_preview_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


