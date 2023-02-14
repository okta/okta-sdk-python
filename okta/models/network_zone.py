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
from okta.models import network_zone_address\
    as network_zone_address
from okta.models import network_zone_location\
    as network_zone_location
from okta.models import network_zone_status\
    as network_zone_status
from okta.models import network_zone_type\
    as network_zone_type
from okta.models import network_zone_usage\
    as network_zone_usage


class NetworkZone(
    OktaObject
):
    """
    A class for NetworkZone objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.links = config["links"]\
                if "links" in config else None
            self.asns = OktaCollection.form_list(
                config["asns"] if "asns"\
                    in config else [],
                str
            )
            self.created = config["created"]\
                if "created" in config else None
            self.gateways = OktaCollection.form_list(
                config["gateways"] if "gateways"\
                    in config else [],
                network_zone_address.NetworkZoneAddress
            )
            self.id = config["id"]\
                if "id" in config else None
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
            self.locations = OktaCollection.form_list(
                config["locations"] if "locations"\
                    in config else [],
                network_zone_location.NetworkZoneLocation
            )
            self.name = config["name"]\
                if "name" in config else None
            self.proxies = OktaCollection.form_list(
                config["proxies"] if "proxies"\
                    in config else [],
                network_zone_address.NetworkZoneAddress
            )
            self.proxy_type = config["proxyType"]\
                if "proxyType" in config else None
            if "status" in config:
                if isinstance(config["status"],
                              network_zone_status.NetworkZoneStatus):
                    self.status = config["status"]
                elif config["status"] is not None:
                    self.status = network_zone_status.NetworkZoneStatus(
                        config["status"].upper()
                    )
                else:
                    self.status = None
            else:
                self.status = None
            self.system = config["system"]\
                if "system" in config else None
            if "type" in config:
                if isinstance(config["type"],
                              network_zone_type.NetworkZoneType):
                    self.type = config["type"]
                elif config["type"] is not None:
                    self.type = network_zone_type.NetworkZoneType(
                        config["type"].upper()
                    )
                else:
                    self.type = None
            else:
                self.type = None
            if "usage" in config:
                if isinstance(config["usage"],
                              network_zone_usage.NetworkZoneUsage):
                    self.usage = config["usage"]
                elif config["usage"] is not None:
                    self.usage = network_zone_usage.NetworkZoneUsage(
                        config["usage"].upper()
                    )
                else:
                    self.usage = None
            else:
                self.usage = None
        else:
            self.links = None
            self.asns = []
            self.created = None
            self.gateways = []
            self.id = None
            self.last_updated = None
            self.locations = []
            self.name = None
            self.proxies = []
            self.proxy_type = None
            self.status = None
            self.system = None
            self.type = None
            self.usage = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_links": self.links,
            "asns": self.asns,
            "created": self.created,
            "gateways": self.gateways,
            "id": self.id,
            "lastUpdated": self.last_updated,
            "locations": self.locations,
            "name": self.name,
            "proxies": self.proxies,
            "proxyType": self.proxy_type,
            "status": self.status,
            "system": self.system,
            "type": self.type,
            "usage": self.usage
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
