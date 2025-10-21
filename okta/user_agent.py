# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

import platform

from okta import __version__ as VERSION


class UserAgent():
    SDK_NAME = "okta-sdk-python"
    PYTHON = "python"

    def __init__(self, user_agent_extra=None):
        python_version = platform.python_version()
        os_name = platform.system()
        os_version = platform.release()
        self._user_agent_string = (f"{UserAgent.SDK_NAME}/{VERSION} "
                                   f"{UserAgent.PYTHON}/{python_version} "
                                   f"{os_name}/{os_version}")
        if (user_agent_extra):
            self._user_agent_string += f" {user_agent_extra}"

    def get_user_agent_string(self):
        return self._user_agent_string
