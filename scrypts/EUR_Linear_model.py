import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from datetime import datetime
import joblib
import os

# Create directories if they do not exist
os.makedirs('models', exist_ok=True)

# Load the data
data = pd.read_csv('../data/EUR_exchange_rates.csv')

# Convert date to datetime and create numerical features
data['date'] = pd.to_datetime(data['date'])
data['date_ordinal'] = data['date'].map(datetime.toordinal)

# Features and target
X = data[['date_ordinal']]
y = data['rate']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=40)

# Create and train the Linear Regression model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# Save the model
joblib.dump(linear_model, '../models/EUR_Linear_model.pkl')
