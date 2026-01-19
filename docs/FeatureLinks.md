# FeatureLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**dependents** | [**FeatureLinksAllOfDependents**](FeatureLinksAllOfDependents.md) |  | [optional] 
**dependencies** | [**FeatureLinksAllOfDependencies**](FeatureLinksAllOfDependencies.md) |  | [optional] 

## Example

```python
from okta.models.feature_links import FeatureLinks

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureLinks from a JSON string
feature_links_instance = FeatureLinks.from_json(json)
# print the JSON string representation of the object
print(FeatureLinks.to_json())

# convert the object into a dict
feature_links_dict = feature_links_instance.to_dict()
# create an instance of FeatureLinks from a dict
feature_links_from_dict = FeatureLinks.from_dict(feature_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


