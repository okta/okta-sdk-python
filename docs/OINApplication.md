# OINApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | [**ApplicationAccessibility**](ApplicationAccessibility.md) |  | [optional] 
**credentials** | [**SchemeApplicationCredentials**](SchemeApplicationCredentials.md) |  | [optional] 
**label** | **str** | User-defined display name for app | [optional] 
**licensing** | [**ApplicationLicensing**](ApplicationLicensing.md) |  | [optional] 
**name** | **str** | The key name for the OIN app definition | [optional] 
**profile** | **Dict[str, object]** | Contains any valid JSON schema for specifying properties that can be referenced from a request (only available to OAuth 2.0 client apps) | [optional] 
**sign_on_mode** | **str** | Authentication mode for the app | [optional] 
**status** | [**ApplicationLifecycleStatus**](ApplicationLifecycleStatus.md) |  | [optional] 
**visibility** | [**ApplicationVisibility**](ApplicationVisibility.md) |  | [optional] 

## Example

```python
from okta.models.oin_application import OINApplication

# TODO update the JSON string below
json = "{}"
# create an instance of OINApplication from a JSON string
oin_application_instance = OINApplication.from_json(json)
# print the JSON string representation of the object
print(OINApplication.to_json())

# convert the object into a dict
oin_application_dict = oin_application_instance.to_dict()
# create an instance of OINApplication from a dict
oin_application_from_dict = OINApplication.from_dict(oin_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


