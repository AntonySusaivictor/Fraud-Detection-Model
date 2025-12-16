import streamlit as st
import pandas as pd
import joblib

model = joblib.load("Fraud_Detection_Model.pkl")
st.title("Fraud_Detector_APP")
st.markdown("please enter the transaction details to find the fraud")

st.divider()

transaction_type = st.selectbox("Trasaction_type",["CASH_OUT","TRANSFER","PAYMENT"])
amount = st.number_input("AMOUNT", min_value= 0.0, value=1000.0)
oldbalanceOrg = st.number_input("OLD BALANCE (sender)", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("NEW BALANCE (SENDER)",min_value=0.0, value=10000.0)
oldbalanceDest = st.number_input("OLD BALANCE (RECIVER)",min_value=0.0, value=10000.0)
newbalanceDest = st.number_input("NEW BALANCE (RECIVER)",min_value=0.0, value=10000.0)

if st.button("Predict"):
    input_data= pd.DataFrame([{
      "type": transaction_type,
      "amount" : amount,
      "oldbalanceOrg": oldbalanceOrg,
      "oldbalanceDest": oldbalanceDest,
      "newbalanceOrig": newbalanceOrig,
      "newbalanceDest" : newbalanceDest 
    }])

    prediction = model.predict(input_data)[0]
    st.subheader(f"prediction: '{int(prediction)}'")

    if prediction ==1:
        st.error("TRANSCATION LOOKS FRAUD NEED ATTENTION !")
    else:
        st.success("TRANSACTION LOOKS LIGIT")