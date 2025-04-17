import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the trained model
model = joblib.load("model.pkl")

# Streamlit UI
st.set_page_config(page_title="🎓 Student Performance Predictor")
st.title("🎓 Student Performance Predictor")

st.markdown("Fill in the details to predict if the student will pass or fail:")

# Inputs from user
studytime = st.slider("Study Time (1=low, 4=high)", 1, 4, 2)
failures = st.slider("Number of Past Failures", 0, 4, 0)
absences = st.slider("Number of Absences", 0, 100, 4)
G1 = st.slider("Grade Period 1 (G1)", 0, 20, 10)
G2 = st.slider("Grade Period 2 (G2)", 0, 20, 10)

# Prepare feature names as used in model training
features = ["studytime", "failures", "absences", "G1", "G2"]

# Create a pandas DataFrame for prediction
input_data = pd.DataFrame({
    "studytime": [studytime],
    "failures": [failures],
    "absences": [absences],
    "G1": [G1],
    "G2": [G2]
})

# When the button is clicked, make a prediction
if st.button("Predict"):
    # Make prediction using the model
    prediction = model.predict(input_data)[0]
    confidence = model.predict_proba(input_data)[0][prediction]

    if prediction == 1:
        st.success(f"✅ Pass (Confidence: {confidence * 100:.2f}%)")
        st.info("Advice: Keep up the consistent study schedule!")
    else:
        st.error(f"❌ Fail (Confidence: {confidence * 100:.2f}%)")
        st.warning("Advice: Consider more study time and focus.")
