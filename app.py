import streamlit as st
import pandas as pd
import joblib

model = joblib.load("Models/random_forest_model.pkl")
st.title("NovaPay Fraud Detection App")
st.write("Enter transaction details to predict fraud risk.")
preprocessor = joblib.load("Models/preprocessor.pkl")


home_country = st.selectbox("Home Country", ["us", "uk", "ca", "unknown"])
source_currency = st.selectbox("Source Currency", ["usd", "gbp", "cad"])
dest_currency = st.selectbox("Destination Currency", ["usd", "gbp", "cad", "eur", "cny", "mxn", "ngn", "php", "inr"])
channel = st.selectbox("Channel", ["web", "mobile", "atm", "unknown"])

amount_src = st.number_input("Amount Source Currency", min_value=0.0)
amount_usd = st.number_input("Amount USD", min_value=0.0)
fee = st.number_input("Fee", min_value=0.0)
exchange_rate_src_to_dest = st.number_input("Exchange Rate Source to Destination", min_value=0.0)

new_device = st.selectbox("New Device", [False, True])
ip_country = st.selectbox("IP Country", ["us", "uk", "ca", "unknown"])
location_mismatch = st.selectbox("Location Mismatch", [False, True])

ip_risk_score = st.number_input("IP Risk Score", min_value=0.0)
kyc_tier = st.selectbox("KYC Tier", ["low", "medium", "high"])
account_age_days = st.number_input("Account Age Days", min_value=0)
device_trust_score = st.slider("Device Trust Score", 0.0, 1.0, 0.5)
chargeback_history_count = st.number_input("Chargeback History Count", min_value=0)
risk_score_internal = st.number_input("Internal Risk Score", min_value=0.0)
txn_velocity_1h = st.number_input("Transaction Velocity 1h", min_value=0)
txn_velocity_24h = st.number_input("Transaction Velocity 24h", min_value=0)
corridor_risk = st.number_input("Corridor Risk", min_value=0.0)

month = st.slider("Month", 1, 12, 6)
weekday = st.slider("Weekday", 0, 6, 2)
hour = st.slider("Hour", 0, 23, 12)

input_data = pd.DataFrame({
    "home_country": [home_country],
    "source_currency": [source_currency],
    "dest_currency": [dest_currency],
    "channel": [channel],
    "amount_src": [amount_src],
    "amount_usd": [amount_usd],
    "fee": [fee],
    "exchange_rate_src_to_dest": [exchange_rate_src_to_dest],
    "new_device": [new_device],
    "ip_country": [ip_country],
    "location_mismatch": [location_mismatch],
    "ip_risk_score": [ip_risk_score],
    "kyc_tier": [kyc_tier],
    "account_age_days": [account_age_days],
    "device_trust_score": [device_trust_score],
    "chargeback_history_count": [chargeback_history_count],
    "risk_score_internal": [risk_score_internal],
    "txn_velocity_1h": [txn_velocity_1h],
    "txn_velocity_24h": [txn_velocity_24h],
    "corridor_risk": [corridor_risk],
    "month": [month],
    "weekday": [weekday],
    "hour": [hour]
})

if st.button("Predict Fraud"):
    processed_input = preprocessor.transform(input_data)
    prediction = model.predict(processed_input)[0]
    probability = model.predict_proba(processed_input)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error(f"Fraud Detected — Probability: {probability:.2%}")
    else:
        st.success(f"Legitimate Transaction — Fraud Probability: {probability:.2%}")

    st.write("Input Data")
    st.dataframe(input_data)