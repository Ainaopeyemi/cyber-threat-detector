import streamlit as st
import joblib
import pandas as pd

# Load the artifacts
model = joblib.load('threat_model.pkl')
encoder = joblib.load('encoder.pkl')
feature_names = joblib.load('feature_names.pkl')

st.title("🛡️ Network Threat Detector")
st.write("Enter network parameters to check for suspicious activity.")

packet_size = st.number_input("Packet Size (bytes)", min_value=0)
logins = st.number_input("Recent Login Attempts", min_value=0)

if st.button("Analyze Traffic"):
    # This matches the structure we used in the training script
    prediction = model.predict([[packet_size, logins]])
    if prediction[0] == 1:
        st.error("⚠️ Threat Detected: High probability of malicious intent.")
    else:
        st.success("✅ Traffic Clear: Normal activity patterns.")
