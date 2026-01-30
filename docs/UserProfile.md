# UserProfile

Specifies the default and custom profile properties for a user.  The default user profile is based on the [System for Cross-domain Identity Management: Core Schema](https://datatracker.ietf.org/doc/html/rfc7643).  The only permitted customizations of the default profile are to update permissions, change whether the `firstName` and `lastName` properties are nullable, and specify a [pattern](https://developer.okta.com/docs/reference/api/schemas/#login-pattern-validation) for `login`. You can use the Profile Editor in the Admin Console or the [Schemas API](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/UISchema/#tag/UISchema) to make schema modifications.  You can extend user profiles with custom properties. You must first add the custom property to the user profile schema before you reference it. You can use the Profile Editor in the Admin Console or the [Schemas API](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/UISchema/#tag/UISchema) to manage schema extensions.  Custom attributes can contain HTML tags. It's the client's responsibility to escape or encode this data before displaying it. Use [best-practices](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html) to prevent cross-site scripting.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | The city or locality of the user&#39;s address (&#x60;locality&#x60;) | [optional] 
**cost_center** | **str** | Name of the cost center assigned to a user | [optional] 
**country_code** | **str** | The country name component of the user&#39;s address (&#x60;country&#x60;). For validation, see [ISO 3166-1 alpha 2 \&quot;short\&quot; code format](https://datatracker.ietf.org/doc/html/draft-ietf-scim-core-schema-22#ref-ISO3166). | [optional] 
**department** | **str** | Name of the user&#39;s department | [optional] 
**display_name** | **str** | Name of the user suitable for display to end users | [optional] 
**division** | **str** | Name of the user&#39;s division | [optional] 
**email** | **str** | The primary email address of the user. For validation, see [RFC 5322 Section 3.2.3](https://datatracker.ietf.org/doc/html/rfc5322#section-3.2.3). | [optional] 
**employee_number** | **str** | The organization or company assigned unique identifier for the user | [optional] 
**first_name** | **str** | Given name of the user (&#x60;givenName&#x60;) | [optional] 
**honorific_prefix** | **str** | Honorific prefix(es) of the user, or title in most Western languages | [optional] 
**honorific_suffix** | **str** | Honorific suffix(es) of the user | [optional] 
**last_name** | **str** | The family name of the user (&#x60;familyName&#x60;) | [optional] 
**locale** | **str** | The user&#39;s default location for purposes of localizing items such as currency, date time format, numerical representations, and so on. A locale value is a concatenation of the ISO 639-1 two-letter language code, an underscore, and the ISO 3166-1 two-letter country code. For example, en_US specifies the language English and country US. This value is &#x60;en_US&#x60; by default. | [optional] 
**login** | **str** | The unique identifier for the user (&#x60;username&#x60;). For validation, see [Login pattern validation](https://developer.okta.com/docs/reference/api/schemas/#login-pattern-validation).  Every user within your Okta org must have a unique identifier for a login. This constraint applies to all users you import from other systems or applications such as Active Directory. Your organization is the top-level namespace to mix and match logins from all your connected applications or directories. Careful consideration of naming conventions for your login identifier will make it easier to onboard new applications in the future.  Logins are not considered unique if they differ only in case and/or diacritical marks. If one of your users has a login of Isaac.Brock@example.com, there cannot be another user whose login is isaac.brock@example.com, nor isáàc.bröck@example.com.  Okta has a default ambiguous name resolution policy for usernames that include @-signs. (By default, usernames must be formatted as email addresses and thus always include @-signs. You can remove that restriction using either the Admin Console or the [Schemas API](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Schema/). Users can sign in with their non-qualified short name (for example: isaac.brock with username isaac.brock@example.com) as long as the short name is still unique within the organization. maxLength: 100 | [optional] 
**manager** | **str** | The &#x60;displayName&#x60; of the user&#39;s manager | [optional] 
**manager_id** | **str** | The &#x60;id&#x60; of the user&#39;s manager | [optional] 
**middle_name** | **str** | The middle name of the user | [optional] 
**mobile_phone** | **str** | The mobile phone number of the user | [optional] 
**nick_name** | **str** | The casual way to address the user in real life | [optional] 
**organization** | **str** | Name of the the user&#39;s organization | [optional] 
**postal_address** | **str** | Mailing address component of the user&#39;s address | [optional] 
**preferred_language** | **str** | The user&#39;s preferred written or spoken language. For validation, see [RFC 7231 Section 5.3.5](https://datatracker.ietf.org/doc/html/rfc7231#section-5.3.5). | [optional] 
**primary_phone** | **str** | The primary phone number of the user such as a home number | [optional] 
**profile_url** | **str** | The URL of the user&#39;s online profile. For example, a web page. See [URL](https://datatracker.ietf.org/doc/html/rfc1808). | [optional] 
**second_email** | **str** | The secondary email address of the user typically used for account recovery. For validation, see [RFC 5322 Section 3.2.3](https://datatracker.ietf.org/doc/html/rfc5322#section-3.2.3). | [optional] 
**state** | **str** | The state or region component of the user&#39;s address (&#x60;region&#x60;) | [optional] 
**street_address** | **str** | The full street address component of the user&#39;s address | [optional] 
**timezone** | **str** | The user&#39;s time zone | [optional] 
**title** | **str** | The user&#39;s title, such as Vice President | [optional] 
**user_type** | **str** | The property used to describe the organization-to-user relationship, such as employee or contractor | [optional] 
**zip_code** | **str** | The ZIP code or postal code component of the user&#39;s address (&#x60;postalCode&#x60;) | [optional] 

## Example

```python
from okta.models.user_profile import UserProfile

# TODO update the JSON string below
json = "{}"
# create an instance of UserProfile from a JSON string
user_profile_instance = UserProfile.from_json(json)
# print the JSON string representation of the object
print(UserProfile.to_json())

# convert the object into a dict
user_profile_dict = user_profile_instance.to_dict()
# create an instance of UserProfile from a dict
user_profile_from_dict = UserProfile.from_dict(user_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


