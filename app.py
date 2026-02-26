import streamlit as st
import joblib
import pandas as pd

# Load the model
model = joblib.load('churn_pipeline.joblib')

# ... (Your UI code for inputs: tenure, monthly_charges, etc.) ...

if st.button("Predict Churn"):
    # 1. Create the dictionary with EXACT matches to your list
    # Note: Ensure the variables (tenure, partner, etc.) are defined above in your UI
    input_dict = {
        'Senior Citizen': senior_citizen, 
        'Partner': partner, 
        'Dependents': dependents, 
        'Tenure': tenure, 
        'Phone Service': phone_service, 
        'Multiple Lines': multiple_lines, 
        'Internet Service': internet_service, 
        'Online Security': online_security, 
        'Online Backup': online_backup, 
        'Device Protection': device_protection, 
        'Tech Support': tech_support, 
        'Streaming TV': streaming_tv, 
        'Streaming Movies': streaming_movies, 
        'Contract': contract, 
        'Paperless Billing': paperless_billing, 
        'Payment Method': payment_method, 
        'Monthly Charges': monthly_charges, 
        'Total Charges': total_charges
    }
    
    # 2. Convert to DataFrame
    input_df = pd.DataFrame([input_dict])
    
    # 3. Explicitly reorder columns to match X_train exactly
    # This prevents the "Feature Name" ValueError
    column_order = [
        'Senior Citizen', 'Partner', 'Dependents', 'Tenure', 'Phone Service', 
        'Multiple Lines', 'Internet Service', 'Online Security', 'Online Backup', 
        'Device Protection', 'Tech Support', 'Streaming TV', 'Streaming Movies', 
        'Contract', 'Paperless Billing', 'Payment Method', 'Monthly Charges', 'Total Charges'
    ]
    input_df = input_df[column_order]
    
    # 4. Predict
    try:
        prediction = model.predict(input_df)
        if prediction[0] == 1:
            st.error("High Risk: Customer is likely to Churn")
        else:
            st.success("Low Risk: Customer is likely to Stay")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
