# Classification of Penguins using a Quantum Support Vector Machine
In this project I have created a Quantum Machine Learning Model that can classify the species of Palmer Penguins on the basis of their features present in this dataset(https://www.kaggle.com/ashkhagan/palmer-penguins-datasetalternative-iris-dataset?select=penguins.csv).

## Palmer Penguins Dataset
The goal of palmerpenguins is to provide a great dataset for data exploration & visualization. It is sometimes considered an alternative to the Iris Dataset.

## Here are the Palmer Penguins!

![Penguin_Species](https://user-images.githubusercontent.com/77266161/146253873-4dfbcc5c-eee2-4b60-b557-7df5abb6af2f.png)

## How to run the project 🚀
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

For running backend with FastAPI

```
uvicorn fast_api:app --reload
```

## Output 
