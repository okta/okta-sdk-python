# UpdateFeatureForApplicationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create** | [**CapabilitiesCreateObject**](CapabilitiesCreateObject.md) |  | [optional] 
**update** | [**CapabilitiesUpdateObject**](CapabilitiesUpdateObject.md) |  | [optional] 
**import_rules** | [**CapabilitiesImportRulesObject**](CapabilitiesImportRulesObject.md) |  | 
**import_settings** | [**CapabilitiesImportSettingsObject**](CapabilitiesImportSettingsObject.md) |  | 

## Example

```python
from okta.models.update_feature_for_application_request import UpdateFeatureForApplicationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFeatureForApplicationRequest from a JSON string
update_feature_for_application_request_instance = UpdateFeatureForApplicationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateFeatureForApplicationRequest.to_json())

# convert the object into a dict
update_feature_for_application_request_dict = update_feature_for_application_request_instance.to_dict()
# create an instance of UpdateFeatureForApplicationRequest from a dict
update_feature_for_application_request_from_dict = UpdateFeatureForApplicationRequest.from_dict(update_feature_for_application_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


