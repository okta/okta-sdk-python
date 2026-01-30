# EmailSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipients** | **str** |  | [optional] 
**links** | [**EmailSettingsResponseLinks**](EmailSettingsResponseLinks.md) |  | [optional] 

## Example

```python
from okta.models.email_settings_response import EmailSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailSettingsResponse from a JSON string
email_settings_response_instance = EmailSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(EmailSettingsResponse.to_json())

# convert the object into a dict
email_settings_response_dict = email_settings_response_instance.to_dict()
# create an instance of EmailSettingsResponse from a dict
email_settings_response_from_dict = EmailSettingsResponse.from_dict(email_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


