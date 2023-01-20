# Classification of Penguins using a Quantum Support Vector Machine

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://bopardikarsoham-penguin-species-quantum-cl-streamlit-app-p7ofhi.streamlit.app/)

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

## Demo Input :computer:
<p align="center">
  <img src="https://user-images.githubusercontent.com/77266161/213678509-453b3504-d7eb-4224-a62d-94f82f559548.png" width="600" height="600" />
</p>

## Prediction :fire:
<p align="center">
  <img src="https://user-images.githubusercontent.com/77266161/213679265-db7b4221-0ef0-4b4a-9603-6a6e23aea4cd.png" width="600" height="600" />
</p>
