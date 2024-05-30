# flake8: noqa
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
from okta.models import sms_template_translations\
    as sms_template_translations
from okta.models import sms_template_type\
    as sms_template_type


class SmsTemplate(
    OktaObject
):
    """
    A class for SmsTemplate objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.created = config["created"]\
                if "created" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
            self.name = config["name"]\
                if "name" in config else None
            self.template = config["template"]\
                if "template" in config else None
            if "translations" in config:
                if isinstance(config["translations"],
                              sms_template_translations.SmsTemplateTranslations):
                    self.translations = config["translations"]
                elif config["translations"] is not None:
                    self.translations = sms_template_translations.SmsTemplateTranslations(
                        config["translations"]
                    )
                else:
                    self.translations = None
            else:
                self.translations = None
            if "type" in config:
                if isinstance(config["type"],
                              sms_template_type.SmsTemplateType):
                    self.type = config["type"]
                elif config["type"] is not None:
                    self.type = sms_template_type.SmsTemplateType(
                        config["type"].upper()
                    )
                else:
                    self.type = None
            else:
                self.type = None
        else:
            self.created = None
            self.id = None
            self.last_updated = None
            self.name = None
            self.template = None
            self.translations = None
            self.type = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "created": self.created,
            "id": self.id,
            "lastUpdated": self.last_updated,
            "name": self.name,
            "template": self.template,
            "translations": self.translations,
            "type": self.type
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
