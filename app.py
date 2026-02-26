import streamlit as st
import joblib
import pandas as pd

# 1. Load the Bundle
model = joblib.load('churn_pipeline.joblib')

st.set_page_config(page_title="Telco Churn Predictor", layout="wide")
st.title("📊 Customer Churn Analysis Tool")

# 2. Input UI (Grouped for better UX)
st.sidebar.header("Customer Demographics & Services")

# Numerical Inputs
tenure = st.sidebar.slider("Tenure (Months)", 0, 72, 12)
monthly = st.sidebar.number_input("Monthly Charges ($)", value=50.0)
total = st.sidebar.number_input("Total Charges ($)", value=500.0)

# Categorical Inputs (Drop-downs)
contract = st.sidebar.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
internet = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
payment = st.sidebar.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])

# Simple Yes/No selections
col1, col2 = st.columns(2)
with col1:
    senior = st.selectbox("Senior Citizen", ["0", "1"])
    partner = st.selectbox("Partner", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["Yes", "No"])
    online_sec = st.selectbox("Online Security", ["Yes", "No", "No internet service"])

with col2:
    paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
    tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
    streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])

# 3. Prediction Execution
if st.button("Calculate Churn Risk"):
    # Create a DataFrame matching your training data columns
    input_dict = {
        'Tenure': tenure, 'Monthly Charges': monthly, 'Total Charges': total,
        'Senior Citizen': senior, 'Partner': partner, 'Dependents': dependents,
        'Contract': contract, 'Internet Service': internet, 'Payment Method': payment,
        'Paperless Billing': paperless, 'Tech Support': tech_support, 'Streaming TV': streaming_tv,
        # Add remaining features here to match your exact X_train columns...
    }
    
    input_df = pd.DataFrame([input_dict])
    
    prediction = model.predict(input_df)
    
    if prediction[0] == 1:
        st.error("### Result: High Risk of Churn")
    else:
        st.success("### Result: Likely to Stay")