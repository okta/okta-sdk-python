# ApplicationExpressConfiguration

<div class=\"x-lifecycle-container\"><x-lifecycle class=\"oie\"></x-lifecycle></div> Indicates which Express Configuration capabilities the app supports and has enabled

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled_capabilities** | [**List[ApplicationCapability]**](ApplicationCapability.md) | Capabilities currently enabled for the app | [optional] 
**supported_capabilities** | [**List[ApplicationCapability]**](ApplicationCapability.md) | Capabilities supported by the app | [optional] 

## Example

```python
from okta.models.application_express_configuration import ApplicationExpressConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationExpressConfiguration from a JSON string
application_express_configuration_instance = ApplicationExpressConfiguration.from_json(json)
# print the JSON string representation of the object
print(ApplicationExpressConfiguration.to_json())

# convert the object into a dict
application_express_configuration_dict = application_express_configuration_instance.to_dict()
# create an instance of ApplicationExpressConfiguration from a dict
application_express_configuration_from_dict = ApplicationExpressConfiguration.from_dict(application_express_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


