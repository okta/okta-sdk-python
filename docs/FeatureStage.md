# FeatureStage

Current release cycle stage of a feature  If a feature's stage value is `EA`, the state is `null` and not returned. If the value is `BETA`, the state is `OPEN` or `CLOSED` depending on whether the `BETA` feature is manageable.  > **Note:** If a feature's stage is `OPEN BETA`, you can update it only in Preview cells. If a feature's stage is `CLOSED BETA`, you can disable it only in Preview cells.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**FeatureStageState**](FeatureStageState.md) |  | [optional] 
**value** | [**FeatureStageValue**](FeatureStageValue.md) |  | [optional] 

## Example

```python
from okta.models.feature_stage import FeatureStage

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureStage from a JSON string
feature_stage_instance = FeatureStage.from_json(json)
# print the JSON string representation of the object
print(FeatureStage.to_json())

# convert the object into a dict
feature_stage_dict = feature_stage_instance.to_dict()
# create an instance of FeatureStage from a dict
feature_stage_from_dict = FeatureStage.from_dict(feature_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


