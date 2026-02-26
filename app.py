if st.button("Predict"):
    # The keys in this dictionary MUST match X_train.columns exactly
    input_dict = {
        'Tenure': tenure, 
        'MonthlyCharges': monthly_charges, 
        'TotalCharges': total_charges
    }
    
    # Convert to DataFrame
    input_df = pd.DataFrame([input_dict])
    
    # Ensure the order is identical to the training data
    # (Replace this list with the output from print(list(X_train.columns)))
    expected_columns = ['Tenure', 'MonthlyCharges', 'TotalCharges'] 
    input_df = input_df[expected_columns]
    
    prediction = model.predict(input_df)
