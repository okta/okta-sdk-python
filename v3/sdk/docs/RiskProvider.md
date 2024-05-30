# RiskProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**RiskProviderAction**](RiskProviderAction.md) |  | 
**client_id** | **str** | The ID of the [OAuth service app](https://developer.okta.com/docs/guides/implement-oauth-for-okta-serviceapp/main/#create-a-service-app-and-grant-scopes) that is used to send risk events to Okta | 
**created** | **datetime** | Timestamp when the Risk Provider object was created | [optional] [readonly] 
**id** | **str** | The ID of the Risk Provider object | [readonly] 
**last_updated** | **datetime** | Timestamp when the Risk Provider object was last updated | [optional] [readonly] 
**name** | **str** | Name of the risk provider | 
**links** | [**LinksSelf**](LinksSelf.md) |  | 

## Example

```python
from openapi_client.models.risk_provider import RiskProvider

# TODO update the JSON string below
json = "{}"
# create an instance of RiskProvider from a JSON string
risk_provider_instance = RiskProvider.from_json(json)
# print the JSON string representation of the object
print(RiskProvider.to_json())

# convert the object into a dict
risk_provider_dict = risk_provider_instance.to_dict()
# create an instance of RiskProvider from a dict
risk_provider_form_dict = risk_provider.from_dict(risk_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


