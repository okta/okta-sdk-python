# UserRiskGetResponseLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**user** | [**HrefObjectUserLink**](HrefObjectUserLink.md) |  | [optional] 

## Example

```python
from okta.models.user_risk_get_response_links import UserRiskGetResponseLinks

# TODO update the JSON string below
json = "{}"
# create an instance of UserRiskGetResponseLinks from a JSON string
user_risk_get_response_links_instance = UserRiskGetResponseLinks.from_json(json)
# print the JSON string representation of the object
print(UserRiskGetResponseLinks.to_json())

# convert the object into a dict
user_risk_get_response_links_dict = user_risk_get_response_links_instance.to_dict()
# create an instance of UserRiskGetResponseLinks from a dict
user_risk_get_response_links_from_dict = UserRiskGetResponseLinks.from_dict(user_risk_get_response_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


