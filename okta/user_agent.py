from okta import __version__ as VERSION

import platform


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
