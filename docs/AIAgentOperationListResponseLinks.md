# AIAgentOperationListResponseLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**next** | [**HrefObjectNextLink**](HrefObjectNextLink.md) |  | [optional] 

## Example

```python
from okta.models.ai_agent_operation_list_response_links import AIAgentOperationListResponseLinks

# TODO update the JSON string below
json = "{}"
# create an instance of AIAgentOperationListResponseLinks from a JSON string
ai_agent_operation_list_response_links_instance = AIAgentOperationListResponseLinks.from_json(json)
# print the JSON string representation of the object
print(AIAgentOperationListResponseLinks.to_json())

# convert the object into a dict
ai_agent_operation_list_response_links_dict = ai_agent_operation_list_response_links_instance.to_dict()
# create an instance of AIAgentOperationListResponseLinks from a dict
ai_agent_operation_list_response_links_from_dict = AIAgentOperationListResponseLinks.from_dict(ai_agent_operation_list_response_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


