# ThreatInsightConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specifies how Okta responds to authentication requests from suspicious IP addresses | 
**created** | **datetime** | Timestamp when the ThreatInsight Configuration object was created | [optional] [readonly] 
**exclude_zones** | **List[str]** | Accepts a list of [Network Zone](/openapi/okta-management/management/tag/NetworkZone/) IDs. IPs in the excluded network zones aren&#39;t logged or blocked. This ensures that traffic from known, trusted IPs isn&#39;t accidentally logged or blocked. | [optional] 
**last_updated** | **datetime** | Timestamp when the ThreatInsight Configuration object was last updated | [optional] [readonly] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.threat_insight_configuration import ThreatInsightConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ThreatInsightConfiguration from a JSON string
threat_insight_configuration_instance = ThreatInsightConfiguration.from_json(json)
# print the JSON string representation of the object
print(ThreatInsightConfiguration.to_json())

# convert the object into a dict
threat_insight_configuration_dict = threat_insight_configuration_instance.to_dict()
# create an instance of ThreatInsightConfiguration from a dict
threat_insight_configuration_from_dict = ThreatInsightConfiguration.from_dict(threat_insight_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


