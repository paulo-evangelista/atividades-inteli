from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from pycaret.regression import load_model, predict_model
import pandas as pd
import os



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["POST"],
    allow_headers=["*"],
)



@app.post("/predict/")
async def get_prediction(item: dict):
    # types_validation(item)
    try:
        if os.path.exists("/app/modelo.pkl"):
            print("File exists.")
        else:
            print("File does not exist.")

        df = pd.DataFrame([item])
        df['Income'] = df['Income'].round(2)
        model = load_model("/app/modelo")
        pred = model.predict_model(df)
        return pred
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

