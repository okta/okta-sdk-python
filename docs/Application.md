# Application


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | [**ApplicationAccessibility**](ApplicationAccessibility.md) |  | [optional] 
**created** | **datetime** | Timestamp when the application object was created | [optional] [readonly] 
**express_configuration** | [**ApplicationExpressConfiguration**](ApplicationExpressConfiguration.md) |  | [optional] 
**features** | **List[str]** | Enabled app features &gt; **Note:** See [Application Features](/openapi/okta-management/management/tag/ApplicationFeatures/) for app provisioning features.  | [optional] [readonly] 
**id** | **str** | Unique ID for the app instance | [optional] [readonly] 
**label** | **str** | User-defined display name for app | 
**last_updated** | **datetime** | Timestamp when the application object was last updated | [optional] [readonly] 
**licensing** | [**ApplicationLicensing**](ApplicationLicensing.md) |  | [optional] 
**orn** | **str** | The Okta resource name (ORN) for the current app instance | [optional] [readonly] 
**profile** | **Dict[str, object]** | Contains any valid JSON schema for specifying properties that can be referenced from a request (only available to OAuth 2.0 client apps). For example, add an app manager contact email address or define an allowlist of groups that you can then reference using the Okta Expression Language &#x60;getFilteredGroups&#x60; function.  &gt; **Notes:** &gt; * &#x60;profile&#x60; isn&#39;t encrypted, so don&#39;t store sensitive data in it. &gt; * &#x60;profile&#x60; doesn&#39;t limit the level of nesting in the JSON schema you created, but there is a practical size limit. Okta recommends a JSON schema size of 1 MB or less for best performance. | [optional] 
**sign_on_mode** | [**ApplicationSignOnMode**](ApplicationSignOnMode.md) |  | 
**status** | [**ApplicationLifecycleStatus**](ApplicationLifecycleStatus.md) |  | [optional] 
**universal_logout** | [**ApplicationUniversalLogout**](ApplicationUniversalLogout.md) |  | [optional] 
**visibility** | [**ApplicationVisibility**](ApplicationVisibility.md) |  | [optional] 
**embedded** | [**ApplicationEmbedded**](ApplicationEmbedded.md) |  | [optional] 
**links** | [**ApplicationLinks**](ApplicationLinks.md) |  | [optional] 

## Example

```python
from okta.models.application import Application

# TODO update the JSON string below
json = "{}"
# create an instance of Application from a JSON string
application_instance = Application.from_json(json)
# print the JSON string representation of the object
print(Application.to_json())

# convert the object into a dict
application_dict = application_instance.to_dict()
# create an instance of Application from a dict
application_from_dict = Application.from_dict(application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


