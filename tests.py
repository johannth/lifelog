import pytest

from api_test_client import APITestClient

from lifelog.app import create_app


@pytest.fixture
def app():
    return create_app(debug=True)


@pytest.fixture
def api_client(app):
    client = APITestClient(app, app.response_class)
    return client


def test_index(api_client):
    response = api_client.get_json("/")
    assert response.status_code == 200
    assert response.json == {}