from pycaret.regression import load_model, predict_model
import pandas as pd
from fastapi import  HTTPException
import os

def types_validation(data: dict):
    if not isinstance(data["Age"], int):
        raise HTTPException(status_code=400, detail="age must be int")
    if not isinstance(data["Gender"], int) or (data["Gender"] != 0 and data["Gender"] != 1):
        raise HTTPException(status_code=400, detail="Gender must be 1 or 0")
    if not isinstance(data["Income"], float):
        raise HTTPException(status_code=400, detail="Income must be float")

def predict(data: dict):
    types_validation(data)
    try:


        if os.path.exists("/app/modelo.pkl"):
            print("File exists.")
        else:
            print("File does not exist.")

        df = pd.DataFrame([data])
        df['Income'] = df['Income'].round(2)
        model = load_model("/app/modelo")
        pred = model.predict_model(df)
        return pred
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)