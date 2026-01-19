# Feature

Specifies feature release cycle information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Brief description of the feature and what it provides | [optional] 
**id** | **str** | Unique identifier for this feature | [optional] [readonly] 
**name** | **str** | Name of the feature | [optional] 
**stage** | [**FeatureStage**](FeatureStage.md) |  | [optional] 
**status** | [**EnabledStatus**](EnabledStatus.md) |  | [optional] 
**type** | [**FeatureType**](FeatureType.md) |  | [optional] 
**links** | [**FeatureLinks**](FeatureLinks.md) |  | [optional] 

## Example

```python
from okta.models.feature import Feature

# TODO update the JSON string below
json = "{}"
# create an instance of Feature from a JSON string
feature_instance = Feature.from_json(json)
# print the JSON string representation of the object
print(Feature.to_json())

# convert the object into a dict
feature_dict = feature_instance.to_dict()
# create an instance of Feature from a dict
feature_from_dict = Feature.from_dict(feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


