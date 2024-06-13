# Aplikacja Blogowa - Rekrutacja Whitefly

## Opis
Projekt jest aplikacją blogową, umożliwiającą użytkownikom dodawanie wiadomości. Aplikacja oferuje dwa tryby dodawania treści: synchroniczny i asynchroniczny, co zapewnia różne opcje interakcji dla użytkowników.

## Funkcjonalności
- **Dodawanie Wiadomości Synchronicznie**: Umożliwia użytkownikowi dodanie wiadomości, która jest natychmiast przetwarzana i wyświetlana.
- **Dodawanie Wiadomości Asynchronicznie**: Użytkownik może dodać wiadomość bez przeładowywania strony, co zapewnia płynniejsze i szybsze działanie.
- **Przeglądanie Wiadomości**: Strona główna zawiera listę wszystkich dodanych wiadomości, które można przeglądać.
- **Usuwanie Wiadomości**: Użytkownicy mogą również usuwać swoje wiadomości.

## Technologie
- **Flask**: Aplikacja webowa stworzona w Flasku, który jest mikroframeworkiem w Pythonie.
- **HTML/CSS**: Struktura i stylowanie stron.
- **Bootstrap**: Framework CSS użyty do szybkiego tworzenia responsywnych layoutów.
- **Celery**:
- **Redis**:


## Uruchomienie lokalne
Aby uruchomić aplikację lokalnie:
1. Sklonuj repozytorium na swoje urządzenie.
2. Zainstaluj wymagane zależności: `pip install -r requirements.txt`
3. Uruchom serwer Flask: `flask run`

## Demo
Aplikacja jest dostępna online pod adresem [Rekrutacja Whitefly](http://161.35.202.8), gdzie można przetestować jej wszystkie funkcjonalności.

## Konfiguracja serwerowa i testy wydajności

Aplikacja jest zabezpieczona za pomocą konfiguracji proxy, co zapewnia dodatkową warstwę bezpieczeństwa i optymalizacji wydajności. Aby maksymalnie wykorzystać możliwości Flask, proponujemy użycie stacka `Flask + uWSGI + Nginx`:

1. **Flask**: Obsługuje logikę aplikacji.
2. **uWSGI**: Serwer aplikacji, który komunikuje się z Flaskiem i zarządza procesami.
3. **Nginx**: Serwer HTTP działający jako proxy dla uWSGI, oferujący lepsze zarządzanie statycznymi plikami i obciążeniem.

### Testy wydajności
Przed uruchomieniem aplikacji w środowisku produkcyjnym zalecamy przeprowadzenie testów wydajności, aby ocenić skalowalność i odporność aplikacji na wysokie obciążenie. Użyj narzędzi takich jak Apache Bench lub JMeter do symulacji ruchu sieciowego i zidentyfikuj potencjalne wąskie gardła.

---

# Aplikacja Blogowa - Rekrutacja Whitefly

## Opis
Projekt to nowoczesna aplikacja blogowa oparta na FastAPI, umożliwiająca użytkownikom dodawanie wiadomości synchronicznie oraz asynchronicznie za pomocą Celery i Redis jako backendu kolejki zadań. Zapewnia efektywne zarządzanie treścią poprzez interfejs API.

## Funkcjonalności
- **Dodawanie Wiadomości Synchronicznie**: Natychmiastowe przetwarzanie i wyświetlanie wiadomości.
- **Dodawanie Wiadomości Asynchronicznie**: Dodawanie wiadomości bez przeładowywania strony dzięki Celery i Redis.
- **Przeglądanie i Usuwanie Wiadomości**: Możliwość przeglądania wszystkich wiadomości oraz ich usuwania.

## Technologie
- **FastAPI**: Framework do tworzenia API z Pythona.
- **Celery**: System kolejkowania zadań do operacji asynchronicznych.
- **Redis**: Backend dla Celery do przechowywania stanu zadań.
- **SQLAlchemy**: ORM do operacji na bazie danych.
- **SQLite**: Baza danych do przechowywania wiadomości.

## Uruchomienie lokalne
1. Sklonuj repozytorium.
2. Zainstaluj wymagane zależności: `pip install -r requirements.txt`.
3. Uruchom aplikację: `uvicorn app.main:app --reload`.

## Konfiguracja serwerowa i testy wydajności
Zalecane użycie `FastAPI + Uvicorn + Gunicorn + Nginx`:
1. **Uvicorn**: ASGI serwer dla FastAPI.
2. **Gunicorn**: WSGI serwer jako manager dla Uvicorn.
3. **Nginx**: Serwer HTTP jako proxy do zarządzania ruchem sieciowym.

### Testy wydajności
Przeprowadź testy wydajności za pomocą Apache Bench lub JMeter.

## Demo
Aplikacja jest dostępna online [tutaj](http://161.35.202.8), gdzie można testować jej funkcjonalności.



Strona FastAPI - http://165.227.146.34
