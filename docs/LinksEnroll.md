# LinksEnroll


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enroll** | [**LinksEnrollEnroll**](LinksEnrollEnroll.md) |  | [optional] 

## Example

```python
from okta.models.links_enroll import LinksEnroll

# TODO update the JSON string below
json = "{}"
# create an instance of LinksEnroll from a JSON string
links_enroll_instance = LinksEnroll.from_json(json)
# print the JSON string representation of the object
print(LinksEnroll.to_json())

# convert the object into a dict
links_enroll_dict = links_enroll_instance.to_dict()
# create an instance of LinksEnroll from a dict
links_enroll_from_dict = LinksEnroll.from_dict(links_enroll_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


