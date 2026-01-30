# SubmissionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[SubmissionAction]**](SubmissionAction.md) | List of actions supported by this integration | [optional] 
**app_contact_details** | [**List[SubmissionResponseAppContactDetailsInner]**](SubmissionResponseAppContactDetailsInner.md) | List of contact details for the app integration | [optional] 
**var_auth_settings** | [**AuthSettings**](AuthSettings.md) |  | [optional] 
**capabilities** | [**List[SubmissionCapability]**](SubmissionCapability.md) | List of capabilities supported by this integration | [optional] 
**config** | [**List[SubmissionResponseConfigInner]**](SubmissionResponseConfigInner.md) | List of org-level variables for the customer per-tenant configuration. For example, a &#x60;subdomain&#x60; variable can be used in the ACS URL: &#x60;https://${org.subdomain}.example.com/saml/login&#x60; | [optional] 
**description** | **str** | A general description of your application and the benefits provided to your customers | [optional] 
**global_token_revocation** | [**SubmissionResponseGlobalTokenRevocation**](SubmissionResponseGlobalTokenRevocation.md) |  | [optional] 
**id** | **str** | OIN Integration ID | [optional] [readonly] 
**last_published** | **str** | Timestamp when the OIN Integration was last published | [optional] [readonly] 
**last_updated** | **str** | Timestamp when the OIN Integration instance was last updated | [optional] [readonly] 
**last_updated_by** | **str** | ID of the user who made the last update | [optional] [readonly] 
**logo** | **str** | URL to an uploaded application logo. This logo appears next to your app integration name in the OIN catalog. You must first [Upload an OIN Integration logo](/openapi/okta-management/management/tag/YourOinIntegrations/#tag/YourOinIntegrations/operation/uploadSubmissionLogo) to obtain the logo URL before you can specify this value. | [optional] 
**name** | **str** | The app integration name. This is the main title used for your integration in the OIN catalog. | [optional] 
**provisioning** | [**ProvisioningDetails**](ProvisioningDetails.md) |  | [optional] 
**sso** | [**Sso**](Sso.md) |  | [optional] 
**status** | **str** | Status of the OIN Integration submission | [optional] [readonly] 

## Example

```python
from okta.models.submission_response import SubmissionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionResponse from a JSON string
submission_response_instance = SubmissionResponse.from_json(json)
# print the JSON string representation of the object
print(SubmissionResponse.to_json())

# convert the object into a dict
submission_response_dict = submission_response_instance.to_dict()
# create an instance of SubmissionResponse from a dict
submission_response_from_dict = SubmissionResponse.from_dict(submission_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


