# TrustedOriginWrite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique name for the trusted origin | [optional] 
**origin** | **str** | Unique origin URL for the trusted origin. The supported schemes for this attribute are HTTP, HTTPS, FTP, Ionic 2, and Capacitor. | [optional] 
**scopes** | [**List[TrustedOriginScope]**](TrustedOriginScope.md) | Array of scope types that this trusted origin is used for | [optional] 

## Example

```python
from okta.models.trusted_origin_write import TrustedOriginWrite

# TODO update the JSON string below
json = "{}"
# create an instance of TrustedOriginWrite from a JSON string
trusted_origin_write_instance = TrustedOriginWrite.from_json(json)
# print the JSON string representation of the object
print(TrustedOriginWrite.to_json())

# convert the object into a dict
trusted_origin_write_dict = trusted_origin_write_instance.to_dict()
# create an instance of TrustedOriginWrite from a dict
trusted_origin_write_from_dict = TrustedOriginWrite.from_dict(trusted_origin_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


