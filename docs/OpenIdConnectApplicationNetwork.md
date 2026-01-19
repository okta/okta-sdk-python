# OpenIdConnectApplicationNetwork

The network restrictions of the client

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection** | **str** | The connection type of the network. Can be &#x60;ANYWHERE&#x60; or &#x60;ZONE&#x60;.  | 
**exclude** | **List[str]** | If &#x60;ZONE&#x60; is specified as a connection, then specify the excluded IP network zones here. Value can be \&quot;ALL_IP_ZONES\&quot; or an array of zone IDs. | [optional] 
**include** | **List[str]** | If &#x60;ZONE&#x60; is specified as a connection, then specify the included IP network zones here. Value can be \&quot;ALL_IP_ZONES\&quot; or an array of zone IDs. | [optional] 

## Example

```python
from okta.models.open_id_connect_application_network import OpenIdConnectApplicationNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of OpenIdConnectApplicationNetwork from a JSON string
open_id_connect_application_network_instance = OpenIdConnectApplicationNetwork.from_json(json)
# print the JSON string representation of the object
print(OpenIdConnectApplicationNetwork.to_json())

# convert the object into a dict
open_id_connect_application_network_dict = open_id_connect_application_network_instance.to_dict()
# create an instance of OpenIdConnectApplicationNetwork from a dict
open_id_connect_application_network_from_dict = OpenIdConnectApplicationNetwork.from_dict(open_id_connect_application_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


