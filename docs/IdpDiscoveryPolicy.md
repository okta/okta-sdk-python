# IdpDiscoveryPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | **str** | Policy conditions aren&#39;t supported for this policy type. | [optional] 

## Example

```python
from okta.models.idp_discovery_policy import IdpDiscoveryPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of IdpDiscoveryPolicy from a JSON string
idp_discovery_policy_instance = IdpDiscoveryPolicy.from_json(json)
# print the JSON string representation of the object
print(IdpDiscoveryPolicy.to_json())

# convert the object into a dict
idp_discovery_policy_dict = idp_discovery_policy_instance.to_dict()
# create an instance of IdpDiscoveryPolicy from a dict
idp_discovery_policy_from_dict = IdpDiscoveryPolicy.from_dict(idp_discovery_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


