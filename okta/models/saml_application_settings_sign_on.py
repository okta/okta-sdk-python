"""
Copyright 2020 - Present Okta, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# AUTO-GENERATED! DO NOT EDIT FILE DIRECTLY
# SEE CONTRIBUTOR DOCUMENTATION


class SamlApplicationSettingsSignOn:
    def __init__(self, config=None):
        if config:
            self.assertion_signed = config["assertionSigned"]
            self.attribute_statements = config["attributeStatements"]
            self.audience = config["audience"]
            self.audience_override = config["audienceOverride"]
            self.authn_context_class_ref = config["authnContextClassRef"]
            self.default_relay_state = config["defaultRelayState"]
            self.destination = config["destination"]
            self.destination_override = config["destinationOverride"]
            self.digest_algorithm = config["digestAlgorithm"]
            self.honor_force_authn = config["honorForceAuthn"]
            self.idp_issuer = config["idpIssuer"]
            self.recipient = config["recipient"]
            self.recipient_override = config["recipientOverride"]
            self.request_compressed = config["requestCompressed"]
            self.response_signed = config["responseSigned"]
            self.signature_algorithm = config["signatureAlgorithm"]
            self.sp_issuer = config["spIssuer"]
            self.sso_acs_url = config["ssoAcsUrl"]
            self.sso_acs_url_override = config["ssoAcsUrlOverride"]
            self.subject_name_id_format = config["subjectNameIdFormat"]
            self.subject_name_id_template = config["subjectNameIdTemplate"]
        else:
            self.assertion_signed = None
            self.attribute_statements = None
            self.audience = None
            self.audience_override = None
            self.authn_context_class_ref = None
            self.default_relay_state = None
            self.destination = None
            self.destination_override = None
            self.digest_algorithm = None
            self.honor_force_authn = None
            self.idp_issuer = None
            self.recipient = None
            self.recipient_override = None
            self.request_compressed = None
            self.response_signed = None
            self.signature_algorithm = None
            self.sp_issuer = None
            self.sso_acs_url = None
            self.sso_acs_url_override = None
            self.subject_name_id_format = None
            self.subject_name_id_template = None

# End of File Generation
