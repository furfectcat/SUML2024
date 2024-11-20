
import streamlit as st
import joblib
import pandas as pd
import numpy as np
from datetime import datetime

# Załaduj wytrenowane modele i skalery
knn_chf = joblib.load('./models/CHF_KNN_model.pkl')
scaler = joblib.load('./models/CHF_scaler.pkl')

# Funkcja do przewidywania kursu waluty
def predict_rate(input_date, model, scaler):
    input_date_ordinal = np.array([[datetime.toordinal(pd.to_datetime(input_date))]])
    input_date_scaled = scaler.transform(input_date_ordinal)
    return model.predict(input_date_scaled)[0]

# Nagłówek aplikacji
st.title("Currency Rate Prediction")

# Wybór waluty
currency_options = ['CHF', 'GBP', 'USD', 'CZK', 'EUR']
currency = st.selectbox("Wybierz walutę", currency_options)

# Wybór daty
input_date = st.date_input("Wybierz datę", min_value=datetime(2020, 1, 1), max_value=datetime.today())

# Przycisk do przewidywania
if st.button('Przewiduj kurs'):
    if currency == 'CHF':
        # Przewidywanie kursu dla CHF
        predicted_rate = predict_rate(input_date, knn_chf, scaler)
    elif currency == 'GBP':
        # Załaduj model i skalery dla GBP i powtórz proces przewidywania
        # Przewidywanie kursu dla GBP
        predicted_rate = "Model dla GBP jeszcze nie załadowany."  # Zastąp w razie potrzeby
    elif currency == 'USD':
        # Załaduj model i skalery dla USD i powtórz proces przewidywania
        predicted_rate = "Model dla USD jeszcze nie załadowany."  # Zastąp w razie potrzeby
    elif currency == 'CZK':
        # Załaduj model i skalery dla CZK i powtórz proces przewidywania
        predicted_rate = "Model dla CZK jeszcze nie załadowany."  # Zastąp w razie potrzeby
    elif currency == 'EUR':
        # Załaduj model i skalery dla EUR i powtórz proces przewidywania
        predicted_rate = "Model dla EUR jeszcze nie załadowany."  # Zastąp w razie potrzeby

    # Wyświetlenie wyniku
    st.write(f"Przewidywany kurs {currency} na dzień {input_date}: {predicted_rate:.4f}" if isinstance(predicted_rate, float) else predicted_rate)

# Uruchomienie aplikacji w Streamlit
