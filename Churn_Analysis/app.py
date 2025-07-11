import streamlit as st
import joblib
import pandas as pd
import numpy as np

# --- Load model and metadata ---
@st.cache_resource
def load_model_bundle():
    return joblib.load('/Users/kirant/PythonProjects/DataScienceProjects/Churn_Analysis/model/model_bundle.joblib')

bundle = load_model_bundle()
model = bundle['model']
threshold = bundle['threshold']
best_params = bundle['best_params']
metrics = bundle['metrics']

# --- App Title ---
st.title("Customer Churn Prediction App")

st.sidebar.header("Model Details")
st.sidebar.json(best_params)
st.sidebar.metric("F1 Score", f"{metrics['f1_score']:.2f}")

# --- Input UI ---
st.header("Enter Customer Information")

gender = st.selectbox("Gender", ['Male', 'Female'])
SeniorCitizen = st.selectbox("Senior Citizen", ['Yes', 'No'])
Partner = st.selectbox("Has Partner?", ['Yes', 'No'])
Dependents = st.selectbox("Has Dependents?", ['Yes', 'No'])
tenure = st.slider("Tenure (months)", min_value=0, max_value=72, value=12)
PhoneService = st.selectbox("Phone Service", ['Yes', 'No'])
MultipleLines = st.selectbox("Multiple Lines", ['No phone service', 'No', 'Yes'])
InternetService = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
OnlineSecurity = st.selectbox("Online Security", ['No internet service', 'No', 'Yes'])
OnlineBackup = st.selectbox("Online Backup", ['No internet service', 'No', 'Yes'])
DeviceProtection = st.selectbox("Device Protection", ['No internet service', 'No', 'Yes'])
TechSupport = st.selectbox("Tech Support", ['No internet service', 'No', 'Yes'])
StreamingTV = st.selectbox("Streaming TV", ['No internet service', 'No', 'Yes'])
StreamingMovies = st.selectbox("Streaming Movies", ['No internet service', 'No', 'Yes'])
Contract = st.selectbox("Contract Type", ['Month-to-month', 'One year', 'Two year'])
PaperlessBilling = st.selectbox("Paperless Billing", ['Yes', 'No'])
PaymentMethod = st.selectbox("Payment Method", [
    'Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'
])
MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)

# --- Create Input Row ---
raw_input = {
    'SeniorCitizen': 1 if SeniorCitizen == 'Yes' else 0,
    'Partner': 1 if Partner == 'Yes' else 0,
    'Dependents': 1 if Dependents == 'Yes' else 0,
    'tenure': tenure,
    'PhoneService': 1 if PhoneService == 'Yes' else 0,
    'PaperlessBilling': 1 if PaperlessBilling == 'Yes' else 0,
    'MonthlyCharges': MonthlyCharges,
    'TotalCharges': tenure * MonthlyCharges,  # Assuming TotalCharges is tenure * MonthlyCharges
}

# One-hot encoded columns for the below features (same as training)
one_hot_cols = {
    'gender': ['Female', 'Male'],
    'MultipleLines': ['No phone service', 'No', 'Yes'],
    'InternetService': ['DSL', 'Fiber optic', 'No'],
    'OnlineSecurity': ['No internet service', 'No', 'Yes'],
    'OnlineBackup': ['No internet service', 'No', 'Yes'],
    'DeviceProtection': ['No internet service', 'No', 'Yes'],
    'TechSupport': ['No internet service', 'No', 'Yes'],
    'StreamingTV': ['No internet service', 'No', 'Yes'],
    'StreamingMovies': ['No internet service', 'No', 'Yes'],
    'Contract': ['Month-to-month', 'One year', 'Two year'],
    'PaymentMethod': [
        'Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'
    ]
}

# Manually one-hot encode the current selection
for col, values in one_hot_cols.items():
    for val in values:
        col_name = f"{col}_{val}"
        raw_input[col_name] = 1 if eval(col) == val else 0

# Create input DataFrame
input_df = pd.DataFrame([raw_input])

# --- Predict ---
if st.button("Predict Churn"):
    probability = model.predict_proba(input_df)[0][1]
    prediction = int(probability > threshold)

    st.subheader("Prediction Result")
    st.write(f"Probability of Churn: `{probability:.3f}`")
    st.write(f"Predicted Churn: `{prediction}`")

    if prediction == 1:
        st.error("Customer is likely to churn ❌")
    else:
        st.success("Customer is likely to stay ✅")
