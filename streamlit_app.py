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
adelie_html="""  
      <div style="background-color:#FF8C00;padding:10px >
       <h2 style="color:white;text-align:center;"> Adelie</h2>
       </div>
    """
chinstrap_html="""  
      <div style="background-color:#BA55D3;padding:10px >
       <h2 style="color:black ;text-align:center;"> Chinstrap</h2>
       </div>
    """
gentoo_html="""  
      <div style="background-color:#48D1CC;padding:10px >
       <h2 style="color:black ;text-align:center;"> Gentoo</h2>
       </div>
    """
if st.button("Predict"):
        prediction=predict_penguin({'island': island,'bill_length_mm': float(bill_length_mm),'bill_depth_mm': float(bill_depth_mm),'flipper_length_mm': float(flipper_length_mm),'body_mass_g': float(body_mass_g),'sex': sex})
        for value in prediction.values():
            st.success('Penguin Species is {}'.format(value))

        if value=="Adelie":
            st.markdown(adelie_html,unsafe_allow_html=True)
            adelie_img = Image.open('Images/Adelie.jpg')
            st.image(adelie_img)
        elif value=="Chinstrap":
            st.markdown(chinstrap_html,unsafe_allow_html=True)
            chinstrap_img = Image.open('Images/Chinstrap.jpg')
            st.image(chinstrap_img)
        elif value=="Gentoo":
            st.markdown(gentoo_html,unsafe_allow_html=True)
            gentoo_img = Image.open('Images/Gentoo.jpg')
            st.image(gentoo_img)
        