# EmailSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipients** | **str** |  | 

## Example

```python
from okta.models.email_settings import EmailSettings

# TODO update the JSON string below
json = "{}"
# create an instance of EmailSettings from a JSON string
email_settings_instance = EmailSettings.from_json(json)
# print the JSON string representation of the object
print(EmailSettings.to_json())

# convert the object into a dict
email_settings_dict = email_settings_instance.to_dict()
# create an instance of EmailSettings from a dict
email_settings_from_dict = EmailSettings.from_dict(email_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


