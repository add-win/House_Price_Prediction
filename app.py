import streamlit as st
import joblib
import pandas as pd

model = joblib.load("log_reg_house_model.pkl")

st.title("House Price Prediction")

area = st.number_input(
    "Enter the Square Feet",
    min_value=600.0,
    max_value=3000.0,
    value=600.0
)
if area<600 or area>3000:
  st.error("Area should be in between 600 and 3000")

bedroom = st.number_input(
    "Enter the Number of Bedrooms",
    min_value=1.0,
    max_value=4.0,
    value=1.0
)
if bedroom<1 or bedroom>4:
  st.error("Number of Bedrooms should be in between 1 and 4")
  
floor = st.number_input(
    "Enter the Number of Floors",
    min_value=0.0,
    max_value=10.0,
    value=0.0
)
if floor<0 or floor>10:
  st.error("Number of Floors should be in between 0 and 10")
  
if st.button("Predict"):

    input_data = pd.DataFrame({
        "Area": [area],
        "Bedrooms": [bedroom],
        "Floor": [floor]
    })
    prediction = model.predict(input_data)
  
    predicted_price = prediction[0]
  
    st.success(f"Predicted House Price: ₹{predicted_price:,.2f}")
