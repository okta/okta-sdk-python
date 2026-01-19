# TrustedOrigin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the trusted origin was created | [optional] [readonly] 
**created_by** | **str** | The ID of the user who created the trusted origin | [optional] 
**id** | **str** | Unique identifier for the trusted origin | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the trusted origin was last updated | [optional] [readonly] 
**last_updated_by** | **str** | The ID of the user who last updated the trusted origin | [optional] 
**name** | **str** | Unique name for the trusted origin | [optional] 
**origin** | **str** | Unique origin URL for the trusted origin. The supported schemes for this attribute are HTTP, HTTPS, FTP, Ionic 2, and Capacitor. | [optional] 
**scopes** | [**List[TrustedOriginScope]**](TrustedOriginScope.md) | Array of scope types that this trusted origin is used for | [optional] 
**status** | [**LifecycleStatus**](LifecycleStatus.md) |  | [optional] 
**links** | [**LinksSelfAndLifecycle**](LinksSelfAndLifecycle.md) |  | [optional] 

## Example

```python
from okta.models.trusted_origin import TrustedOrigin

# TODO update the JSON string below
json = "{}"
# create an instance of TrustedOrigin from a JSON string
trusted_origin_instance = TrustedOrigin.from_json(json)
# print the JSON string representation of the object
print(TrustedOrigin.to_json())

# convert the object into a dict
trusted_origin_dict = trusted_origin_instance.to_dict()
# create an instance of TrustedOrigin from a dict
trusted_origin_from_dict = TrustedOrigin.from_dict(trusted_origin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


