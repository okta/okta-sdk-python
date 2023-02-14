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
from okta.models import event_hook_channel\
    as event_hook_channel
from okta.models import event_subscriptions\
    as event_subscriptions


class EventHook(
    OktaObject
):
    """
    A class for EventHook objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.links = config["links"]\
                if "links" in config else None
            if "channel" in config:
                if isinstance(config["channel"],
                              event_hook_channel.EventHookChannel):
                    self.channel = config["channel"]
                elif config["channel"] is not None:
                    self.channel = event_hook_channel.EventHookChannel(
                        config["channel"]
                    )
                else:
                    self.channel = None
            else:
                self.channel = None
            self.created = config["created"]\
                if "created" in config else None
            self.created_by = config["createdBy"]\
                if "createdBy" in config else None
            if "events" in config:
                if isinstance(config["events"],
                              event_subscriptions.EventSubscriptions):
                    self.events = config["events"]
                elif config["events"] is not None:
                    self.events = event_subscriptions.EventSubscriptions(
                        config["events"]
                    )
                else:
                    self.events = None
            else:
                self.events = None
            self.id = config["id"]\
                if "id" in config else None
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
            self.name = config["name"]\
                if "name" in config else None
            self.status = config["status"]\
                if "status" in config else None
            self.verification_status = config["verificationStatus"]\
                if "verificationStatus" in config else None
        else:
            self.links = None
            self.channel = None
            self.created = None
            self.created_by = None
            self.events = None
            self.id = None
            self.last_updated = None
            self.name = None
            self.status = None
            self.verification_status = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_links": self.links,
            "channel": self.channel,
            "created": self.created,
            "createdBy": self.created_by,
            "events": self.events,
            "id": self.id,
            "lastUpdated": self.last_updated,
            "name": self.name,
            "status": self.status,
            "verificationStatus": self.verification_status
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
