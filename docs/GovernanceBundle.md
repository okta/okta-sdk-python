# GovernanceBundle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the governance bundle | [optional] 
**id** | **str** | Governance bundle ID | [optional] 
**name** | **str** | Name of the governance bundle | [optional] 
**orn** | **str** | The governance bundle resource, in [ORN format](https://developer.okta.com/docs/api/openapi/okta-management/guides/roles/#okta-resource-name-orn) | [optional] 
**status** | **str** | Status of the governance bundle | [optional] 
**links** | [**GovernanceBundleLinks**](GovernanceBundleLinks.md) |  | [optional] 

## Example

```python
from okta.models.governance_bundle import GovernanceBundle

# TODO update the JSON string below
json = "{}"
# create an instance of GovernanceBundle from a JSON string
governance_bundle_instance = GovernanceBundle.from_json(json)
# print the JSON string representation of the object
print(GovernanceBundle.to_json())

# convert the object into a dict
governance_bundle_dict = governance_bundle_instance.to_dict()
# create an instance of GovernanceBundle from a dict
governance_bundle_from_dict = GovernanceBundle.from_dict(governance_bundle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


