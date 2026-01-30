# GovernanceBundlesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundles** | [**List[GovernanceBundle]**](GovernanceBundle.md) | List of governance bundles | [optional] 
**links** | [**GovernanceBundlesResponseLinks**](GovernanceBundlesResponseLinks.md) |  | [optional] 

## Example

```python
from okta.models.governance_bundles_response import GovernanceBundlesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GovernanceBundlesResponse from a JSON string
governance_bundles_response_instance = GovernanceBundlesResponse.from_json(json)
# print the JSON string representation of the object
print(GovernanceBundlesResponse.to_json())

# convert the object into a dict
governance_bundles_response_dict = governance_bundles_response_instance.to_dict()
# create an instance of GovernanceBundlesResponse from a dict
governance_bundles_response_from_dict = GovernanceBundlesResponse.from_dict(governance_bundles_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


