import streamlit as st
import numpy as np

st.title("Medical Insurance Cost Predictor")

age = st.number_input("Enter Age", min_value=18, max_value=100)
bmi = st.number_input("Enter BMI")
children = st.number_input("Number of Children", min_value=0, max_value=10)

if st.button("Predict"):
    input_data = np.array([[age, bmi, children]])  # Ensure this matches model input
    prediction = loaded_model.predict(input_data)
    st.write(f"Predicted Insurance Cost: ${prediction[0]:.2f}")
