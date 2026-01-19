# BouncesRemoveListObj


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_addresses** | **List[str]** | A list of email addresses to remove from the email-service bounce list | [optional] 

## Example

```python
from okta.models.bounces_remove_list_obj import BouncesRemoveListObj

# TODO update the JSON string below
json = "{}"
# create an instance of BouncesRemoveListObj from a JSON string
bounces_remove_list_obj_instance = BouncesRemoveListObj.from_json(json)
# print the JSON string representation of the object
print(BouncesRemoveListObj.to_json())

# convert the object into a dict
bounces_remove_list_obj_dict = bounces_remove_list_obj_instance.to_dict()
# create an instance of BouncesRemoveListObj from a dict
bounces_remove_list_obj_from_dict = BouncesRemoveListObj.from_dict(bounces_remove_list_obj_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


