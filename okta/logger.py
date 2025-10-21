# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

import logging

LOG_FORMAT = \
    '%(asctime)s - %(name)s - %(module)s - %(levelname)s - %(message)s'


def setup_logging(log_level=logging.INFO):
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(log_level)
    log_formatter = logging.Formatter(LOG_FORMAT)
    stream_handler.setFormatter(log_formatter)

    logger = logging.getLogger('okta-sdk-python')
    logger.addHandler(stream_handler)
    logger.setLevel(log_level)

    # disable logger by default
    logger.disabled = True
