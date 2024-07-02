# ApplicationCredentialsUsernameTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**push_status** | **str** |  | [optional] 
**template** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**user_suffix** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.application_credentials_username_template import ApplicationCredentialsUsernameTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCredentialsUsernameTemplate from a JSON string
application_credentials_username_template_instance = ApplicationCredentialsUsernameTemplate.from_json(json)
# print the JSON string representation of the object
print(ApplicationCredentialsUsernameTemplate.to_json())

# convert the object into a dict
application_credentials_username_template_dict = application_credentials_username_template_instance.to_dict()
# create an instance of ApplicationCredentialsUsernameTemplate from a dict
application_credentials_username_template_from_dict = ApplicationCredentialsUsernameTemplate.from_dict(application_credentials_username_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


