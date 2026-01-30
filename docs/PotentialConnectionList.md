# PotentialConnectionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PotentialConnection]**](PotentialConnection.md) | Potential connections that can be established | 
**links** | [**PotentialConnectionListLinks**](PotentialConnectionListLinks.md) |  | 

## Example

```python
from okta.models.potential_connection_list import PotentialConnectionList

# TODO update the JSON string below
json = "{}"
# create an instance of PotentialConnectionList from a JSON string
potential_connection_list_instance = PotentialConnectionList.from_json(json)
# print the JSON string representation of the object
print(PotentialConnectionList.to_json())

# convert the object into a dict
potential_connection_list_dict = potential_connection_list_instance.to_dict()
# create an instance of PotentialConnectionList from a dict
potential_connection_list_from_dict = PotentialConnectionList.from_dict(potential_connection_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


