# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:40:41 2020
@author: win10
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI
from Penguins import Penguin
import pickle
# 2. Create the app object
app = FastAPI()
pickle_in = open("penguin_classifier.pkl","rb")
classifier=pickle.load(pickle_in)

minmax_in = open("minmax.pkl","rb")
minmax_scale = pickle.load(minmax_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Navigate to http://127.0.0.1:8000/docs for model'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_penguin(data:Penguin):
    data = data.dict()
    island=data['island']
    if island == "Biscoe":
        island = 0
    elif island == "Torgersen":
        island = 1
    elif island == "Dream":
        island = 2
    else:
        print("Write correct island name")
    bill_length_mm=data['bill_length_mm']
    bill_depth_mm=data['bill_depth_mm']
    flipper_length_mm=data['flipper_length_mm']
    body_mass_g=data['body_mass_g']
    sex=data['sex']
    if sex == "Female":
        sex = 0
    elif sex == "Male":
        sex = 1
    else:
        print("Write correct gender")
    prediction = classifier.predict(minmax_scale.transform([[island,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g,sex]])).tolist()[0]
    if(prediction == 0):
        prediction="Adelie"
    elif(prediction == 1):
        prediction="Chinstrap"
    elif(prediction == 2):
        prediction="Gentoo"
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload
