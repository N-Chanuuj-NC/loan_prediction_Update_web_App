import pickle
from pathlib import Path

import numpy as np
import streamlit as st


BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "src" / "model.pkl"

st.set_page_config(
    page_title="Loan Approval Prediction",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 Loan Approval Prediction App")
st.write(
    "This app predicts whether a loan application will be approved "
    "based on applicant income and credit score."
)

@st.cache_resource
def load_model():
    with open(MODEL_PATH, "rb") as file:
        return pickle.load(file)

model = load_model()

st.subheader("Enter Applicant Details")

income = st.number_input(
    "Applicant Income",
    min_value=0,
    value=30000,
    step=1000
)

credit_score = st.number_input(
    "Credit Score",
    min_value=300,
    max_value=900,
    value=650,
    step=10
)

if st.button("Predict Loan Status"):
    input_data = np.array([[income, credit_score]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Not Approved")

st.markdown("---")
st.caption("Built with Python, Scikit-learn, and Streamlit")