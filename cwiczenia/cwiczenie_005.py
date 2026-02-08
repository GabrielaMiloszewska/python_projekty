"""
# Zadanie - funkcje - adv -
System naliczania prowizji sprzedażowych (wersja rozszerzona). Firma sprzedażowa wypłaca prowizje handlowcom. Prowizja zależy od:
* wartości sprzedaży,
* regionu sprzedaży,
* typu klienta,
* aktualnej polityki prowizyjnej (strategii),
* dodatkowych modyfikatorów (np. premie kwartalne).

System musi być: elastyczny (łatwa zmiana reguł), testowalny, otwarty na rozbudowę bez modyfikowania głównej logiki.

Zasady biznesowe:
1. Bazowa prowizja 5% od kwoty sprzedaży
2. Modyfikator regionu   EU → +1%    US → +2%    ASIA → +3%
3. Modyfikator typu klienta B2B → +2%    B2C → 0%
4. Premia za wysoką sprzedaż jeśli `amount > 100_000` → +1% (opcjonalny modyfikator)

---

### Wymagania techniczne
* zastosuj funkcje jako obiekty pierwszej klasy:
  * funkcje modyfikujące prowizję przekazywane jako argumenty,
* użyj:
  * parametrów pozycyjnych i nazwanych,
  * wartości domyślnych,
  * `*args` dla listy modyfikatorów,
* główna funkcja licząca prowizje nie może znać szczegółów reguł,
* wynik: łączna prowizja per sprzedawca.
"""
from collections import defaultdict

sales = [ # to jest lista
    {"seller": "Anna", "region": "EU", "client_type": "B2B", "amount": 120_000}, # to jest jeden słownik
    {"seller": "Anna", "region": "EU", "client_type": "B2C", "amount": 15_000},
    {"seller": "Anna", "region": "US", "client_type": "B2B", "amount": 90_000},

    {"seller": "Bartek", "region": "US", "client_type": "B2C", "amount": 8_000},
    {"seller": "Bartek", "region": "EU", "client_type": "B2C", "amount": 22_000},

    {"seller": "Celina", "region": "EU", "client_type": "B2B", "amount": 250_000},
    {"seller": "Celina", "region": "ASIA", "client_type": "B2B", "amount": 60_000},

    {"seller": "Daniel", "region": "ASIA", "client_type": "B2C", "amount": 12_000},
    {"seller": "Daniel", "region": "EU", "client_type": "B2C", "amount": 9_000},
]

def region_modifier(sale):
    if sale["region"] == "EU":
        return 0.01
    elif sale["region"] == "US":
        return 0.02
    elif sale["region"] == "ASIA":
        return 0.03
    return 0.0


def client_type_modifier(sale):
    if sale["client_type"] == "B2B":
        return 0.02
    return 0.0


def high_amount_bonus(sale, threshold=100_000):
    if sale["amount"] > threshold:
        return 0.01
    return 0.0


def calculate_commission(sale, base_rate=0.05, *modifiers): # *modifiers oznacza, że funkcja może przyjąć dowolną liczbę funkcji i zapisać je w krotce
    total_rate = base_rate # do sumy prowizji przypisuję najpierw prowizję bazową, czyli total_rate = 0.05

    for modifier in modifiers: # Iteruję po funkcjach, czyli najpierw region_modifier
        total_rate = total_rate + modifier(sale) # wywołuję pierwszą funkcję i jej wynik np. 0.01, dodaję do total_rate

    return sale["amount"] * total_rate # zwracam policzoną prowizję przez daną sprzedaź


def commission_per_seller(sales, base_rate=0.05, *modifiers): # wyliczam prowizję dla każdego z listy słowników
    result = defaultdict(float) # inicjuję słownik z automatycznie ustawioną wartością na 0.0

    for sale in sales: # iteruję po liście ze słownikami
        commission = calculate_commission( # wyliczam prowizję z jednej sprzedaży - dla jednego słownika
            sale,
            base_rate,
            *modifiers
        )
        result[sale["seller"]] = commission + commission # zaczynam od 0.0 i do danego sprzedawcy dodaję prowizje ze wszystkich jego sprzedaży

    return dict(result) # zwracam słownik "sprzedawca : wyliczona suma prowizji ze wszystkich sprzedaży z podanej listy słowników"


commissions = commission_per_seller( # dla listy ze słownikami, z bazą prowizją 5%, dodaję 3 reguły
    sales,
    0.05,
    region_modifier,
    client_type_modifier,
    high_amount_bonus
)

for seller, value in commissions.items():
    print(f"{seller}'s commision: {round(value, 2)}")
