# SingleLogout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**issuer** | **str** |  | [optional] 
**logout_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.single_logout import SingleLogout

# TODO update the JSON string below
json = "{}"
# create an instance of SingleLogout from a JSON string
single_logout_instance = SingleLogout.from_json(json)
# print the JSON string representation of the object
print(SingleLogout.to_json())

# convert the object into a dict
single_logout_dict = single_logout_instance.to_dict()
# create an instance of SingleLogout from a dict
single_logout_from_dict = SingleLogout.from_dict(single_logout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


