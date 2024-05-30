# ErrorPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_content** | **str** |  | [optional] 
**content_security_policy_setting** | [**ContentSecurityPolicySetting**](ContentSecurityPolicySetting.md) |  | [optional] 

## Example

```python
from openapi_client.models.error_page import ErrorPage

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorPage from a JSON string
error_page_instance = ErrorPage.from_json(json)
# print the JSON string representation of the object
print(ErrorPage.to_json())

# convert the object into a dict
error_page_dict = error_page_instance.to_dict()
# create an instance of ErrorPage from a dict
error_page_form_dict = error_page.from_dict(error_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


