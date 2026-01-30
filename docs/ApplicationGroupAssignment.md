# ApplicationGroupAssignment

The Application Group object that defines a group of users' app-specific profile and credentials for an app

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the [group](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Group/) | [optional] [readonly] 
**last_updated** | **datetime** |  | [optional] 
**priority** | **int** | Priority assigned to the group. If an app has more than one group assigned to the same user, then the group with the higher priority has its profile applied to the [application user](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/ApplicationUsers/). If a priority value isn&#39;t specified, then the next highest priority is assigned by default. See [Assign attribute group priority](https://help.okta.com/okta_help.htm?type&#x3D;oie&amp;id&#x3D;ext-usgp-app-group-priority) and the [sample priority use case](https://help.okta.com/okta_help.htm?type&#x3D;oie&amp;id&#x3D;ext-usgp-combine-values-use). | [optional] 
**profile** | **Dict[str, object]** | Specifies the profile properties applied to [application users](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/ApplicationUsers/) that are assigned to the app through group membership. Some reference properties are imported from the target app and can&#39;t be configured. See [profile](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/User/#tag/User/operation/getUser!c&#x3D;200&amp;path&#x3D;profile&amp;t&#x3D;response). | [optional] 
**embedded** | **Dict[str, object]** | Embedded resource related to the Application Group using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification. If the &#x60;expand&#x3D;group&#x60; query parameter is specified, then the [group](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Group/) object is embedded. If the &#x60;expand&#x3D;metadata&#x60; query parameter is specified, then the group assignment metadata is embedded. | [optional] [readonly] 
**links** | [**ApplicationGroupAssignmentLinks**](ApplicationGroupAssignmentLinks.md) |  | [optional] 

## Example

```python
from okta.models.application_group_assignment import ApplicationGroupAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationGroupAssignment from a JSON string
application_group_assignment_instance = ApplicationGroupAssignment.from_json(json)
# print the JSON string representation of the object
print(ApplicationGroupAssignment.to_json())

# convert the object into a dict
application_group_assignment_dict = application_group_assignment_instance.to_dict()
# create an instance of ApplicationGroupAssignment from a dict
application_group_assignment_from_dict = ApplicationGroupAssignment.from_dict(application_group_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


