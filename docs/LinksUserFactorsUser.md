# LinksUserFactorsUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hints** | [**HrefHints**](HrefHints.md) |  | [optional] 
**href** | **str** | Link URI | 
**name** | **str** | Link name | [optional] [readonly] 
**templated** | **bool** | Indicates whether the link object&#39;s &#x60;href&#x60; property is a URI template. | [optional] [readonly] 
**type** | **str** | The media type of the link. If omitted, it is implicitly &#x60;application/json&#x60;. | [optional] [readonly] 

## Example

```python
from okta.models.links_user_factors_user import LinksUserFactorsUser

# TODO update the JSON string below
json = "{}"
# create an instance of LinksUserFactorsUser from a JSON string
links_user_factors_user_instance = LinksUserFactorsUser.from_json(json)
# print the JSON string representation of the object
print(LinksUserFactorsUser.to_json())

# convert the object into a dict
links_user_factors_user_dict = links_user_factors_user_instance.to_dict()
# create an instance of LinksUserFactorsUser from a dict
links_user_factors_user_from_dict = LinksUserFactorsUser.from_dict(links_user_factors_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


