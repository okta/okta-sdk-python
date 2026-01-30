# OrganizationalUnit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the organizational unit where privileged app users are present | 

## Example

```python
from okta.models.organizational_unit import OrganizationalUnit

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationalUnit from a JSON string
organizational_unit_instance = OrganizationalUnit.from_json(json)
# print the JSON string representation of the object
print(OrganizationalUnit.to_json())

# convert the object into a dict
organizational_unit_dict = organizational_unit_instance.to_dict()
# create an instance of OrganizationalUnit from a dict
organizational_unit_from_dict = OrganizationalUnit.from_dict(organizational_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


