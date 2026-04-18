import joblib
import numpy as np

# Load the model we trained in the Notebook
model = joblib.load('fraud_model.pkl')

def evaluate_transaction(amount, time_sec):
    # Model expects 2D array: [[Amount, Time]]
    prediction = model.predict([[amount, time_sec]])
    
    if prediction[0] == -1:
        return "🚨 ALERT: High Anomaly Detected! Flagging for Fraud."
    return "✅ Transaction Verified: Normal."

# Simulate testing
print(evaluate_transaction(25000.0, 100)) # Suspicious: High amount, low time
print(evaluate_transaction(50.0, 45000))   # Normal: Low amount, mid-day