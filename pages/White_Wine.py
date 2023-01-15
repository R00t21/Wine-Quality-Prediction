import pickle
import streamlit as st
import pandas as pd

filename = 'White Wine/model.sav'
model = pickle.load(open(filename, 'rb'))


@st.cache
def predict(fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide,	density, pH, sulphates,	alcohol):
    prediction = model.predict(pd.DataFrame([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]], columns=['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']))
    return prediction


st.title('White Wine')
st.image("images\white_wine.jpg")
st.header('Entre las característica del vino:')
fixed_acidity = st.number_input('Fixed acidity:', min_value=5.0, max_value=12.0, value=5.0)
volatile_acidity = st.number_input('Volatile acidity:', min_value=0.1, max_value=2.0, value=1.0)
citric_acid = st.number_input('Citric acid:', min_value=0.1, max_value=1.0, value=1.0)
residual_sugar = st.number_input('Residual sugar:', min_value=1.0, max_value=25.0, value=1.0)
chlorides = st.number_input('Chlorides:', min_value=0.001, max_value=1.0, value=1.0)
free_sulfur_dioxide = st.number_input('Free sulfur dioxide:', min_value=1.0, max_value=60.0, value=1.0)
total_sulfur_dioxide = st.number_input('Total sulfur dioxide:', min_value=1.0, max_value=300.0, value=1.0)
density = st.number_input('Density:', min_value=0.001, max_value=1.0, value=1.0)
pH = st.number_input('pH:', min_value=0.1, max_value=10.0, value=1.0)
sulphates = st.number_input('Sulphates:', min_value=0.1, max_value=1.0, value=1.0)
alcohol = st.number_input('Alcohol:', min_value=0.1, max_value=15.0, value=1.0)


if st.button('Predecir la calidad del vino blanco'):
    wine = predict(fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide,	density, pH, sulphates,	alcohol)
    if wine == 1:
        st.header('Good Quality White Wine')
        st.image("images\white_wine_predict.jpg")
    else:
        st.header('Bad Quality White Wine')
        st.image("images\Bad_quality_white_wine.jpg")
