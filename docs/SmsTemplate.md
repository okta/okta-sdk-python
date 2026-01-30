# SmsTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**last_updated** | **datetime** |  | [optional] [readonly] 
**name** | **str** | Human-readable name of the Template | [optional] 
**template** | **str** | Text of the Template, including any [macros](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Template/) | [optional] 
**translations** | **object** | - Template translations are optionally provided when you want to localize the SMS messages. Translations are provided as an object that contains &#x60;key:value&#x60; pairs: the language and the translated Template text. The key portion is a two-letter country code that conforms to [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php). The value is the translated SMS Template. - Just like with regular SMS Templates, the length of the SMS message can&#39;t exceed 160 characters.  | [optional] 
**type** | [**SmsTemplateType**](SmsTemplateType.md) |  | [optional] 

## Example

```python
from okta.models.sms_template import SmsTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of SmsTemplate from a JSON string
sms_template_instance = SmsTemplate.from_json(json)
# print the JSON string representation of the object
print(SmsTemplate.to_json())

# convert the object into a dict
sms_template_dict = sms_template_instance.to_dict()
# create an instance of SmsTemplate from a dict
sms_template_from_dict = SmsTemplate.from_dict(sms_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


