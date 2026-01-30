# ChildOrg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin** | [**OrgCreationAdmin**](OrgCreationAdmin.md) |  | 
**created** | **datetime** | Timestamp when the org was created | [optional] [readonly] 
**edition** | **str** | Edition for the org. &#x60;SKU&#x60; is the only supported value. | 
**id** | **str** | Org ID | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the org was last updated | [optional] [readonly] 
**name** | **str** | Unique name of the org. This name appears in the HTML &#x60;&lt;title&gt;&#x60; tag of the new org sign-in page. Only less than 4-width UTF-8 encoded characters are allowed. | 
**settings** | **Dict[str, object]** | Settings associated with the created org | [optional] [readonly] 
**status** | **str** | Status of the org. &#x60;ACTIVE&#x60; is returned after the org is created. | [optional] [readonly] 
**subdomain** | **str** | Subdomain of the org. Must be unique and include no spaces. | 
**token** | **str** | API token associated with the child org super admin account. Use this API token to provision resources (such as policies, apps, and groups) on the newly created child org. This token is revoked if the super admin account is deactivated. &gt; **Note:** If this API token expires, sign in to the Admin Console as the super admin user and create a new API token. See [Create an API token](https://developer.okta.com/docs/guides/create-an-api-token/). | [optional] [readonly] 
**token_type** | **str** | Type of returned &#x60;token&#x60;. See [Okta API tokens](https://developer.okta.com/docs/guides/create-an-api-token/main/#okta-api-tokens). | [optional] [readonly] 
**website** | **str** | Default website for the org | [optional] 
**links** | **Dict[str, object]** | Specifies available link relations (see [Web Linking](https://www.rfc-editor.org/rfc/rfc8288)) using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification | [optional] [readonly] 

## Example

```python
from okta.models.child_org import ChildOrg

# TODO update the JSON string below
json = "{}"
# create an instance of ChildOrg from a JSON string
child_org_instance = ChildOrg.from_json(json)
# print the JSON string representation of the object
print(ChildOrg.to_json())

# convert the object into a dict
child_org_dict = child_org_instance.to_dict()
# create an instance of ChildOrg from a dict
child_org_from_dict = ChildOrg.from_dict(child_org_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


