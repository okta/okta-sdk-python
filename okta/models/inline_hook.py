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
from okta.models import inline_hook_channel\
    as inline_hook_channel
from okta.models import inline_hook_status\
    as inline_hook_status
from okta.models import inline_hook_type\
    as inline_hook_type


class InlineHook(
    OktaObject
):
    """
    A class for InlineHook objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.links = config["links"]\
                if "links" in config else None
            if "channel" in config:
                if isinstance(config["channel"],
                              inline_hook_channel.InlineHookChannel):
                    self.channel = config["channel"]
                elif config["channel"] is not None:
                    self.channel = inline_hook_channel.InlineHookChannel(
                        config["channel"]
                    )
                else:
                    self.channel = None
            else:
                self.channel = None
            self.created = config["created"]\
                if "created" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
            self.name = config["name"]\
                if "name" in config else None
            if "status" in config:
                if isinstance(config["status"],
                              inline_hook_status.InlineHookStatus):
                    self.status = config["status"]
                elif config["status"] is not None:
                    self.status = inline_hook_status.InlineHookStatus(
                        config["status"].upper()
                    )
                else:
                    self.status = None
            else:
                self.status = None
            if "type" in config:
                if isinstance(config["type"],
                              inline_hook_type.InlineHookType):
                    self.type = config["type"]
                elif config["type"] is not None:
                    self.type = inline_hook_type.InlineHookType(
                        config["type"].upper()
                    )
                else:
                    self.type = None
            else:
                self.type = None
            self.version = config["version"]\
                if "version" in config else None
        else:
            self.links = None
            self.channel = None
            self.created = None
            self.id = None
            self.last_updated = None
            self.name = None
            self.status = None
            self.type = None
            self.version = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_links": self.links,
            "channel": self.channel,
            "created": self.created,
            "id": self.id,
            "lastUpdated": self.last_updated,
            "name": self.name,
            "status": self.status,
            "type": self.type,
            "version": self.version
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
