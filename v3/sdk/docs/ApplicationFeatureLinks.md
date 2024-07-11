# ApplicationFeatureLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 

## Example

```python
from okta.models.application_feature_links import ApplicationFeatureLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationFeatureLinks from a JSON string
application_feature_links_instance = ApplicationFeatureLinks.from_json(json)
# print the JSON string representation of the object
print(ApplicationFeatureLinks.to_json())

# convert the object into a dict
application_feature_links_dict = application_feature_links_instance.to_dict()
# create an instance of ApplicationFeatureLinks from a dict
application_feature_links_from_dict = ApplicationFeatureLinks.from_dict(application_feature_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


