# UserFactorLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activate** | [**LinksActivateActivate**](LinksActivateActivate.md) |  | [optional] 
**cancel** | [**LinksCancelCancel**](LinksCancelCancel.md) |  | [optional] 
**deactivate** | [**LinksDeactivateDeactivate**](LinksDeactivateDeactivate.md) |  | [optional] 
**enroll** | [**LinksEnrollEnroll**](LinksEnrollEnroll.md) |  | [optional] 
**factor** | [**LinksFactorFactor**](LinksFactorFactor.md) |  | [optional] 
**poll** | [**LinksPollPoll**](LinksPollPoll.md) |  | [optional] 
**qrcode** | [**LinksQrcodeQrcode**](LinksQrcodeQrcode.md) |  | [optional] 
**question** | [**LinksQuestionsQuestion**](LinksQuestionsQuestion.md) |  | [optional] 
**resend** | [**LinksResendResend**](LinksResendResend.md) |  | [optional] 
**send** | [**LinksSendSend**](LinksSendSend.md) |  | [optional] 
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**user** | [**LinksUserFactorsUser**](LinksUserFactorsUser.md) |  | [optional] 
**verify** | [**LinksVerifyVerify**](LinksVerifyVerify.md) |  | [optional] 

## Example

```python
from okta.models.user_factor_links import UserFactorLinks

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorLinks from a JSON string
user_factor_links_instance = UserFactorLinks.from_json(json)
# print the JSON string representation of the object
print(UserFactorLinks.to_json())

# convert the object into a dict
user_factor_links_dict = user_factor_links_instance.to_dict()
# create an instance of UserFactorLinks from a dict
user_factor_links_from_dict = UserFactorLinks.from_dict(user_factor_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


