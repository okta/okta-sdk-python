# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS
# IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

import os

DEV_OKTA = "https://developer.okta.com"

FINDING_OKTA_DOMAIN = f"{DEV_OKTA}" "/docs/guides/find-your-domain/overview"
GET_OKTA_API_TOKEN = f"{DEV_OKTA}" "/docs/guides/create-an-api-token/overview"
FINDING_OKTA_APP_CRED = f"{DEV_OKTA}" "/docs/guides/find-your-app-credentials/overview"
REPO_URL = "https://github.com/okta/okta-sdk-python"

EPOCH_YEAR = 1970
EPOCH_MONTH = 1
EPOCH_DAY = 1

DATETIME_FORMAT = "%a, %d %b %Y %H:%M:%S %Z"

_GLOBAL_YAML_PATH = os.path.join(os.path.expanduser("~"), ".okta", "okta.yaml")
_LOCAL_YAML_PATH = os.path.join(os.getcwd(), "okta.yaml")

SWA_APP_NAME = "template_swa"
SWA3_APP_NAME = "template_swa3field"
