"""

## Zadanie 3: Analiza aktywności użytkowników (login / logout + czas)

Dane aktywności użytkowników zapisane są jako lista zdarzeń.
Każde zdarzenie zawiera:

* identyfikator użytkownika (`user_id`),
* typ zdarzenia (`"login"`, `"logout"`, `"purchase"`),
* czas zdarzenia (`time`) — liczba całkowita, rosnąca w skali całego systemu,
* kwotę (`amount`) — dla zdarzeń innych niż `"purchase"` zawsze `0`.

### Dane wejściowe

```python
events = [
    {"user_id": "u1", "type": "login",    "time": 1,  "amount": 0},
    {"user_id": "u1", "type": "purchase", "time": 5,  "amount": 120},
    {"user_id": "u1", "type": "logout",   "time": 10, "amount": 0},

    {"user_id": "u2", "type": "login",    "time": 12, "amount": 0},
    {"user_id": "u2", "type": "logout",   "time": 18, "amount": 0},

    {"user_id": "u3", "type": "login",    "time": 20, "amount": 0},
    {"user_id": "u3", "type": "purchase", "time": 25, "amount": 50},
    {"user_id": "u3", "type": "purchase", "time": 30, "amount": 75},
    {"user_id": "u3", "type": "logout",   "time": 40, "amount": 0},

    {"user_id": "u4", "type": "login",    "time": 45, "amount": 0},
    {"user_id": "u4", "type": "logout",   "time": 50, "amount": 0},
]
```

---

### Twoim zadaniem jest:

1. Zliczyć, ilu **unikalnych użytkowników** występuje w danych.
2. Obliczyć **łączną wartość zakupów** dla każdego użytkownika.
3. Obliczyć **łączny czas spędzony w systemie** przez każdego użytkownika
   (różnica `logout.time - login.time`).
4. Wypisać użytkowników, którzy:
   * wykonali co najmniej jeden `"login"`,
   * ale **nie wykonali żadnego `"purchase"`.
5. Wypisać użytkownika, który spędził **najwięcej czasu w systemie**.


"""
from collections import defaultdict

events = [
    {"user_id": "u1", "type": "login",    "time": 1,  "amount": 0},
    {"user_id": "u1", "type": "purchase", "time": 5,  "amount": 120},
    {"user_id": "u1", "type": "logout",   "time": 10, "amount": 0},

    {"user_id": "u2", "type": "login",    "time": 12, "amount": 0},
    {"user_id": "u2", "type": "logout",   "time": 18, "amount": 0},

    {"user_id": "u3", "type": "login",    "time": 20, "amount": 0},
    {"user_id": "u3", "type": "purchase", "time": 25, "amount": 50},
    {"user_id": "u3", "type": "purchase", "time": 30, "amount": 75},
    {"user_id": "u3", "type": "logout",   "time": 40, "amount": 0},

    {"user_id": "u4", "type": "login",    "time": 45, "amount": 0},
    {"user_id": "u4", "type": "logout",   "time": 50, "amount": 0},
]

# 1. ilu jest unikalnych użytkowników
users = {}
for event in events:
    user_id = event["user_id"]
    current_user = users.get(user_id ,0)
    users[user_id] = current_user + event["amount"] # przy okazji dodaję do słownika, łączną wartość zakupów dla danego użytkownika
print(f"There are {len(users)} unique users.\n")


# 2. Obliczyć łączną wartość zakupów dla każdego użytkownika
for user, total_amount in users.items():
    print(f"User {user} made purchases for a total value: {total_amount}.")


# 3. Obliczyć **łączny czas spędzony w systemie** przez każdego użytkownika (różnica `logout.time - login.time`)
spent_times = {}
login_times = {} # biblioteka tymczasowa

for event in events:
    user_id = event["user_id"]

    if event["type"] == "login":
        login_times[user_id] = event["time"]  # zapisujee czas logowania

    elif event["type"] == "logout":
        if user_id in login_times:
            duration = event["time"] - login_times[user_id] # obliczam duration czyli czas spędzony w systemie
            current_duration = spent_times.get(user_id, 0)
            spent_times[user_id] = current_duration + duration # dodaje duration do słownika
            del login_times[user_id]  # usuwam login ze słownika pomocniczego, bo sesja zakończona

for user, time in spent_times.items():
    print(f"Time spent in system by {user} is: {time}")


# 4. Wypisać użytkowników, którzy wykonali co najmniej jeden `"login"`, ale **nie wykonali żadnego `"purchase"`.
logins = defaultdict(int) # to słownik, który gdy odwołasz się do nieistniejącego klucza, sam utworzy ten klucz i ustawi jego wartość na 0 (bo int() → 0)
purchases = defaultdict(int) # czyli do porównania ze słownikiem z pkt 3 - tam jest więcej kodu - chodzi o część kodu z current_duration

for event in events:
    user_id = event["user_id"]
    event_type = event["type"]

    if event_type == "login":
        logins[user_id] = event["time"]
    elif event_type == "purchase":
        purchases[user_id] = event["time"]

print("Users without purchases:")
for user in logins:
    if purchases[user] == 0:
        print(f"User {user} has no purchases.")


# 5. Wypisać użytkownika, który spędził **najwięcej czasu w systemie**.
system_fan_user = max(spent_times, key=spent_times.get)
print(f"\n{system_fan_user} spent the most time in the system: {spent_times[system_fan_user]}")