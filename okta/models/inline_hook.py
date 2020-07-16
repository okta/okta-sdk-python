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
from okta.models.inline_hook_channel\
    import InlineHookChannel
from okta.models.inline_hook_status\
    import InlineHookStatus
from okta.models.inline_hook_type\
    import InlineHookType


class InlineHook(
    OktaObject
):
    """
    A class for InlineHook objects.
    """

    def __init__(self, config=None):
        if config:
            self.links = config["_links"]\
                if "_links" in config else None
            if "channel" in config:
                if isinstance(config["channel"],
                              InlineHookChannel):
                    self.channel = config["channel"]
                else:
                    self.channel = InlineHookChannel(
                        config["channel"]
                    )
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
                              InlineHookStatus):
                    self.status = config["status"]
                else:
                    self.status = InlineHookStatus(
                        config["status"]
                    )
            else:
                self.status = None
            if "type" in config:
                if isinstance(config["type"],
                              InlineHookType):
                    self.type = config["type"]
                else:
                    self.type = InlineHookType(
                        config["type"]
                    )
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
