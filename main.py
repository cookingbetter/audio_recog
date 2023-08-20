from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from pydub import AudioSegment
import os
import speech_recognition as sr
import time


app = FastAPI()


@app.post("/modify_audio")
async def modify_audio(file: UploadFile = File(...), speed: float = 1.01, volume: float = 1.0):
    with open(file.filename, "wb") as buffer:
        buffer.write(await file.read())
    audio = AudioSegment.from_wav(file.filename)
    modified_audio = audio.speedup(playback_speed=speed).apply_gain(volume)

    if os.path.isfile("modified_audio.wav"):
        os.remove("modified_audio.wav")

    modified_audio.export("modified_audio.wav", format="wav")

    if os.path.isfile("modified_audio.wav"):
        return {'msg': 'success'}
    else:
        return {'msg': 'error'}

# нужен отдельный get запрос для получения измененного аудиофайла,
# так как в post запросе же это сделать невозможно

@app.get("/get_modified_audio")
async def get_modified_audio():
    return FileResponse("modified_audio.wav")


@app.post("/predict")
async def predict(file: UploadFile = File(...), lang_int: int = 0):
    with open(file.filename, "wb") as buffer:
        buffer.write(await file.read())

    r = sr.Recognizer()
    with sr.AudioFile(file.filename) as source:
        audio_text = r.record(source)

    lang = 'ru-RU' if lang_int == 0 else 'en-US'

    start_time = time.time()

    prediction = r.recognize_google(audio_text, language=lang)

    #running_time =  (time.time() - start_time)

    #return prediction, round(running_time, 2)

    return {'prediction': prediction}