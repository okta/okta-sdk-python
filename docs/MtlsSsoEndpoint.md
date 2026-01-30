# MtlsSsoEndpoint

The Single Sign-On (SSO) endpoint is the IdP's `SingleSignOnService` endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 

## Example

```python
from okta.models.mtls_sso_endpoint import MtlsSsoEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of MtlsSsoEndpoint from a JSON string
mtls_sso_endpoint_instance = MtlsSsoEndpoint.from_json(json)
# print the JSON string representation of the object
print(MtlsSsoEndpoint.to_json())

# convert the object into a dict
mtls_sso_endpoint_dict = mtls_sso_endpoint_instance.to_dict()
# create an instance of MtlsSsoEndpoint from a dict
mtls_sso_endpoint_from_dict = MtlsSsoEndpoint.from_dict(mtls_sso_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


