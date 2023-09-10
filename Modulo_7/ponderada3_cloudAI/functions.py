from pycaret.regression import load_model, predict_model
import pandas as pd
from fastapi import  HTTPException

# def data_validation(data: dict):



def predict(data: dict):
    df = pd.DataFrame([data])
