# flake8: noqa
"""
Copyright 2021 - Present Okta, Inc.

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


class SignInPageTouchPointVariant(
    str,
    MultiValueEnum
):
    """
    An enumeration class for SignInPageTouchPointVariant.
    """

    OKTA_DEFAULT = "OKTA_DEFAULT", "okta_default"
    BACKGROUND_SECONDARY_COLOR = "BACKGROUND_SECONDARY_COLOR", "background_secondary_color"
    BACKGROUND_IMAGE = "BACKGROUND_IMAGE", "background_image"
