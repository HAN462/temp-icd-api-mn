from fastapi import FastAPI
import pandas as pd

app = FastAPI()
df = pd.read_csv('./data/services2019.csv')