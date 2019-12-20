from okta.framework.ApiClient import ApiClient
from okta.framework.Utils import Utils
from okta.models.logs.Logs import Logs
from okta.framework.PagedResults import PagedResults


class LogsClient(ApiClient):
    def __init__(self, *args, **kwargs):
        kwargs['pathname'] = '/api/v1/logs'
        ApiClient.__init__(self, *args, **kwargs)

    def get_logs(self, limit=None, since=None, filter_string=None):
        """Get a list of Events

        :param limit: maximum number of events to return
        :type limit: int or None
        :param since: the lower time bound of the log events published property
        :type since: str
        :param filter_string: string to filter events
        :type filter_string: str or None
        :rtype: list of Event
        """
        params = {
            'limit': limit,
            'since': since,
            'filter': filter_string
        }
        response = ApiClient.get_path(self, '/', params=params)

        return Utils.deserialize(response.text, Logs)

    def get_paged_logs(self, limit=None, since=None, after=None, filter_string=None, url=None):
        """Get a paged list of Events

        :param limit: maximum number of events to return
        :type limit: int or None
        :param since: the lower time bound of the log events published property
        :type since: str
        :param filter_string: string to filter events
        :type filter_string: str or None
        :param after: event id that filtering will resume after
        :type after: str or None
        :param url: url that returns a list of Event
        :type url: str or None
        :rtype: PagedResults of Event
        """
        if url:
            response = ApiClient.get(self, url)

        else:
            params = {
                'limit': limit,
                'since': since,
                'after': after,
                'filter': filter_string
            }
            response = ApiClient.get_path(self, '/', params=params)

        return PagedResults(response, Logs)