from fastapi import FastAPI
import pandas as pd

app = FastAPI()
df = pd.read_csv('./data/services2019.csv')

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/preview")
def preview():
    top10rows = df.head(1)
    result= top10rows.to_json(orient="records")
    return result  

@app.get("/services/{value}")  
def services(value: str):
    filtered = df[df['svc_code'] == value]
    if len(filtered) <= 0:
        return 'There is nothing here'
    else:
        return filtered.to_json(orient="records")

@app.get("/services/{value}/sex/{value2}")
def services2(value: str, value2: str):
    filtered = df[df['svc_code'] == value]
    filtered2 = filtered[filtered['sex'] == value2]
    if len(filtered2) <= 0:
        return 'There is nothing here'
    else:
        return filtered2.to_json(orient="records")  

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)