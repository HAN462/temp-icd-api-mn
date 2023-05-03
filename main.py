from fastapi import FastAPI
import pandas as pd

app = FastAPI()
df = pd.read_csv("services2019.csv")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.route('/', methods=["GET"])
def home():
    return 'this is a API service for MN services details'

@app.route('/preview', methods=["GET"])
def preview():
    top10rows = df.head(1)
    result = top10rows.to_json(orient="records")
    return result