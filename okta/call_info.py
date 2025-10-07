# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

class CallInfo:
    method: None
    url: None
    headers: None
    body: None
    post_params: None
    response_data: None

    def __init__(self, call_info_dict) -> None:
        self.method = call_info_dict['method']
        self.url = call_info_dict['url']
        self.headers = call_info_dict['headers']
        self.body = call_info_dict['body']
        self.post_params = call_info_dict['post_params']
        if ('response_data' in call_info_dict):
            self.response_data = call_info_dict['response_data']
