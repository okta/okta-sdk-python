# VerifyUserFactorResponseLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**poll** | [**HrefObject**](HrefObject.md) |  | [optional] 
**cancel** | [**HrefObject**](HrefObject.md) |  | [optional] 

## Example

```python
from openapi_client.models.verify_user_factor_response_links import VerifyUserFactorResponseLinks

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyUserFactorResponseLinks from a JSON string
verify_user_factor_response_links_instance = VerifyUserFactorResponseLinks.from_json(json)
# print the JSON string representation of the object
print(VerifyUserFactorResponseLinks.to_json())

# convert the object into a dict
verify_user_factor_response_links_dict = verify_user_factor_response_links_instance.to_dict()
# create an instance of VerifyUserFactorResponseLinks from a dict
verify_user_factor_response_links_form_dict = verify_user_factor_response_links.from_dict(verify_user_factor_response_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


