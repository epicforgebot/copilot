import os
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture(scope='module')
def set_env_vars():
    os.environ['SAP_AI_CORE_URL'] = 'https://fake-ai-core-url'
    os.environ['XSUAA_URL'] = 'https://fake-xsuaa-url'
    os.environ['CLIENT_ID'] = 'fake-client-id'
    os.environ['CLIENT_SECRET'] = 'fake-client-secret'


def test_read_root(set_env_vars):
    """
    Test case for the root endpoint.
    """
    response = client.get('/')
    assert response.status_code == 200
    assert response.() == {'Hello': 'World'}


def test_predict_success(set_env_vars, requests_mock):
    """
    Test case for successful prediction.
    """
    requests_mock.post('https://fake-ai-core-url/predict', ={'prediction': 'success'})
    response = client.post('/ai/predict', ={'input': 'data'})
    assert response.status_code == 200
    assert response.() == {'prediction': 'success'}


def test_predict_failure(set_env_vars, requests_mock):
    """
    Test case for failed prediction.
    """
    requests_mock.post('https://fake-ai-core-url/predict', status_code=400, text='Bad Request')
    response = client.post('/ai/predict', ={'input': 'data'})
    assert response.status_code == 400
    assert response.() == {'detail': 'Bad Request'}
