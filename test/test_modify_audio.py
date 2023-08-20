from main import app
from fastapi.testclient import TestClient
import pytest


client = TestClient(app)


@pytest.mark.run(order=1)
def test_modify_audio_one_more():
    with open("english_speech.wav", "rb") as file:
        response = client.post("/modify_audio?speed=1.1&volume=1", files={"file": file})

    assert response.status_code == 200
    assert response.json() == {"msg": "success"}


@pytest.mark.run(order=3)
def test_modify_audio_one_more():
    with open("russian_speech.wav", "rb") as file:
        response = client.post("/modify_audio?speed=1.1&volume=1", files={"file": file})

    assert response.status_code == 200
    assert response.json() == {"msg": "success"}