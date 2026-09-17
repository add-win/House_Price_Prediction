import streamlit as st
import joblib
import pandas as pd

model = joblib.load("log_reg_house_model.pkl")

st.title("House Price Prediction")

area = st.number_input(
    "Enter the Square Feet",
    min_value=0.0,
    max_value=5000.0,
    value=600.0
)

bedroom = st.number_input(
    "Enter the Number of Bedrooms",
    min_value=0.0,
    max_value=10.0,
    value=1.0
)

floor = st.number_input(
    "Enter the Number of Floors",
    min_value=0.0,
    max_value=20.0,
    value=0.0
)

if st.button("Predict"):

    if area < 600 or area > 3000:
        st.error("Cannot predict: Area must be between 600 and 3000.")

    elif bedroom < 1 or bedroom > 4:
        st.error("Cannot predict: Bedrooms must be between 1 and 4.")

    elif floor < 0 or floor > 10:
        st.error("Cannot predict: Floors must be between 0 and 10.")

    else:
        input_data = pd.DataFrame({
            "Area": [area],
            "Bedrooms": [bedroom],
            "Floor": [floor]
        })

        prediction = model.predict(input_data)

        predicted_price = prediction[0]

        st.success(f"Predicted House Price: ₹{predicted_price:,.2f}")
