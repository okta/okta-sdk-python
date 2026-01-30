# EmailCustomization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The HTML body of the email. May contain [variable references](https://velocity.apache.org/engine/1.7/user-guide.html#references).  &lt;x-lifecycle class&#x3D;\&quot;ea\&quot;&gt;&lt;/x-lifecycle&gt; Not required if Custom languages for Okta Email Templates is enabled. A &#x60;null&#x60; body is replaced with a default value from one of the following in priority order:  1. An existing default email customization, if one exists 2. Okta-provided translated content for the specified language, if one exists 3. Okta-provided translated content for the brand locale, if it&#39;s set 4. Okta-provided content in English  | 
**subject** | **str** | The email subject. May contain [variable references](https://velocity.apache.org/engine/1.7/user-guide.html#references).  &lt;x-lifecycle class&#x3D;\&quot;ea\&quot;&gt;&lt;/x-lifecycle&gt; Not required if Custom languages for Okta Email Templates is enabled. A &#x60;null&#x60; subject is replaced with a default value from one of the following in priority order:  1. An existing default email customization, if one exists 2. Okta-provided translated content for the specified language, if one exists 3. Okta-provided translated content for the brand locale, if it&#39;s set 4. Okta-provided content in English  | 
**created** | **datetime** | The UTC time at which this email customization was created. | [optional] [readonly] 
**id** | **str** | A unique identifier for this email customization | [optional] [readonly] 
**is_default** | **bool** | Whether this is the default customization for the email template. Each customized email template must have exactly one default customization. Defaults to &#x60;true&#x60; for the first customization and &#x60;false&#x60; thereafter. | [optional] 
**language** | **str** | The language specified as an [IETF BCP 47 language tag](https://datatracker.ietf.org/doc/html/rfc5646) | 
**last_updated** | **datetime** | The UTC time at which this email customization was last updated. | [optional] [readonly] 
**links** | [**EmailCustomizationAllOfLinks**](EmailCustomizationAllOfLinks.md) |  | [optional] 

## Example

```python
from okta.models.email_customization import EmailCustomization

# TODO update the JSON string below
json = "{}"
# create an instance of EmailCustomization from a JSON string
email_customization_instance = EmailCustomization.from_json(json)
# print the JSON string representation of the object
print(EmailCustomization.to_json())

# convert the object into a dict
email_customization_dict = email_customization_instance.to_dict()
# create an instance of EmailCustomization from a dict
email_customization_from_dict = EmailCustomization.from_dict(email_customization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


