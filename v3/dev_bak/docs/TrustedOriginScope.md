# TrustedOriginScope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_okta_apps** | [**List[IframeEmbedScopeAllowedApps]**](IframeEmbedScopeAllowedApps.md) |  | [optional] 
**type** | [**TrustedOriginScopeType**](TrustedOriginScopeType.md) |  | [optional] 

## Example

```python
from openapi_client.models.trusted_origin_scope import TrustedOriginScope

# TODO update the JSON string below
json = "{}"
# create an instance of TrustedOriginScope from a JSON string
trusted_origin_scope_instance = TrustedOriginScope.from_json(json)
# print the JSON string representation of the object
print(TrustedOriginScope.to_json())

# convert the object into a dict
trusted_origin_scope_dict = trusted_origin_scope_instance.to_dict()
# create an instance of TrustedOriginScope from a dict
trusted_origin_scope_from_dict = TrustedOriginScope.from_dict(trusted_origin_scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


