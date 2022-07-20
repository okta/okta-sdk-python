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
from okta.models import email_template_touch_point_variant\
    as email_template_touch_point_variant
from okta.models import end_user_dashboard_touch_point_variant\
    as end_user_dashboard_touch_point_variant
from okta.models import error_page_touch_point_variant\
    as error_page_touch_point_variant
from okta.models import sign_in_page_touch_point_variant\
    as sign_in_page_touch_point_variant


class ThemeResponse(
    OktaObject
):
    """
    A class for ThemeResponse objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.links = config["links"]\
                if "links" in config else None
            self.background_image = config["backgroundImage"]\
                if "backgroundImage" in config else None
            if "emailTemplateTouchPointVariant" in config:
                if isinstance(config["emailTemplateTouchPointVariant"],
                              email_template_touch_point_variant.EmailTemplateTouchPointVariant):
                    self.email_template_touch_point_variant = config["emailTemplateTouchPointVariant"]
                elif config["emailTemplateTouchPointVariant"] is not None:
                    self.email_template_touch_point_variant = email_template_touch_point_variant.EmailTemplateTouchPointVariant(
                        config["emailTemplateTouchPointVariant"].upper()
                    )
                else:
                    self.email_template_touch_point_variant = None
            else:
                self.email_template_touch_point_variant = None
            if "endUserDashboardTouchPointVariant" in config:
                if isinstance(config["endUserDashboardTouchPointVariant"],
                              end_user_dashboard_touch_point_variant.EndUserDashboardTouchPointVariant):
                    self.end_user_dashboard_touch_point_variant = config["endUserDashboardTouchPointVariant"]
                elif config["endUserDashboardTouchPointVariant"] is not None:
                    self.end_user_dashboard_touch_point_variant = end_user_dashboard_touch_point_variant.EndUserDashboardTouchPointVariant(
                        config["endUserDashboardTouchPointVariant"].upper()
                    )
                else:
                    self.end_user_dashboard_touch_point_variant = None
            else:
                self.end_user_dashboard_touch_point_variant = None
            if "errorPageTouchPointVariant" in config:
                if isinstance(config["errorPageTouchPointVariant"],
                              error_page_touch_point_variant.ErrorPageTouchPointVariant):
                    self.error_page_touch_point_variant = config["errorPageTouchPointVariant"]
                elif config["errorPageTouchPointVariant"] is not None:
                    self.error_page_touch_point_variant = error_page_touch_point_variant.ErrorPageTouchPointVariant(
                        config["errorPageTouchPointVariant"].upper()
                    )
                else:
                    self.error_page_touch_point_variant = None
            else:
                self.error_page_touch_point_variant = None
            self.favicon = config["favicon"]\
                if "favicon" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.logo = config["logo"]\
                if "logo" in config else None
            self.primary_color_contrast_hex = config["primaryColorContrastHex"]\
                if "primaryColorContrastHex" in config else None
            self.primary_color_hex = config["primaryColorHex"]\
                if "primaryColorHex" in config else None
            self.secondary_color_contrast_hex = config["secondaryColorContrastHex"]\
                if "secondaryColorContrastHex" in config else None
            self.secondary_color_hex = config["secondaryColorHex"]\
                if "secondaryColorHex" in config else None
            if "signInPageTouchPointVariant" in config:
                if isinstance(config["signInPageTouchPointVariant"],
                              sign_in_page_touch_point_variant.SignInPageTouchPointVariant):
                    self.sign_in_page_touch_point_variant = config["signInPageTouchPointVariant"]
                elif config["signInPageTouchPointVariant"] is not None:
                    self.sign_in_page_touch_point_variant = sign_in_page_touch_point_variant.SignInPageTouchPointVariant(
                        config["signInPageTouchPointVariant"].upper()
                    )
                else:
                    self.sign_in_page_touch_point_variant = None
            else:
                self.sign_in_page_touch_point_variant = None
        else:
            self.links = None
            self.background_image = None
            self.email_template_touch_point_variant = None
            self.end_user_dashboard_touch_point_variant = None
            self.error_page_touch_point_variant = None
            self.favicon = None
            self.id = None
            self.logo = None
            self.primary_color_contrast_hex = None
            self.primary_color_hex = None
            self.secondary_color_contrast_hex = None
            self.secondary_color_hex = None
            self.sign_in_page_touch_point_variant = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_links": self.links,
            "backgroundImage": self.background_image,
            "emailTemplateTouchPointVariant": self.email_template_touch_point_variant,
            "endUserDashboardTouchPointVariant": self.end_user_dashboard_touch_point_variant,
            "errorPageTouchPointVariant": self.error_page_touch_point_variant,
            "favicon": self.favicon,
            "id": self.id,
            "logo": self.logo,
            "primaryColorContrastHex": self.primary_color_contrast_hex,
            "primaryColorHex": self.primary_color_hex,
            "secondaryColorContrastHex": self.secondary_color_contrast_hex,
            "secondaryColorHex": self.secondary_color_hex,
            "signInPageTouchPointVariant": self.sign_in_page_touch_point_variant
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
