import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the fitted pipeline
model = joblib.load('churn_pipeline.joblib')

st.title("Customer Churn Prediction")

# --- UI INPUTS ---
col1, col2 = st.columns(2)

with col1:
    senior = st.selectbox("Senior Citizen (1=Yes, 0=No)", [0, 1])
    partner = st.selectbox("Partner", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["Yes", "No"])
    tenure = st.number_input("Tenure (Months)", 0, 100, 24)
    phone = st.selectbox("Phone Service", ["Yes", "No"])
    multiple = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
    internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    security = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
    backup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"])

with col2:
    protection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
    support = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])
    tv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
    movies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
    payment = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])
    monthly = st.number_input("Monthly Charges", 0.0, 200.0, 65.0)
    total = st.number_input("Total Charges", 0.0, 10000.0, 1500.0)

# --- PREDICTION LOGIC ---
if st.button("Predict"):
    # 1. Map text to numbers (Matches typical Churn dataset encoding)
    input_dict = {
        'Senior Citizen': senior,
        'Partner': 1 if partner == "Yes" else 0,
        'Dependents': 1 if dependents == "Yes" else 0,
        'Tenure': tenure,
        'Phone Service': 1 if phone == "Yes" else 0,
        'Multiple Lines': 1 if multiple == "Yes" else 0,
        'Internet Service': 1 if internet == "Fiber optic" else 0,
        'Online Security': 1 if security == "Yes" else 0,
        'Online Backup': 1 if backup == "Yes" else 0,
        'Device Protection': 1 if protection == "Yes" else 0,
        'Tech Support': 1 if support == "Yes" else 0,
        'Streaming TV': 1 if tv == "Yes" else 0,
        'Streaming Movies': 1 if movies == "Yes" else 0,
        'Contract': 0 if contract == "Month-to-month" else (1 if contract == "One year" else 2),
        'Paperless Billing': 1 if paperless == "Yes" else 0,
        'Payment Method': 0 if "check" in payment.lower() else 1,
        'Monthly Charges': monthly,
        'Total Charges': total
    }

    # 2. Create DataFrame
    df = pd.DataFrame([input_dict])

    # 3. FORCE ORDER (Crucial for SVM)
    column_order = [
        'Senior Citizen', 'Partner', 'Dependents', 'Tenure', 'Phone Service', 
        'Multiple Lines', 'Internet Service', 'Online Security', 'Online Backup', 
        'Device Protection', 'Tech Support', 'Streaming TV', 'Streaming Movies', 
        'Contract', 'Paperless Billing', 'Payment Method', 'Monthly Charges', 'Total Charges'
    ]
    df = df[column_order]

    # 4. Predict
    res = model.predict(df)
    
    st.divider()
    if res[0] == 1:
        st.error("Prediction: Customer is likely to CHURN")
    else:
        st.success("Prediction: Customer is likely to STAY")