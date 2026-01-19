# CreateResourceSetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the resource set | 
**label** | **str** | Unique name for the resource set | 
**resources** | **List[str]** | The endpoint (URL) that references all resource objects included in the resource set. Resources are identified by either an Okta Resource Name (ORN) or by a REST URL format. See [Okta Resource Name](/openapi/okta-management/guides/roles/#okta-resource-name-orn). | 

## Example

```python
from okta.models.create_resource_set_request import CreateResourceSetRequest

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


