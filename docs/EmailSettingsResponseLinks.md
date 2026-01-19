# EmailSettingsResponseLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObject**](HrefObject.md) |  | [optional] 
**template** | [**HrefObject**](HrefObject.md) |  | [optional] 

## Example

```python
from okta.models.email_settings_response_links import EmailSettingsResponseLinks

# TODO update the JSON string below
json = "{}"
# create an instance of EmailSettingsResponseLinks from a JSON string
email_settings_response_links_instance = EmailSettingsResponseLinks.from_json(json)
# print the JSON string representation of the object
print(EmailSettingsResponseLinks.to_json())

# convert the object into a dict
email_settings_response_links_dict = email_settings_response_links_instance.to_dict()
# create an instance of EmailSettingsResponseLinks from a dict
email_settings_response_links_from_dict = EmailSettingsResponseLinks.from_dict(email_settings_response_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


