# Classification of Penguins using a Quantum Support Vector Machine

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://bopardikarsoham-penguin-species-quantum-cl-streamlit-app-p7ofhi.streamlit.app/) :arrow_left:	 It also works on mobile devices

In this project I have created a Quantum Machine Learning Model that can classify the species of Palmer Penguins on the basis of their features present in this [dataset](https://www.kaggle.com/datasets/ashkhagan/palmer-penguins-datasetalternative-iris-dataset).

## Here are the Palmer Penguins!

![Penguin_Species](https://user-images.githubusercontent.com/77266161/146253873-4dfbcc5c-eee2-4b60-b557-7df5abb6af2f.png)

## How to run the project locally 🚀
After cloning the repository to your local system, create a virtual environment, and activate it.

```
pip install virtualenv 
virtualenv env
```

On Windows, powershell

```
.\env\Scripts\activate.ps1
```

On Mac/Linux

```
source ./env/bin/activate
```

Then install the required packages using the specified requirements.txt file

```
pip install -r requirements.txt
```

To launch the server and run the project,

```
streamlit run streamlit_app.py
```

For running the backend with FastAPI

```
uvicorn fast_api:app --reload
```

## Demo Input from [penguins.csv](https://github.com/bopardikarsoham/Penguin_Species_Quantum_Classifer_App/blob/main/penguins.csv):computer:
<p align="center">
  <img src="https://user-images.githubusercontent.com/77266161/213694508-6eb2899a-ec82-48fa-ba94-6af74abc4578.png" width="600" height="600" />
</p>

## Prediction :fire:
<p align="center">
  <img src="https://user-images.githubusercontent.com/77266161/213695069-7bab3e3f-a86c-44f2-97c7-d1fcf6c4f07a.png" width="600" height="600" />
</p>
