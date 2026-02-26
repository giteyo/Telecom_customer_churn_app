import streamlit as st
import joblib
import pandas as pd
import numpy as np

if st.button("Predict"):
    # Convert "Yes"/"No" and categories into numbers manually
    input_dict = {
        'Senior Citizen': senior,
        'Partner': 1 if partner == "Yes" else 0,
        'Dependents': 1 if dependents == "Yes" else 0,
        'Tenure': tenure,
        'Phone Service': 1 if phone == "Yes" else 0,
        'Multiple Lines': 1 if multiple == "Yes" else (0 if multiple == "No" else 2),
        'Internet Service': 1 if internet == "Fiber optic" else (0 if internet == "DSL" else 2),
        'Online Security': 1 if online_sec == "Yes" else 0,
        'Online Backup': 1 if online_bak == "Yes" else 0,
        'Device Protection': 1 if device_prot == "Yes" else 0,
        'Tech Support': 1 if tech_supp == "Yes" else 0,
        'Streaming TV': 1 if tv == "Yes" else 0,
        'Streaming Movies': 1 if movies == "Yes" else 0,
        'Contract': 0 if contract == "Month-to-month" else (1 if contract == "One year" else 2),
        'Paperless Billing': 1 if paperless == "Yes" else 0,
        'Payment Method': 0 if payment == "Electronic check" else 1, # Simplified for example
        'Monthly Charges': monthly,
        'Total Charges': total
    }

    input_df = pd.DataFrame([input_dict])
    
    # Ensure columns are in the exact order again
    column_order = [
        'Senior Citizen', 'Partner', 'Dependents', 'Tenure', 'Phone Service', 
        'Multiple Lines', 'Internet Service', 'Online Security', 'Online Backup', 
        'Device Protection', 'Tech Support', 'Streaming TV', 'Streaming Movies', 
        'Contract', 'Paperless Billing', 'Payment Method', 'Monthly Charges', 'Total Charges'
    ]
    input_df = input_df[column_order]

    # Convert all to float to satisfy numpy
    input_df = input_df.astype(float) 

    prediction = model.predict(input_df)
    # ... result logic

