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
from okta.models import log_geolocation\
    as log_geolocation


class LogGeographicalContext(
    OktaObject
):
    """
    A class for LogGeographicalContext objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.city = config["city"]\
                if "city" in config else None
            self.country = config["country"]\
                if "country" in config else None
            if "geolocation" in config:
                if isinstance(config["geolocation"],
                              log_geolocation.LogGeolocation):
                    self.geolocation = config["geolocation"]
                elif config["geolocation"] is not None:
                    self.geolocation = log_geolocation.LogGeolocation(
                        config["geolocation"]
                    )
                else:
                    self.geolocation = None
            else:
                self.geolocation = None
            self.postal_code = config["postalCode"]\
                if "postalCode" in config else None
            self.state = config["state"]\
                if "state" in config else None
        else:
            self.city = None
            self.country = None
            self.geolocation = None
            self.postal_code = None
            self.state = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "city": self.city,
            "country": self.country,
            "geolocation": self.geolocation,
            "postalCode": self.postal_code,
            "state": self.state
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
