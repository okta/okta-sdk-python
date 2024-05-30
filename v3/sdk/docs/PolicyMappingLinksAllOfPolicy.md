# PolicyMappingLinksAllOfPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hints** | [**HrefObjectHints**](HrefObjectHints.md) |  | [optional] 
**href** | **str** | Link URI | 
**name** | **str** | Link name | [optional] 
**type** | **str** | The media type of the link. If omitted, it is implicitly &#x60;application/json&#x60;. | [optional] 
**templated** | **bool** | Indicates whether the Link Object&#39;s \&quot;href\&quot; property is a URI Template. | [optional] 

## Example

```python
from openapi_client.models.policy_mapping_links_all_of_policy import PolicyMappingLinksAllOfPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyMappingLinksAllOfPolicy from a JSON string
policy_mapping_links_all_of_policy_instance = PolicyMappingLinksAllOfPolicy.from_json(json)
# print the JSON string representation of the object
print(PolicyMappingLinksAllOfPolicy.to_json())

# convert the object into a dict
policy_mapping_links_all_of_policy_dict = policy_mapping_links_all_of_policy_instance.to_dict()
# create an instance of PolicyMappingLinksAllOfPolicy from a dict
policy_mapping_links_all_of_policy_form_dict = policy_mapping_links_all_of_policy.from_dict(policy_mapping_links_all_of_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


