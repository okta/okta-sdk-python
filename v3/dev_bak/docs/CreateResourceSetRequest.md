# CreateResourceSetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the Resource Set | [optional] 
**label** | **str** | Unique label for the Resource Set | [optional] 
**resources** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.create_resource_set_request import CreateResourceSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateResourceSetRequest from a JSON string
create_resource_set_request_instance = CreateResourceSetRequest.from_json(json)
# print the JSON string representation of the object
print(CreateResourceSetRequest.to_json())

# convert the object into a dict
create_resource_set_request_dict = create_resource_set_request_instance.to_dict()
# create an instance of CreateResourceSetRequest from a dict
create_resource_set_request_from_dict = CreateResourceSetRequest.from_dict(create_resource_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


