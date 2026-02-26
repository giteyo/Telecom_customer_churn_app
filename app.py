import streamlit as st
import joblib
import pandas as pd

# Load the model
model = joblib.load('churn_pipeline.joblib')

st.title("Telco Customer Churn Predictor")

# --- STEP 1: DEFINE EVERY SINGLE INPUT ---
st.header("Enter Customer Details")

col1, col2 = st.columns(2)

with col1:
    senior = st.selectbox("Senior Citizen", [0, 1])
    partner = st.selectbox("Partner", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["Yes", "No"])
    tenure = st.slider("Tenure (Months)", 0, 72, 24)
    phone = st.selectbox("Phone Service", ["Yes", "No"])
    multiple = st.selectbox("Multiple Lines", ["No phone service", "No", "Yes"])
    internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    online_sec = st.selectbox("Online Security", ["No internet service", "No", "Yes"])
    online_bak = st.selectbox("Online Backup", ["No internet service", "No", "Yes"])

with col2:
    device_prot = st.selectbox("Device Protection", ["No internet service", "No", "Yes"])
    tech_supp = st.selectbox("Tech Support", ["No internet service", "No", "Yes"])
    tv = st.selectbox("Streaming TV", ["No internet service", "No", "Yes"])
    movies = st.selectbox("Streaming Movies", ["No internet service", "No", "Yes"])
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
    payment = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])
    monthly = st.number_input("Monthly Charges", value=65.0)
    total = st.number_input("Total Charges", value=1500.0)

# --- STEP 2: ARRANGE IN THE EXACT ORDER ---
if st.button("Predict"):
    # This dictionary matches your X_train column names EXACTLY
    input_data = pd.DataFrame([{
        'Senior Citizen': senior,
        'Partner': partner,
        'Dependents': dependents,
        'Tenure': tenure,
        'Phone Service': phone,
        'Multiple Lines': multiple,
        'Internet Service': internet,
        'Online Security': online_sec,
        'Online Backup': online_bak,
        'Device Protection': device_prot,
        'Tech Support': tech_supp,
        'Streaming TV': tv,
        'Streaming Movies': movies,
        'Contract': contract,
        'Paperless Billing': paperless,
        'Payment Method': payment,
        'Monthly Charges': monthly,
        'Total Charges': total
    }])

    # Ensure column order is exactly what the model expects
    column_order = [
        'Senior Citizen', 'Partner', 'Dependents', 'Tenure', 'Phone Service', 
        'Multiple Lines', 'Internet Service', 'Online Security', 'Online Backup', 
        'Device Protection', 'Tech Support', 'Streaming TV', 'Streaming Movies', 
        'Contract', 'Paperless Billing', 'Payment Method', 'Monthly Charges', 'Total Charges'
    ]
    input_df = input_data[column_order]

    # --- STEP 3: PREDICT ---
    prediction = model.predict(input_df)
    
    if prediction[0] == 1:
        st.error("Result: High Risk of Churn")
    else:
        st.success("Result: Customer Likely to Stay")
