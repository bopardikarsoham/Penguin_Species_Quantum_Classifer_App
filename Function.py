import pickle
from Penguins import Penguin

pickle_in = open("penguin_classifier.pkl","rb")
classifier=pickle.load(pickle_in)
minmax_in = open("minmax.pkl","rb")
minmax_scale = pickle.load(minmax_in)
def predict_penguin(data:Penguin):
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