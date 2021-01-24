from urllib import parse


class NoCorsApi:
    """
    Accesses a remote REST API endpoint that is normally not accessible through
    a browser because of unmatched CORS / same-origin policies.
    """

    def __init__(self, endpoint: str):
        if not endpoint:
            raise ValueError('Endpoint must be provided.')
        self.endpoint = parse.urlparse(endpoint)

    def get_endpoint(self):
        return self.endpoint
