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
from okta.okta_collection import OktaCollection
from okta.models import notification_type\
    as notification_type
from okta.models import subscription_status\
    as subscription_status


class Subscription(
    OktaObject
):
    """
    A class for Subscription objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.links = config["links"]\
                if "links" in config else None
            if "_links" in config:
                self.links = config["_links"]
            self.channels = OktaCollection.form_list(
                config["channels"] if "channels"\
                    in config else [],
                str
            )
            if "notificationType" in config:
                if isinstance(config["notificationType"],
                              notification_type.NotificationType):
                    self.notification_type = config["notificationType"]
                elif config["notificationType"] is not None:
                    self.notification_type = notification_type.NotificationType(
                        config["notificationType"].upper()
                    )
                else:
                    self.notification_type = None
            else:
                self.notification_type = None
            if "status" in config:
                if isinstance(config["status"],
                              subscription_status.SubscriptionStatus):
                    self.status = config["status"]
                elif config["status"] is not None:
                    self.status = subscription_status.SubscriptionStatus(
                        config["status"].upper()
                    )
                else:
                    self.status = None
            else:
                self.status = None
        else:
            self.links = None
            self.channels = []
            self.notification_type = None
            self.status = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_links": self.links,
            "channels": self.channels,
            "notificationType": self.notification_type,
            "status": self.status
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
