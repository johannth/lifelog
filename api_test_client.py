
import json

from flask.testing import FlaskClient


class APITestClient(FlaskClient):

    def _default_headers(self):
        headers = {}

        headers.update({
            'Accept': 'application/json',
        })
        return headers

    def _make_http_headers(self, headers=None):
        request_headers = self._default_headers()
        if headers:
            request_headers.update(headers)

        return request_headers

    def get_json(self, url, query_string=None, headers=None):
        response = self.get(
            url,
            query_string=query_string or {},
            content_type="application/json",
            headers=self._make_http_headers(headers))

        self._add_json_to_response(response)

        return response

    def post_json(self, url, data=None, headers=None):
        response = self.post(
            url,
            data=json.dumps(data or {}),
            content_type="application/json",
            headers=self._make_http_headers(headers),
        )

        self._add_json_to_response(response)

        return response

    def delete_json(self, url, data=None, headers=None):
        response = self.delete(
            url,
            data=json.dumps(data or {}),
            content_type="application/json",
            headers=self._make_http_headers(headers)
        )

        self._add_json_to_response(response)

        return response

    def put_json(self, url, data=None, headers=None):
        response = self.put(
            url,
            data=json.dumps(data or {}),
            content_type="application/json",
            headers=self._make_http_headers(headers)
        )

        self._add_json_to_response(response)

        return response

    def patch_json(self, url, data=None, headers=None):
        response = self.patch(
            url,
            data=json.dumps(data or {}),
            content_type="application/json",
            headers=self._make_http_headers(headers)
        )

        self._add_json_to_response(response)

        return response

    def _add_json_to_response(self, response):
        if response.headers['Content-Type'] == "application/json":
            response.json = json.loads(response.data)
        else:
            response.json = None
