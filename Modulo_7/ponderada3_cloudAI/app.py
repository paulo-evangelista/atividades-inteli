from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pycaret.regression import load_model
import pandas as pd
from pydantic import BaseModel 

# classe para Pydantic (tipagem da requisição)
class body(BaseModel):
    Age: int
    Income: float
    Gender: int
 
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["POST"],
    allow_headers=["*"],
)

@app.post("/predict/")
async def get_prediction(item: body):
    try:
        df = pd.DataFrame([item.dict()])
        model = load_model("/app/model")
        pred = model.predict(df)
        return {"predictions": pred.tolist()[0]}
    except Exception as e:
        return HTTPException(e)