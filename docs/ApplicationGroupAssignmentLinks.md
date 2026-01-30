# ApplicationGroupAssignmentLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**app** | [**HrefObjectAppLink**](HrefObjectAppLink.md) |  | [optional] 
**group** | [**HrefObjectGroupLink**](HrefObjectGroupLink.md) |  | [optional] 

## Example

```python
from okta.models.application_group_assignment_links import ApplicationGroupAssignmentLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationGroupAssignmentLinks from a JSON string
application_group_assignment_links_instance = ApplicationGroupAssignmentLinks.from_json(json)
# print the JSON string representation of the object
print(ApplicationGroupAssignmentLinks.to_json())

# convert the object into a dict
application_group_assignment_links_dict = application_group_assignment_links_instance.to_dict()
# create an instance of ApplicationGroupAssignmentLinks from a dict
application_group_assignment_links_from_dict = ApplicationGroupAssignmentLinks.from_dict(application_group_assignment_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


