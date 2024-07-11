# EmailDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand_id** | **str** |  | 
**domain** | **str** |  | 
**display_name** | **str** |  | 
**user_name** | **str** |  | 

## Example

```python
from openapi_client.models.email_domain import EmailDomain

# TODO update the JSON string below
json = "{}"
# create an instance of EmailDomain from a JSON string
email_domain_instance = EmailDomain.from_json(json)
# print the JSON string representation of the object
print(EmailDomain.to_json())

# convert the object into a dict
email_domain_dict = email_domain_instance.to_dict()
# create an instance of EmailDomain from a dict
email_domain_from_dict = EmailDomain.from_dict(email_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


