# EmailContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The HTML body of the email. May contain [variable references](https://velocity.apache.org/engine/1.7/user-guide.html#references).  &lt;x-lifecycle class&#x3D;\&quot;ea\&quot;&gt;&lt;/x-lifecycle&gt; Not required if Custom languages for Okta Email Templates is enabled. A &#x60;null&#x60; body is replaced with a default value from one of the following in priority order:  1. An existing default email customization, if one exists 2. Okta-provided translated content for the specified language, if one exists 3. Okta-provided translated content for the brand locale, if it&#39;s set 4. Okta-provided content in English  | 
**subject** | **str** | The email subject. May contain [variable references](https://velocity.apache.org/engine/1.7/user-guide.html#references).  &lt;x-lifecycle class&#x3D;\&quot;ea\&quot;&gt;&lt;/x-lifecycle&gt; Not required if Custom languages for Okta Email Templates is enabled. A &#x60;null&#x60; subject is replaced with a default value from one of the following in priority order:  1. An existing default email customization, if one exists 2. Okta-provided translated content for the specified language, if one exists 3. Okta-provided translated content for the brand locale, if it&#39;s set 4. Okta-provided content in English  | 

## Example

```python
from okta.models.email_content import EmailContent

# TODO update the JSON string below
json = "{}"
# create an instance of EmailContent from a JSON string
email_content_instance = EmailContent.from_json(json)
# print the JSON string representation of the object
print(EmailContent.to_json())

# convert the object into a dict
email_content_dict = email_content_instance.to_dict()
# create an instance of EmailContent from a dict
email_content_from_dict = EmailContent.from_dict(email_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


