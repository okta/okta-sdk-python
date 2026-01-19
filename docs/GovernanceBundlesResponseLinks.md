# GovernanceBundlesResponseLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**next** | [**HrefObjectNextLink**](HrefObjectNextLink.md) |  | [optional] 

## Example

```python
from okta.models.governance_bundles_response_links import GovernanceBundlesResponseLinks

# TODO update the JSON string below
json = "{}"
# create an instance of GovernanceBundlesResponseLinks from a JSON string
governance_bundles_response_links_instance = GovernanceBundlesResponseLinks.from_json(json)
# print the JSON string representation of the object
print(GovernanceBundlesResponseLinks.to_json())

# convert the object into a dict
governance_bundles_response_links_dict = governance_bundles_response_links_instance.to_dict()
# create an instance of GovernanceBundlesResponseLinks from a dict
governance_bundles_response_links_from_dict = GovernanceBundlesResponseLinks.from_dict(governance_bundles_response_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


