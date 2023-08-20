from main import app
from fastapi.testclient import TestClient
import pytest


client = TestClient(app)


@pytest.mark.run(order=2)
def test_get_modified_audio():
    response = client.get("/get_modified_audio")
    assert response.status_code == 200
    assert response.headers["content-type"] == "audio/wav"


@pytest.mark.run(order=4)
def test_get_modified_audio_one_more():
    response = client.get("/get_modified_audio")
    assert response.status_code == 200
    assert response.headers["content-type"] == "audio/wav"