# LinksSelfLifecycleAndAuthorize


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**activate** | [**HrefObjectActivateLink**](HrefObjectActivateLink.md) |  | [optional] 
**deactivate** | [**HrefObjectDeactivateLink**](HrefObjectDeactivateLink.md) |  | [optional] 
**authorize** | [**HrefObjectAuthorizeLink**](HrefObjectAuthorizeLink.md) |  | [optional] 

## Example

```python
from okta.models.links_self_lifecycle_and_authorize import LinksSelfLifecycleAndAuthorize

# TODO update the JSON string below
json = "{}"
# create an instance of LinksSelfLifecycleAndAuthorize from a JSON string
links_self_lifecycle_and_authorize_instance = LinksSelfLifecycleAndAuthorize.from_json(json)
# print the JSON string representation of the object
print(LinksSelfLifecycleAndAuthorize.to_json())

# convert the object into a dict
links_self_lifecycle_and_authorize_dict = links_self_lifecycle_and_authorize_instance.to_dict()
# create an instance of LinksSelfLifecycleAndAuthorize from a dict
links_self_lifecycle_and_authorize_from_dict = LinksSelfLifecycleAndAuthorize.from_dict(links_self_lifecycle_and_authorize_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


