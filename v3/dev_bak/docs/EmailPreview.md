# EmailPreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The email&#39;s HTML body | [optional] [readonly] 
**subject** | **str** | The email&#39;s subject | [optional] [readonly] 
**links** | [**EmailPreviewLinks**](EmailPreviewLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.email_preview import EmailPreview

# TODO update the JSON string below
json = "{}"
# create an instance of EmailPreview from a JSON string
email_preview_instance = EmailPreview.from_json(json)
# print the JSON string representation of the object
print(EmailPreview.to_json())

# convert the object into a dict
email_preview_dict = email_preview_instance.to_dict()
# create an instance of EmailPreview from a dict
email_preview_from_dict = EmailPreview.from_dict(email_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


