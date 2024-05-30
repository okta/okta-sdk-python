# OAuth2Claim


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**always_include_in_token** | **bool** |  | [optional] 
**claim_type** | [**OAuth2ClaimType**](OAuth2ClaimType.md) |  | [optional] 
**conditions** | [**OAuth2ClaimConditions**](OAuth2ClaimConditions.md) |  | [optional] 
**group_filter_type** | [**OAuth2ClaimGroupFilterType**](OAuth2ClaimGroupFilterType.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**status** | [**LifecycleStatus**](LifecycleStatus.md) |  | [optional] 
**system** | **bool** |  | [optional] 
**value** | **str** |  | [optional] 
**value_type** | [**OAuth2ClaimValueType**](OAuth2ClaimValueType.md) |  | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from openapi_client.models.o_auth2_claim import OAuth2Claim

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2Claim from a JSON string
o_auth2_claim_instance = OAuth2Claim.from_json(json)
# print the JSON string representation of the object
print(OAuth2Claim.to_json())

# convert the object into a dict
o_auth2_claim_dict = o_auth2_claim_instance.to_dict()
# create an instance of OAuth2Claim from a dict
o_auth2_claim_form_dict = o_auth2_claim.from_dict(o_auth2_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


