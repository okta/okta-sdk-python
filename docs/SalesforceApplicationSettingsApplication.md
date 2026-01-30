# SalesforceApplicationSettingsApplication

Salesforce app instance properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_type** | **str** | Salesforce instance that you want to connect to | 
**integration_type** | **str** | Salesforce integration type | 
**login_url** | **str** | The Login URL specified in your Salesforce Single Sign-On settings | [optional] 
**logout_url** | **str** | Salesforce Logout URL | [optional] 

## Example

```python
from okta.models.salesforce_application_settings_application import SalesforceApplicationSettingsApplication

# TODO update the JSON string below
json = "{}"
# create an instance of SalesforceApplicationSettingsApplication from a JSON string
salesforce_application_settings_application_instance = SalesforceApplicationSettingsApplication.from_json(json)
# print the JSON string representation of the object
print(SalesforceApplicationSettingsApplication.to_json())

# convert the object into a dict
salesforce_application_settings_application_dict = salesforce_application_settings_application_instance.to_dict()
# create an instance of SalesforceApplicationSettingsApplication from a dict
salesforce_application_settings_application_from_dict = SalesforceApplicationSettingsApplication.from_dict(salesforce_application_settings_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


