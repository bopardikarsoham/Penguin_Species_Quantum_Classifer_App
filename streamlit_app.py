import streamlit as st
from Function import predict_penguin #Calling the predict_penguin function from Function.py
from PIL import Image
st.title("Penguin Species Quantum Classifer :penguin:")

island  = st.text_input("Island")
bill_length_mm  = st.text_input("Bill Length(mm)")
bill_depth_mm  = st.text_input("Bill Depth(mm)")
flipper_length_mm  = st.text_input("Flipper Length(mm)")
body_mass_g = st.text_input("Body Mass(g)")
sex = st.text_input("Sex")
if st.button("Predict"):
        prediction=predict_penguin({'island': island,'bill_length_mm': float(bill_length_mm),'bill_depth_mm': float(bill_depth_mm),'flipper_length_mm': float(flipper_length_mm),'body_mass_g': float(body_mass_g),'sex': sex})
        for value in prediction.values():
            st.success('Penguin Species is {}'.format(value))

        if value=="Adelie":
            im = Image.open("Images/Adelie.jpg")
            new_im = im.resize((600,600))
            st.image(new_im)
        elif value=="Chinstrap":
            im = Image.open("Images/Chinstrap.jpg")
            new_im = im.resize((600,600))
            st.image(new_im)
        elif value=="Gentoo":
            im = Image.open("Images/Gentoo.jpg")
            new_im = im.resize((600,600)) 
            st.image(new_im)       
