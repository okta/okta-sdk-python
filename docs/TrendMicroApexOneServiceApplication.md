# TrendMicroApexOneServiceApplication

Schema for Trend Micro Apex One as a Service app (key name: `trendmicroapexoneservice`)  To create a Trend Micro Apex One as a Service app, use the [Create an Application](/openapi/okta-management/management/tag/Application/#tag/Application/operation/createApplication) request with the following parameters in the request body. > **Note:** The Trend Micro Apex One as a Service app only supports `SAML_2_0` sign-on mode. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | [**ApplicationAccessibility**](ApplicationAccessibility.md) |  | [optional] 
**credentials** | [**SchemeApplicationCredentials**](SchemeApplicationCredentials.md) |  | [optional] 
**label** | **str** | User-defined display name for app | 
**licensing** | [**ApplicationLicensing**](ApplicationLicensing.md) |  | [optional] 
**name** | **str** |  | 
**profile** | **Dict[str, object]** | Contains any valid JSON schema for specifying properties that can be referenced from a request (only available to OAuth 2.0 client apps) | [optional] 
**sign_on_mode** | **str** |  | [optional] 
**status** | [**ApplicationLifecycleStatus**](ApplicationLifecycleStatus.md) |  | [optional] 
**visibility** | [**ApplicationVisibility**](ApplicationVisibility.md) |  | [optional] 
**settings** | [**TrendMicroApexOneServiceApplicationSettings**](TrendMicroApexOneServiceApplicationSettings.md) |  | 

## Example

```python
from okta.models.trend_micro_apex_one_service_application import TrendMicroApexOneServiceApplication

# TODO update the JSON string below
json = "{}"
# create an instance of TrendMicroApexOneServiceApplication from a JSON string
trend_micro_apex_one_service_application_instance = TrendMicroApexOneServiceApplication.from_json(json)
# print the JSON string representation of the object
print(TrendMicroApexOneServiceApplication.to_json())

# convert the object into a dict
trend_micro_apex_one_service_application_dict = trend_micro_apex_one_service_application_instance.to_dict()
# create an instance of TrendMicroApexOneServiceApplication from a dict
trend_micro_apex_one_service_application_from_dict = TrendMicroApexOneServiceApplication.from_dict(trend_micro_apex_one_service_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


