# HrefHintsGuidanceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow** | [**List[HttpMethod]**](HttpMethod.md) |  | [optional] 
**guidance** | **List[str]** | Specifies the URI to invoke for granting scope consent required to complete the OAuth 2.0 connection  | [optional] 

## Example

```python
from okta.models.href_hints_guidance_object import HrefHintsGuidanceObject

# TODO update the JSON string below
json = "{}"
# create an instance of HrefHintsGuidanceObject from a JSON string
href_hints_guidance_object_instance = HrefHintsGuidanceObject.from_json(json)
# print the JSON string representation of the object
print(HrefHintsGuidanceObject.to_json())

# convert the object into a dict
href_hints_guidance_object_dict = href_hints_guidance_object_instance.to_dict()
# create an instance of HrefHintsGuidanceObject from a dict
href_hints_guidance_object_from_dict = HrefHintsGuidanceObject.from_dict(href_hints_guidance_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


