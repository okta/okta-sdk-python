# OAuth2ClaimConditions

Specifies the scopes for the Claim

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scopes** | **List[str]** |  | [optional] 

## Example

```python
from okta.models.o_auth2_claim_conditions import OAuth2ClaimConditions

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2ClaimConditions from a JSON string
o_auth2_claim_conditions_instance = OAuth2ClaimConditions.from_json(json)
# print the JSON string representation of the object
print(OAuth2ClaimConditions.to_json())

# convert the object into a dict
o_auth2_claim_conditions_dict = o_auth2_claim_conditions_instance.to_dict()
# create an instance of OAuth2ClaimConditions from a dict
o_auth2_claim_conditions_from_dict = OAuth2ClaimConditions.from_dict(o_auth2_claim_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


