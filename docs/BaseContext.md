# BaseContext

This object contains a number of sub-objects, each of which provide some type of contextual information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**InlineHookRequestObject**](InlineHookRequestObject.md) |  | [optional] 
**session** | [**BaseContextSession**](BaseContextSession.md) |  | [optional] 
**user** | [**BaseContextUser**](BaseContextUser.md) |  | [optional] 

## Example

```python
from okta.models.base_context import BaseContext

# TODO update the JSON string below
json = "{}"
# create an instance of BaseContext from a JSON string
base_context_instance = BaseContext.from_json(json)
# print the JSON string representation of the object
print(BaseContext.to_json())

# convert the object into a dict
base_context_dict = base_context_instance.to_dict()
# create an instance of BaseContext from a dict
base_context_from_dict = BaseContext.from_dict(base_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


