# CAPTCHAInstance



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique key for the CAPTCHA instance | [optional] [readonly] 
**name** | **str** | The name of the CAPTCHA instance | [optional] 
**secret_key** | **str** | The secret key issued from the CAPTCHA provider to perform server-side validation for a CAPTCHA token | [optional] 
**site_key** | **str** | The site key issued from the CAPTCHA provider to render a CAPTCHA on a page | [optional] 
**type** | [**CAPTCHAType**](CAPTCHAType.md) |  | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from openapi_client.models.captcha_instance import CAPTCHAInstance

# TODO update the JSON string below
json = "{}"
# create an instance of CAPTCHAInstance from a JSON string
captcha_instance_instance = CAPTCHAInstance.from_json(json)
# print the JSON string representation of the object
print(CAPTCHAInstance.to_json())

# convert the object into a dict
captcha_instance_dict = captcha_instance_instance.to_dict()
# create an instance of CAPTCHAInstance from a dict
captcha_instance_from_dict = CAPTCHAInstance.from_dict(captcha_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


