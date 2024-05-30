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

from aenum import MultiValueEnum


class FactorResultType(
    str,
    MultiValueEnum
):
    """
    An enumeration class for FactorResultType.
    """

    SUCCESS = "SUCCESS", "success"
    CHALLENGE = "CHALLENGE", "challenge"
    WAITING = "WAITING", "waiting"
    FAILED = "FAILED", "failed"
    REJECTED = "REJECTED", "rejected"
    TIMEOUT = "TIMEOUT", "timeout"
    TIME_WINDOW_EXCEEDED = "TIME_WINDOW_EXCEEDED", "time_window_exceeded"
    PASSCODE_REPLAYED = "PASSCODE_REPLAYED", "passcode_replayed"
    ERROR = "ERROR", "error"
    CANCELLED = "CANCELLED", "cancelled"
