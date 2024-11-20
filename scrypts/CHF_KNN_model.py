
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from datetime import datetime
import numpy as np
import joblib
import os

# Create directories if they do not exist
os.makedirs('./models', exist_ok=True)

# Load the data
data = pd.read_csv('./data/CHF_exchange_rates.csv')

# Convert date to datetime and create numerical features
data['date'] = pd.to_datetime(data['date'])
data['date_ordinal'] = data['date'].map(datetime.toordinal)

# Features and target
X = data[['date_ordinal']]
y = data['rate']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train the KNN model
knn = KNeighborsRegressor(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

# Save the model and scaler
joblib.dump(knn, './models/CHF_KNN_model.pkl')
joblib.dump(scaler, './models/CHF_scaler.pkl')

# Function to predict rate for a given date
def predict_rate(input_date):
    input_date_ordinal = np.array([[datetime.toordinal(pd.to_datetime(input_date))]])
    input_date_scaled = scaler.transform(input_date_ordinal)
    return knn.predict(input_date_scaled)[0]

# Example usage
if __name__ == "__main__":
    example_date = '2024-11-01'
    prediction = predict_rate(example_date)
    print(f"Predicted rate for {example_date}: {prediction}")
