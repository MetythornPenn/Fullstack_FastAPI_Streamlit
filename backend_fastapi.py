import joblib
import uvicorn
import numpy as np
import pandas as pd
from pydantic import BaseModel
from fastapi import FastAPI

# Initialize the app
app = FastAPI(title= 'Placement API', version='1.0', description='API for Placement Prediction')

# Initaialize model artifacts files
model = joblib.load('traned_model.joblib')

class Data(BaseModel):
    year: float


# AP root and home endpoint
@app.get('/')
@app.get('/home')
async def root():
    return {'message': 'Full Stack ML App using FastAPI and Streamlit'}

# API endpoint for prediction
@app.post('/predict/')
async def predict(data: Data):
    data_dict = data.dict()
    data_df = pd.DataFrame.from_dict([data_dict])
    #year = data_dict['year']
    #prediction = model.predict(data_df)
    prediction = data_df * 2 + 1

    return prediction

if __name__ == "__main__":
    uvicorn.run("backend_fastapi:app", host="localhost", port=8000, reload=True)





