# ApiTokenNetwork

The Network Condition of the API Token

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection** | **str** | The connection type of the Network Condition | [optional] 
**include** | **List[str]** | List of included IP network zones | [optional] 
**exclude** | **List[str]** | List of excluded IP network zones | [optional] 

## Example

```python
from okta.models.api_token_network import ApiTokenNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTokenNetwork from a JSON string
api_token_network_instance = ApiTokenNetwork.from_json(json)
# print the JSON string representation of the object
print(ApiTokenNetwork.to_json())

# convert the object into a dict
api_token_network_dict = api_token_network_instance.to_dict()
# create an instance of ApiTokenNetwork from a dict
api_token_network_from_dict = ApiTokenNetwork.from_dict(api_token_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


