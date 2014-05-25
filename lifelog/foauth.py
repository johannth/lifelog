import os

import requests

FOAUTH_BASE_URL = 'https://foauth.org'


def foauth(endpoint, base_api_url, method, auth=None, *args, **kwargs):
    url = os.path.join(FOAUTH_BASE_URL, base_api_url, endpoint)

    if auth is None:
        auth = os.environ['FOUTH_USERNAME'], os.environ["FOUTH_PASSWORD"]

    return requests.request(
        url=url,
        method=method,
        auth=auth,
        *args,
        **kwargs
    )
