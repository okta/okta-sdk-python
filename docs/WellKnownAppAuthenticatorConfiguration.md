# WellKnownAppAuthenticatorConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_authenticator_enroll_endpoint** | **str** | The authenticator enrollment endpoint | [optional] 
**authenticator_id** | **str** | The unique identifier of the app authenticator | [optional] 
**created_date** | **datetime** | Timestamp when the authenticator was created | [optional] 
**key** | [**AuthenticatorKeyEnum**](AuthenticatorKeyEnum.md) |  | [optional] 
**last_updated** | **datetime** | Timestamp when the authenticator was last modified | [optional] 
**name** | **str** | The authenticator display name | [optional] 
**org_id** | **str** | The &#x60;id&#x60; of the Okta Org | [optional] 
**settings** | [**WellKnownAppAuthenticatorConfigurationSettings**](WellKnownAppAuthenticatorConfigurationSettings.md) |  | [optional] 
**supported_methods** | [**List[SupportedMethods]**](SupportedMethods.md) |  | [optional] 
**type** | **str** | The type of authenticator | [optional] 

## Example

```python
from okta.models.well_known_app_authenticator_configuration import WellKnownAppAuthenticatorConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of WellKnownAppAuthenticatorConfiguration from a JSON string
well_known_app_authenticator_configuration_instance = WellKnownAppAuthenticatorConfiguration.from_json(json)
# print the JSON string representation of the object
print(WellKnownAppAuthenticatorConfiguration.to_json())

# convert the object into a dict
well_known_app_authenticator_configuration_dict = well_known_app_authenticator_configuration_instance.to_dict()
# create an instance of WellKnownAppAuthenticatorConfiguration from a dict
well_known_app_authenticator_configuration_from_dict = WellKnownAppAuthenticatorConfiguration.from_dict(well_known_app_authenticator_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


