# RateLimitWarningThresholdResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warning_threshold** | **int** | The threshold value (percentage) of a rate limit that, when exceeded, triggers a warning notification. By default, this value is 90 for Workforce orgs and 60 for CIAM orgs. | [optional] 

## Example

```python
from openapi_client.models.rate_limit_warning_threshold_response import RateLimitWarningThresholdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RateLimitWarningThresholdResponse from a JSON string
rate_limit_warning_threshold_response_instance = RateLimitWarningThresholdResponse.from_json(json)
# print the JSON string representation of the object
print(RateLimitWarningThresholdResponse.to_json())

# convert the object into a dict
rate_limit_warning_threshold_response_dict = rate_limit_warning_threshold_response_instance.to_dict()
# create an instance of RateLimitWarningThresholdResponse from a dict
rate_limit_warning_threshold_response_from_dict = RateLimitWarningThresholdResponse.from_dict(rate_limit_warning_threshold_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


