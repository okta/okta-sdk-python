# ManagedConnectionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ManagedConnection]**](ManagedConnection.md) | All connections the agent has established | 
**links** | [**ManagedConnectionListLinks**](ManagedConnectionListLinks.md) |  | 

## Example

```python
from okta.models.managed_connection_list import ManagedConnectionList

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedConnectionList from a JSON string
managed_connection_list_instance = ManagedConnectionList.from_json(json)
# print the JSON string representation of the object
print(ManagedConnectionList.to_json())

# convert the object into a dict
managed_connection_list_dict = managed_connection_list_instance.to_dict()
# create an instance of ManagedConnectionList from a dict
managed_connection_list_from_dict = ManagedConnectionList.from_dict(managed_connection_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


