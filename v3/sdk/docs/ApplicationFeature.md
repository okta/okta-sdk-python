# ApplicationFeature

The Feature object is used to configure application feature settings.  The only feature currently supported is `USER_PROVISIONING` for the Org2Org application type. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | [**CapabilitiesObject**](CapabilitiesObject.md) |  | [optional] 
**description** | **str** | Description of the feature | [optional] [readonly] 
**name** | **str** | Identifying name of the feature | [optional] [readonly] 
**status** | [**EnabledStatus**](EnabledStatus.md) |  | [optional] 
**links** | [**ApplicationFeatureLinks**](ApplicationFeatureLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.application_feature import ApplicationFeature

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationFeature from a JSON string
application_feature_instance = ApplicationFeature.from_json(json)
# print the JSON string representation of the object
print(ApplicationFeature.to_json())

# convert the object into a dict
application_feature_dict = application_feature_instance.to_dict()
# create an instance of ApplicationFeature from a dict
application_feature_from_dict = ApplicationFeature.from_dict(application_feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


