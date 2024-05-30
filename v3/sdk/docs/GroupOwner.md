# GroupOwner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name of the group owner | [optional] [readonly] 
**id** | **str** | The &#x60;id&#x60; of the group owner | [optional] 
**last_updated** | **datetime** | Timestamp when the group owner was last updated | [optional] [readonly] 
**origin_id** | **str** | The ID of the app instance if the &#x60;originType&#x60; is &#x60;APPLICATION&#x60;. This value is &#x60;NULL&#x60; if &#x60;originType&#x60; is &#x60;OKTA_DIRECTORY&#x60;. | [optional] 
**origin_type** | [**GroupOwnerOriginType**](GroupOwnerOriginType.md) |  | [optional] 
**resolved** | **bool** | If &#x60;originType&#x60;is APPLICATION, this parameter is set to &#x60;FALSE&#x60; until the owner’s &#x60;originId&#x60; is reconciled with an associated Okta ID. | [optional] 
**type** | [**GroupOwnerType**](GroupOwnerType.md) |  | [optional] 

## Example

```python
from openapi_client.models.group_owner import GroupOwner

# TODO update the JSON string below
json = "{}"
# create an instance of GroupOwner from a JSON string
group_owner_instance = GroupOwner.from_json(json)
# print the JSON string representation of the object
print(GroupOwner.to_json())

# convert the object into a dict
group_owner_dict = group_owner_instance.to_dict()
# create an instance of GroupOwner from a dict
group_owner_form_dict = group_owner.from_dict(group_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


