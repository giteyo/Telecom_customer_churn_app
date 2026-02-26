import streamlit as st
import joblib
import pandas as pd
import numpy as np

# 1. Load the model first
model = joblib.load('churn_pipeline.joblib')

# 2. Define your inputs (Sliders, Selectboxes) BEFORE the button
# Example:
tenure = st.sidebar.slider("Tenure", 0, 72, 12)
# ... add all your other inputs here ...

# 3. Finally, the button logic
if st.button("Predict"):
    # ... your prediction code ...
