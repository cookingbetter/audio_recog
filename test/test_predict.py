from main import app
from fastapi.testclient import TestClient
import pytest


client = TestClient(app)


@pytest.mark.run(order=5)
def test_predict():
    with open("english_speech.wav", "rb") as file:
        response = client.post("/predict?lang_int=1", files={"file": file})
    assert response.status_code == 200
    assert response.json() == {
  "prediction": "Algeria will rise again and dragon eaten is the key Algeria will rise again and dragon eat them is the key Algeria will rise again and dragon eat some is the key Algeria will rise again and dragon eat some is the key Algeria will rise again and dragon eat them is the key will Jerry will rise again and dragon eat some is the key"
}


@pytest.mark.run(order=6)
def test_predict_one_more():
    with open("russian_speech.wav", "rb") as file:
        response = client.post("/predict?lang_int=0", files={"file": file})
    assert response.status_code == 200
    assert response.json() == {
  "prediction": "Саша Маша Даша Катя Света и Наташа Лена Женя Вова Даня Вася Галя Валя Таня Вика Миша Толя Оля Ксюша Ксюша слова Коля Дима Тёма Юля Лёша они Настя и Серёжа Витя Лёня fiestas Ваня тоже Петя эти имена у нас носят Каждый третий"
}