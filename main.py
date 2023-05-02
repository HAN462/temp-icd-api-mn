from flask import Flask
import pandas as pd 

df = pd.read_csv('./data/diagnoses2019.csv')

app = Flask(_name_)

@app.route('/',methods='get')
def home():
    return 'this is a API service for MN ICD code details'

@app.route('/preview', methods=["GET"])
def preview(): 
    top10rows = df.head(10)
    result = top10rows.to_json(orient="record")
    return result

@app.route('/icd', methods =['GET'])
def preview():
    filter_value = request.args.get(icdcode)
    filtered = df[df['principal_diagnosis_code'] == filter_value]
    return filtered.to_json(orient="records")

if _name_== '_main_':
    app.run(debug=True)