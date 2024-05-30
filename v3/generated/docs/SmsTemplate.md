# SmsTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**last_updated** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**template** | **str** |  | [optional] 
**translations** | **object** |  | [optional] 
**type** | [**SmsTemplateType**](SmsTemplateType.md) |  | [optional] 

## Example

```python
from openapi_client.models.sms_template import SmsTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of SmsTemplate from a JSON string
sms_template_instance = SmsTemplate.from_json(json)
# print the JSON string representation of the object
print(SmsTemplate.to_json())

# convert the object into a dict
sms_template_dict = sms_template_instance.to_dict()
# create an instance of SmsTemplate from a dict
sms_template_form_dict = sms_template.from_dict(sms_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


