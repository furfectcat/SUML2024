import streamlit as st
import joblib
import pandas as pd
import numpy as np
from datetime import datetime

# Załaduj wytrenowane modele i skalery
models = {
    'CHF': joblib.load('./models/CHF_KNN_model.pkl'),
    'GBP': joblib.load('./models/GBP_KNN_model.pkl'),
    'USD': joblib.load('./models/USD_KNN_model.pkl'),
    'CZK': joblib.load('./models/CZK_KNN_model.pkl'),
    'EUR': joblib.load('./models/EUR_KNN_model.pkl'),
}

scalers = {
    'CHF': joblib.load('./models/CHF_scaler.pkl'),
    'GBP': joblib.load('./models/GBP_scaler.pkl'),
    'USD': joblib.load('./models/USD_scaler.pkl'),
    'CZK': joblib.load('./models/CZK_scaler.pkl'),
    'EUR': joblib.load('./models/EUR_scaler.pkl'),
}


# Funkcja do przewidywania kursu waluty
def predict_rate(input_date, model, scaler):
    # Zamiana daty na liczbę porządkową
    input_date_ordinal = np.array([[pd.to_datetime(input_date).toordinal()]])

    # Dopasowanie skalera do bieżącej daty (opcjonalnie rozszerz zakres skalera)
    input_date_scaled = scaler.transform(input_date_ordinal)

    # Przewidywanie kursu
    predicted_rate = model.predict(input_date_scaled)
    return predicted_rate[0]


# Nagłówek aplikacji
st.title("Currency Rate Prediction")

# Wybór waluty
currency_options = ['CHF', 'GBP', 'USD', 'CZK', 'EUR']
currency = st.selectbox("Wybierz walutę", currency_options)

# Wybór daty
input_date = st.date_input(
    "Wybierz datę (przeszła lub przyszła)",
    min_value=datetime(2020, 1, 1)
)

# Przycisk do przewidywania
if st.button('Przewiduj kurs'):
    try:
        # Załaduj odpowiedni model i skaler dla wybranej waluty
        model = models[currency]
        scaler = scalers[currency]

        # Przewidywanie kursu
        predicted_rate = predict_rate(input_date, model, scaler)

        # Wyświetlenie wyniku
        st.write(f"Przewidywany kurs {currency} na dzień {input_date}: {predicted_rate:.4f}")
    except Exception as e:
        st.write(f"Wystąpił błąd: {e}")
