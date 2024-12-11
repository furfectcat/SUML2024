import requests
import csv
import os
from datetime import datetime, timedelta


# Funkcja pobierająca kursy walut z API NBP w podanych rocznych przedziałach czasu
def fetch_exchange_rates(currency, start_date, end_date):
    rates = []
    current_start_date = start_date

    # Pobieramy dane rok po roku
    while current_start_date < end_date:
        # Ustawiamy datę końcową na koniec bieżącego roku lub na end_date, jeśli jesteśmy w ostatnim roku
        current_end_date = min(current_start_date.replace(year=current_start_date.year + 1) - timedelta(days=1),
                               end_date)

        url = f"https://api.nbp.pl/api/exchangerates/rates/a/{currency}/{current_start_date.strftime('%Y-%m-%d')}/{current_end_date.strftime('%Y-%m-%d')}/?format=json"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json().get("rates", [])
            rates.extend([
                {"date": rate["effectiveDate"], "rate": rate["mid"]}
                for rate in data
            ])
            print(
                f"Fetched data for {currency} from {current_start_date.strftime('%Y-%m-%d')} to {current_end_date.strftime('%Y-%m-%d')}")
        else:
            print(
                f"Error fetching data for {currency} from {current_start_date.strftime('%Y-%m-%d')} to {current_end_date.strftime('%Y-%m-%d')}: {response.status_code}")

        # Przesuwamy start do początku kolejnego roku
        current_start_date = current_end_date + timedelta(days=1)

    return rates


# Funkcja zapisująca dane do pliku CSV w folderze 'data'
def save_to_csv(currency, data):
    # Upewniamy się, że folder 'data' istnieje
    os.makedirs('data', exist_ok=True)

    # Ścieżka do pliku w folderze 'data'
    filename = os.path.join('data', f"{currency.upper()}_exchange_rates.csv")

    # Zapisujemy dane do pliku
    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["date", "rate"])
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    print(f"Saved {currency.upper()} exchange rates to {filename}")


if __name__ == "__main__":
    currencies = ['eur', 'gbp', 'chf', 'usd', 'czk']
    start_date = datetime.strptime("2014-01-01", "%Y-%m-%d")
    end_date = datetime.now()

    for currency in currencies:
        print(f"Pobieranie danych dla {currency.upper()}...")
        data = fetch_exchange_rates(currency, start_date, end_date)
        if data:
            save_to_csv(currency, data)
        else:
            print(f"Brak danych dla {currency.upper()} w podanym zakresie czasu.")
