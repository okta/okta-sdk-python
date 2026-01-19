# LinksUserFactors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**LinksUserFactorsUser**](LinksUserFactorsUser.md) |  | [optional] 

## Example

```python
from okta.models.links_user_factors import LinksUserFactors

# TODO update the JSON string below
json = "{}"
# create an instance of LinksUserFactors from a JSON string
links_user_factors_instance = LinksUserFactors.from_json(json)
# print the JSON string representation of the object
print(LinksUserFactors.to_json())

# convert the object into a dict
links_user_factors_dict = links_user_factors_instance.to_dict()
# create an instance of LinksUserFactors from a dict
links_user_factors_from_dict = LinksUserFactors.from_dict(links_user_factors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


