# EmailTestAddresses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | An email address to send the test email from | 
**to** | **str** | An email address to send the test email to | 

## Example

```python
from okta.models.email_test_addresses import EmailTestAddresses

# TODO update the JSON string below
json = "{}"
# create an instance of EmailTestAddresses from a JSON string
email_test_addresses_instance = EmailTestAddresses.from_json(json)
# print the JSON string representation of the object
print(EmailTestAddresses.to_json())

# convert the object into a dict
email_test_addresses_dict = email_test_addresses_instance.to_dict()
# create an instance of EmailTestAddresses from a dict
email_test_addresses_from_dict = EmailTestAddresses.from_dict(email_test_addresses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


