from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Carregando o modelo

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["POST"],
    allow_headers=["*"],
)



@app.post("/predict/")
async def get_prediction(query):
    print(query)

# Para rodar a aplicação, no terminal: uvicorn main:app --reload
