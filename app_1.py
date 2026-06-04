import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("student_model.pkl")

# Page title
st.title("🎓 Student Performance Prediction System")

st.write("Enter student details to predict Pass or Fail.")

# Inputs
study_hours = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=5.0
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)

previous_score = st.number_input(
    "Previous Score",
    min_value=0.0,
    max_value=100.0,
    value=60.0
)

# Prediction button
if st.button("Predict"):

    features = np.array([
        [study_hours, attendance, previous_score]
    ])

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("Student is likely to PASS")
    else:
        st.error("Student is likely to FAIL")