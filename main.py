from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi import FastAPI
from datetime import date
from utils import hum, rain, temp, pred

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app = FastAPI()


class Inputs(BaseModel):
    nitrogen: float
    phosphorous: float
    potassium: float
    ph: float
    state: str
    district: str
    month: date


@app.post("/predict")
async def predict(inputs: Inputs):
    nitrogen = inputs.nitrogen
    phosphorous = inputs.phosphorous
    potassium = inputs.potassium
    state = inputs.state
    district = inputs.district
    month = inputs.month
    ph = inputs.ph

    rainfall = rain.get_rainfall(state, district, month)
    temperature = temp.get_temperature(state, district, month)
    humidity = hum.get_humidity(state, district, month)

    prediction = pred.get_prediction(
        nitrogen, phosphorous, potassium, ph, temperature, humidity, rainfall)

    return {"result": prediction}
