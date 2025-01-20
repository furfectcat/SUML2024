# Przewidywanie kursów wymiany walut

Aplikacja webowa stworzona w celu przewidywania kursów wymiany walut dla pięciu najpopularniejszych walut:
- **CHF** (Frank szwajcarski)
- **GBP** (Funt brytyjski)
- **USD** (Dolar amerykański)
- **CZK** (Korona czeska)
- **EUR** (Euro)

Aplikacja korzysta z modeli regresji liniowej do prognozowania wartości walut na podstawie daty. Regularne aktualizacje modeli gwarantują dokładność przewidywań.

## Funkcjonalności
- Przewidywanie kursów wymiany walut dla dat historycznych i przyszłych.
- Intuicyjny interfejs webowy stworzony z wykorzystaniem Streamlit.
- Regularne aktualizacje danych i modeli dzięki zautomatyzowanemu pipeline w GitHub Actions.

## Demo
Aplikacja jest dostępna online: [https://suml2024-project.streamlit.app/](https://suml2024-project.streamlit.app/)

## Wymagania systemowe
- Python 3.8 lub nowszy
- Zainstalowane zależności (patrz sekcja "Instalacja")

## Instalacja
Aby uruchomić aplikację lokalnie, wykonaj poniższe kroki:

1. Sklonuj repozytorium:
    ```bash
    git clone https://github.com/yourusername/currency-prediction.git
    cd currency-prediction
    ```

2. Utwórz wirtualne środowisko i je aktywuj:
    ```bash
    python -m venv venv
    source venv/bin/activate # Na Windows: venv\Scripts\activate
    ```

3. Zainstaluj wymagane pakiety:
    ```bash
    pip install -r requirements.txt
    ```

4. Uruchom następujące skrypty, aby pobrać dane i wytrenować modele:
    ```bash
    python getData.py          # Pobiera dane z API NBP
    python CHF_Linear_model.py # Trenuje model dla CHF
    python CZK_Linear_model.py # Trenuje model dla CZK
    python EUR_Linear_model.py # Trenuje model dla EUR
    python GBP_Linear_model.py # Trenuje model dla GBP
    python USD_Linear_model.py # Trenuje model dla USD
    ```

    **Uwaga:** Każdy skrypt trenuje model regresji liniowej dla danej waluty i zapisuje go w katalogu `models/`.

5. Uruchom aplikację Streamlit:
    ```bash
    streamlit run streamlit_app.py
    ```

6. Aplikacja powinna być teraz dostępna pod adresem:
    ```
    http://localhost:8501
    ```

## Struktura projektu
- `data/` – katalog z danymi wejściowymi w formacie CSV.
- `models/` – katalog z wytrenowanymi modelami dla każdej waluty.
- `CHF_Linear_model.py` – skrypt trenujący model regresji liniowej dla CHF.
- `CZK_Linear_model.py` – skrypt trenujący model regresji liniowej dla CZK.
- `EUR_Linear_model.py` – skrypt trenujący model regresji liniowej dla EUR.
- `GBP_Linear_model.py` – skrypt trenujący model regresji liniowej dla GBP.
- `USD_Linear_model.py` – skrypt trenujący model regresji liniowej dla USD.
- `getData.py` – skrypt do pobierania danych z API NBP.
- `streamlit_app.py` – aplikacja webowa oparta na Streamlit.
- `.github/workflows/` – pliki YAML automatyzujące pobieranie danych i trenowanie modeli.

## Automatyzacja (GitHub Actions)
Repozytorium zawiera pipeline, który:
1. Codziennie pobiera dane o kursach walut z API Narodowego Banku Polskiego (NBP).
2. Trenuje modele regresji liniowej dla każdej waluty.
3. Zapisuje zaktualizowane modele w katalogu `models/`.

Dzięki temu aplikacja korzysta zawsze z najnowszych danych.



## Autorzy
Wojciech Fuśnik
Katarzyna Janeczko


---
