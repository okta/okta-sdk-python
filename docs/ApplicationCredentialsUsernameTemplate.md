# ApplicationCredentialsUsernameTemplate

The template used to generate the username when the app is assigned through a group or directly to a user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**push_status** | **str** | Determines if the username is pushed to the app on updates for CUSTOM &#x60;type&#x60; | [optional] 
**template** | **str** | Mapping expression used to generate usernames.  The following are supported mapping expressions that are used with the &#x60;BUILT_IN&#x60; template type:  | Name                            | Template Expression                            | | ------------------------------- | ---------------------------------------------- | | AD Employee ID                  | &#x60;${source.employeeID}&#x60;                         | | AD SAM Account Name             | &#x60;${source.samAccountName}&#x60;                     | | AD SAM Account Name (lowercase) | &#x60;${fn:toLowerCase(source.samAccountName)}&#x60;     | | AD User Principal Name          | &#x60;${source.userName}&#x60;                           | | AD User Principal Name prefix   | &#x60;${fn:substringBefore(source.userName, \&quot;@\&quot;)}&#x60;  | | Email                           | &#x60;${source.email}&#x60;                              | | Email (lowercase)               | &#x60;${fn:toLowerCase(source.email)}&#x60;              | | Email prefix                    | &#x60;${fn:substringBefore(source.email, \&quot;@\&quot;)}&#x60;     | | LDAP UID + custom suffix        | &#x60;${source.userName}${instance.userSuffix}&#x60;     | | Okta username                   | &#x60;${source.login}&#x60;                              | | Okta username prefix            | &#x60;${fn:substringBefore(source.login, \&quot;@\&quot;)}&#x60;     | | [optional] [default to '${source.login}']
**type** | **str** | Type of mapping expression. Empty string is allowed. | [optional] [default to 'BUILT_IN']
**user_suffix** | **str** | An optional suffix appended to usernames for &#x60;BUILT_IN&#x60; mapping expressions | [optional] 

## Example

```python
from okta.models.application_credentials_username_template import ApplicationCredentialsUsernameTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCredentialsUsernameTemplate from a JSON string
application_credentials_username_template_instance = ApplicationCredentialsUsernameTemplate.from_json(json)
# print the JSON string representation of the object
print(ApplicationCredentialsUsernameTemplate.to_json())

# convert the object into a dict
application_credentials_username_template_dict = application_credentials_username_template_instance.to_dict()
# create an instance of ApplicationCredentialsUsernameTemplate from a dict
application_credentials_username_template_from_dict = ApplicationCredentialsUsernameTemplate.from_dict(application_credentials_username_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


