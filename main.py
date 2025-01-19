import streamlit as st
import joblib
import pandas as pd
import numpy as np
from datetime import datetime

# Załaduj wytrenowane modele regresji liniowej
models = {
    'CHF': joblib.load('./models/CHF_Linear_model.pkl'),
    'GBP': joblib.load('./models/GBP_Linear_model.pkl'),
    'USD': joblib.load('./models/USD_Linear_model.pkl'),
    'CZK': joblib.load('./models/CZK_Linear_model.pkl'),
    'EUR': joblib.load('./models/EUR_Linear_model.pkl'),
}

# Funkcja do przewidywania kursu waluty
def predict_rate(input_date, model):
    # Zamiana daty na liczbę porządkową
    input_date_ordinal = np.array([[pd.to_datetime(input_date).toordinal()]])

    # Przewidywanie kursu
    predicted_rate = model.predict(input_date_ordinal)
    return predicted_rate[0]

# Nagłówek aplikacji
st.title("Currency Rate Prediction")

# Wybór waluty
currency_options = ['CHF', 'GBP', 'USD', 'CZK', 'EUR']
currency = st.selectbox("Wybierz walutę", currency_options)

# Wybór daty
input_date = st.date_input(
    "Wybierz datę (przeszła lub przyszła)",
    min_value=datetime(2020, 1, 1)  # Zakres dat od 2020 roku
)

# Przycisk do przewidywania
if st.button('Przewiduj kurs'):
    try:
        # Załaduj odpowiedni model dla wybranej waluty
        model = models[currency]

        # Przewidywanie kursu
        predicted_rate = predict_rate(input_date, model)

        # Wyświetlenie wyniku
        st.write(f"Przewidywany kurs {currency} na dzień {input_date}: {predicted_rate:.4f}")
    except Exception as e:
        st.error(f"Wystąpił błąd: {e}")
