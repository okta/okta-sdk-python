# GovernanceBundleCreateRequest

Request to create a governance bundle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the governance bundle | [optional] 
**entitlements** | [**List[IAMBundleEntitlement]**](IAMBundleEntitlement.md) | List of entitlements to include in the governance bundle | [optional] 
**name** | **str** | Name of the governance bundle | [optional] 

## Example

```python
from okta.models.governance_bundle_create_request import GovernanceBundleCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GovernanceBundleCreateRequest from a JSON string
governance_bundle_create_request_instance = GovernanceBundleCreateRequest.from_json(json)
# print the JSON string representation of the object
print(GovernanceBundleCreateRequest.to_json())

# convert the object into a dict
governance_bundle_create_request_dict = governance_bundle_create_request_instance.to_dict()
# create an instance of GovernanceBundleCreateRequest from a dict
governance_bundle_create_request_from_dict = GovernanceBundleCreateRequest.from_dict(governance_bundle_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


