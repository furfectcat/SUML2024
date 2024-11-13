import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, accuracy_score, classification_report
from sklearn.model_selection import train_test_split
import joblib
import numpy as np
import os


# Funkcja do trenowania modelu dla pojedynczego pliku
def train_model(filename):
    # Wczytaj dane z pliku CSV
    data = pd.read_csv(filename)

    # Konwertowanie kolumny 'date' na format datetime
    data['date'] = pd.to_datetime(data['date'])

    # Dodanie kolumny celu (target) - 1 jeśli następna wartość wzrośnie, 0 jeśli spadnie
    data['target'] = np.where(data['rate'].shift(-1) > data['rate'], 1, 0)

    # Usunięcie ostatniego wiersza, gdzie target jest NaN
    data = data.dropna()

    # Ekstrakcja cech
    data['day_of_week'] = data['date'].dt.dayofweek
    data['day'] = data['date'].dt.day
    data['month'] = data['date'].dt.month
    X = data[['rate', 'day_of_week', 'day', 'month']]
    y = data['target']

    # Podział na dane treningowe i testowe
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Tworzenie i trenowanie modelu
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predykcje
    predictions = model.predict(X_test)
    predictions_binary = [1 if pred > 0.5 else 0 for pred in predictions]

    # Obliczanie metryk
    mse = mean_squared_error(y_test, predictions)
    accuracy = accuracy_score(y_test, predictions_binary)
    report = classification_report(y_test, predictions_binary)

    # Upewnij się, że folder "models" istnieje
    os.makedirs("models", exist_ok=True)

    # Zapisz model do pliku
    model_name = "models/" + os.path.basename(filename).split('_')[0] + "_model.pkl"
    joblib.dump(model, model_name)

    # Wyświetl metryki
    print(f"Metryki dla modelu {model_name}:")
    print(f"Mean Squared Error: {mse}")
    print(f"Accuracy: {accuracy}")
    print("Classification Report:")
    print(report)
    print("-" * 50)


# Ścieżka do folderu z plikami CSV
data_folder = "data"

# Lista plików CSV w folderze "data"
files = [os.path.join(data_folder, file) for file in os.listdir(data_folder) if file.endswith('.csv')]

# Trenuj modele dla każdego pliku
for file in files:
    train_model(file)
