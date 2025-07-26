
import requests

class ReliefWebClient:
    """
    Python client for the ReliefWeb API.
    See: https://apidoc.reliefweb.int/
    """
    BASE_URL = 'https://api.reliefweb.int/v1/'

    def __init__(self, api_key=None, appname="reliefweb-python-client"):
        """
        Initialize the ReliefWebClient.
        Args:
            api_key (str, optional): API key for authentication (if required).
            appname (str, optional): App name to send as required by ReliefWeb API.
        """
        self.api_key = api_key
        self.appname = appname
        self.session = requests.Session()
        if api_key:
            self.session.headers.update({'Authorization': f'Bearer {api_key}'})

    def _request(self, endpoint, payload=None):
        """
        Internal method to send a POST request to ReliefWeb API.
        Args:
            endpoint (str): API endpoint (e.g., 'reports').
            payload (dict, optional): Request payload.
        Returns:
            dict: Parsed JSON response.
        """
        url = self.BASE_URL + endpoint
        # Ensure appname is always included as a query parameter
        params = {"appname": self.appname}
        response = self.session.post(url, params=params, json=payload or {})
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            raise RuntimeError(f'ReliefWeb API error: {e}\n{response.text}')
        return response.json()

    def get_reports(self, filters=None, fields=None, sort=None, limit=10, offset=0, presets=None):
        """
        Fetch reports from ReliefWeb API.
        Args:
            filters (dict, optional): Filtering parameters.
            fields (list, optional): Fields to include in results.
            sort (list, optional): Sorting options.
            limit (int, optional): Number of results to return.
            offset (int, optional): Offset for pagination.
            presets (list, optional): Presets to apply.
        Returns:
            dict: API response.
        Example:
            client.get_reports(filters={"country": {"eq": "ETH"}}, fields=["id", "date", "title"], limit=5)
        """
        payload = self._build_payload(filters, fields, sort, limit, offset, presets)
        return self._request('reports', payload)

    def get_jobs(self, filters=None, fields=None, sort=None, limit=10, offset=0, presets=None):
        """
        Fetch jobs from ReliefWeb API.
        Args and returns same as get_reports.
        """
        payload = self._build_payload(filters, fields, sort, limit, offset, presets)
        return self._request('jobs', payload)

    def get_training(self, filters=None, fields=None, sort=None, limit=10, offset=0, presets=None):
        """
        Fetch training from ReliefWeb API.
        Args and returns same as get_reports.
        """
        payload = self._build_payload(filters, fields, sort, limit, offset, presets)
        return self._request('training', payload)

    def _build_payload(self, filters, fields, sort, limit, offset, presets):
        """
        Build the request payload for ReliefWeb API.
        """
        payload = {
            "filter": {},
            "fields": {"include": fields or []},
            "sort": sort or [],
            "limit": limit,
            "offset": offset
        }
        if filters:
            payload["filter"].update(filters)
        if presets:
            payload["presets"] = presets
        return payload
