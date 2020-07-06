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

from okta.okta_object import OktaObject


class SamlApplicationSettingsSignOn(
    OktaObject
):
    def __init__(self, config=None):
        if config:
            self.assertion_signed = config["assertionSigned"]\
                if "assertionSigned" in config else None
            self.attribute_statements = config["attributeStatements"]\
                if "attributeStatements" in config else None
            self.audience = config["audience"]\
                if "audience" in config else None
            self.audience_override = config["audienceOverride"]\
                if "audienceOverride" in config else None
            self.authn_context_class_ref = config["authnContextClassRef"]\
                if "authnContextClassRef" in config else None
            self.default_relay_state = config["defaultRelayState"]\
                if "defaultRelayState" in config else None
            self.destination = config["destination"]\
                if "destination" in config else None
            self.destination_override = config["destinationOverride"]\
                if "destinationOverride" in config else None
            self.digest_algorithm = config["digestAlgorithm"]\
                if "digestAlgorithm" in config else None
            self.honor_force_authn = config["honorForceAuthn"]\
                if "honorForceAuthn" in config else None
            self.idp_issuer = config["idpIssuer"]\
                if "idpIssuer" in config else None
            self.recipient = config["recipient"]\
                if "recipient" in config else None
            self.recipient_override = config["recipientOverride"]\
                if "recipientOverride" in config else None
            self.request_compressed = config["requestCompressed"]\
                if "requestCompressed" in config else None
            self.response_signed = config["responseSigned"]\
                if "responseSigned" in config else None
            self.signature_algorithm = config["signatureAlgorithm"]\
                if "signatureAlgorithm" in config else None
            self.sp_issuer = config["spIssuer"]\
                if "spIssuer" in config else None
            self.sso_acs_url = config["ssoAcsUrl"]\
                if "ssoAcsUrl" in config else None
            self.sso_acs_url_override = config["ssoAcsUrlOverride"]\
                if "ssoAcsUrlOverride" in config else None
            self.subject_name_id_format = config["subjectNameIdFormat"]\
                if "subjectNameIdFormat" in config else None
            self.subject_name_id_template = config["subjectNameIdTemplate"]\
                if "subjectNameIdTemplate" in config else None
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