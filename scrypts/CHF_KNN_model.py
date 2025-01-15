import os
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime
import joblib

# Create directories if they do not exist
os.makedirs('models', exist_ok=True)

# Load the data
data = pd.read_csv('../data/CHF_exchange_rates.csv')

# Convert date to datetime and create numerical features
data['date'] = pd.to_datetime(data['date'])
data['date_ordinal'] = data['date'].map(datetime.toordinal)

# Features and target
X = data[['date_ordinal']]
y = data['rate']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=68)

# Scale the features using MinMaxScaler
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train the KNN model
knn = KNeighborsRegressor(n_neighbors=10)
knn.fit(X_train_scaled, y_train)

# Save the model and scaler
joblib.dump(knn, '../models/CHF_KNN_model.pkl')
joblib.dump(scaler, '../models/CHF_scaler.pkl')

# Optional: Test predictions
print("Sample predictions:")
sample_dates = [datetime(2025, 1, 15).toordinal(), datetime(2025, 1, 16).toordinal(), datetime(2025, 1, 17).toordinal()]
for date in sample_dates:
    # Tworzymy DataFrame z odpowiednią nazwą kolumny
    date_df = pd.DataFrame([[date]], columns=['date_ordinal'])
    scaled_date = scaler.transform(date_df)
    prediction = knn.predict(scaled_date)[0]
    print(f"Prediction for date {datetime.fromordinal(date)}: {prediction}")



