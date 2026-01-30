# OrgCrossAppAccessConnection

Connection object for Cross App Access connections

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | The ISO 8601 formatted date and time when the connection was created | [optional] [readonly] 
**id** | **str** | Unique identifier for the connection | [optional] [readonly] 
**last_updated** | **datetime** | The ISO 8601 formatted date and time when the connection was last updated | [optional] [readonly] 
**requesting_app_instance_id** | **str** | ID of the requesting app instance | [optional] 
**resource_app_instance_id** | **str** | ID of the resource app instance | [optional] 
**status** | **str** | Indicates if the Cross App Access connection is active or inactive | [optional] 

## Example

```python
from okta.models.org_cross_app_access_connection import OrgCrossAppAccessConnection

# TODO update the JSON string below
json = "{}"
# create an instance of OrgCrossAppAccessConnection from a JSON string
org_cross_app_access_connection_instance = OrgCrossAppAccessConnection.from_json(json)
# print the JSON string representation of the object
print(OrgCrossAppAccessConnection.to_json())

# convert the object into a dict
org_cross_app_access_connection_dict = org_cross_app_access_connection_instance.to_dict()
# create an instance of OrgCrossAppAccessConnection from a dict
org_cross_app_access_connection_from_dict = OrgCrossAppAccessConnection.from_dict(org_cross_app_access_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


