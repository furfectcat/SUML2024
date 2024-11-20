
import pandas as pd
from datetime import datetime
import numpy as np
import joblib
import os

def predict_currency_rate(input_date):
    """Predict the currency rate for a given date."""
    # Load the model and scaler
    model_path = './models/CZK_KNN_model.pkl'
    scaler_path = './models/CZK_scaler.pkl'
    
    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        raise FileNotFoundError("Model or scaler files not found. Ensure they are in the 'models' folder.")
    
    knn = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    
    # Convert input date to ordinal
    input_date_ordinal = np.array([[datetime.toordinal(pd.to_datetime(input_date))]])
    input_date_scaled = scaler.transform(input_date_ordinal)
    
    # Predict and return the result
    return knn.predict(input_date_scaled)[0]

# Example usage
if __name__ == "__main__":
    example_date = '2024-11-01'
    prediction = predict_currency_rate(example_date)
    print(f"Predicted rate for {example_date}: {prediction}")
