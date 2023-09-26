from pycaret.regression import load_model
import pandas as pd
import sys
import os

data = {
    "Age": sys.argv[1],
    "Income": sys.argv[2],
    "Gender" : sys.argv[3],
}

sys.stdout = open(os.devnull, 'w')

df = pd.DataFrame([data])
model = load_model("AI/model")
pred = model.predict(df)

sys.stdout = sys.__stdout__

print(pred[0])