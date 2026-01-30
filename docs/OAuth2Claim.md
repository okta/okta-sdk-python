# OAuth2Claim


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**always_include_in_token** | **bool** | Specifies whether to include Claims in the token. The value is always &#x60;TRUE&#x60; for access token Claims. If the value is set to &#x60;FALSE&#x60; for an ID token claim, the Claim isn&#39;t included in the ID token when the token is requested with the access token or with the &#x60;authorization_code&#x60;. The client instead uses the access token to get Claims from the &#x60;/userinfo&#x60; endpoint. | [optional] 
**claim_type** | [**OAuth2ClaimType**](OAuth2ClaimType.md) |  | [optional] 
**conditions** | [**OAuth2ClaimConditions**](OAuth2ClaimConditions.md) |  | [optional] 
**group_filter_type** | [**OAuth2ClaimGroupFilterType**](OAuth2ClaimGroupFilterType.md) |  | [optional] 
**id** | **str** | ID of the Claim | [optional] [readonly] 
**name** | **str** | Name of the Claim | [optional] 
**status** | [**LifecycleStatus**](LifecycleStatus.md) |  | [optional] 
**system** | **bool** | When &#x60;true&#x60;, indicates that Okta created the Claim | [optional] 
**value** | **str** | Specifies the value of the Claim. This value must be a string literal if &#x60;valueType&#x60; is &#x60;GROUPS&#x60;, and the string literal is matched with the selected &#x60;group_filter_type&#x60;. The value must be an Okta EL expression if &#x60;valueType&#x60; is &#x60;EXPRESSION&#x60;. | [optional] 
**value_type** | [**OAuth2ClaimValueType**](OAuth2ClaimValueType.md) |  | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.o_auth2_claim import OAuth2Claim

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2Claim from a JSON string
o_auth2_claim_instance = OAuth2Claim.from_json(json)
# print the JSON string representation of the object
print(OAuth2Claim.to_json())

# convert the object into a dict
o_auth2_claim_dict = o_auth2_claim_instance.to_dict()
# create an instance of OAuth2Claim from a dict
o_auth2_claim_from_dict = OAuth2Claim.from_dict(o_auth2_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


