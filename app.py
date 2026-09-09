import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("final_model.pkl", "rb"))

st.title("🏦 Loan Approval Prediction")
st.write("Enter the applicant details below:")

# Categorical / object columns
Gender = st.selectbox("Gender",["Male", "Female"])
Married = st.selectbox("Married",["Yes", "No"])
Dependents = st.selectbox("Dependents",["0", "1", "2", "3+"])
Education = st.selectbox("Education",["Graduate", "Not Graduate"])
Self_Employed = st.selectbox("Self Employed",["Yes", "No"])
Property_Area = st.selectbox("Property Area",["Urban", "Semiurban", "Rural"])

# Numerical columns
ApplicantIncome = st.number_input("Applicant Income",min_value=0,value=5000)
CoapplicantIncome = st.number_input("Coapplicant Income",min_value=0.0,value=0.0)
LoanAmount = st.number_input("Loan Amount",min_value=0.0,value=100.0)
Loan_Amount_Term = st.number_input("Loan Amount Term",min_value=0.0,value=360.0)
Credit_History = st.selectbox("Credit History",[1.0, 0.0])

# Prediction button
if st.button("Predict Loan Status"):

    # Create input data
    data = [[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,
             CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]]

    # Create DataFrame
    data = pd.DataFrame(data, columns=["Gender","Married","Dependents","Education",
        "Self_Employed","ApplicantIncome","CoapplicantIncome","LoanAmount",
        "Loan_Amount_Term","Credit_History","Property_Area"])

    categorical_columns = ["Gender", "Married", "Dependents", "Education",
                           "Self_Employed", "Property_Area"]
    data[categorical_columns] = data[categorical_columns].apply(
        lambda column: column.str.strip().str.lower()
    )

    # Prediction
    result = model.predict(data)

    # Display result
    if result[0] == 0:
        st.error("❌ Loan Rejected")
    else:
        st.success("✅ Loan Approved")
