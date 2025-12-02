from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import joblib
import numpy as np
import os

# Define a Pydantic model for input validation
class Features(BaseModel):
    features: list[float]

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained model
model = joblib.load("model.pkl")

# Serve HTML frontend
@app.get("/", response_class=HTMLResponse)
def home():
    html_file = os.path.join(os.path.dirname(__file__), "index.html")
    with open(html_file, "r", encoding="utf-8") as f:
        return f.read()

# Prediction endpoint
@app.post("/predict")
def predict(input: Features):
    try:
        data = np.array(input.features).reshape(1, -1)
        prediction = model.predict(data)
        return {"prediction": float(prediction[0])}
    except Exception as e:
        return {"error": str(e)}



