"""
## Zadanie 2: Analiza danych sprzedażowych

Dane sprzedażowe zapisane są jako lista słowników. Każdy element zawiera:

* nazwę produktu,
* kategorię produktu,
* liczbę sprzedanych sztuk.

```python
sales = [
    {"product": "Laptop", "category": "Electronics", "quantity": 15},
    {"product": "Mouse", "category": "Electronics", "quantity": 120},
    {"product": "Keyboard", "category": "Electronics", "quantity": 85},
    {"product": "Monitor", "category": "Electronics", "quantity": 0},

    {"product": "Desk", "category": "Furniture", "quantity": 20},
    {"product": "Chair", "category": "Furniture", "quantity": 55},
    {"product": "Lamp", "category": "Furniture", "quantity": 35},

    {"product": "Notebook", "category": "Office", "quantity": 200},
    {"product": "Pen", "category": "Office", "quantity": 350},
    {"product": "Stapler", "category": "Office", "quantity": 40},
]
```

### Twoim zadaniem jest:

1. Obliczyć łączną sprzedaż (sumę `quantity`) dla każdej kategorii.
2. Wypisać kategorię, która ma **najwyższą łączną sprzedaż**.
3. Wypisać wszystkie produkty, których sprzedaż jest **większa niż średnia sprzedaż w ich kategorii**.
4. Sprawdzić, czy istnieją produkty, których sprzedaż wynosi `0`, i wypisać ich nazwy (lub informację, że takich produktów nie ma).


"""

sales = [
    {"product": "Laptop", "category": "Electronics", "quantity": 15},
    {"product": "Mouse", "category": "Electronics", "quantity": 120},
    {"product": "Keyboard", "category": "Electronics", "quantity": 85},
    {"product": "Monitor", "category": "Electronics", "quantity": 0},
    {"product": "Desk", "category": "Furniture", "quantity": 20},
    {"product": "Chair", "category": "Furniture", "quantity": 55},
    {"product": "Lamp", "category": "Furniture", "quantity": 35},
    {"product": "Notebook", "category": "Office", "quantity": 200},
    {"product": "Pen", "category": "Office", "quantity": 350},
    {"product": "Stapler", "category": "Office", "quantity": 40},
]

# 1. łączna sprzedaż dla każdej kategorii
new_dict = {} # tworzę pusty słownik, który będzie przechowywał sumy sprzedaży (quantity) dla każdej kategorii. Kluczem będzie nazwa kategorii ("Electronics", "Furniture", "Office"); Wartością będzie łączna sprzedaż w tej kategorii
for sale in sales:
    category = sale["category"] # pobieram nazwę kategorii w obecnym przebiegu
    current_total = new_dict.get(category, 0) # dict.get(key, default) sprawdza, czy klucz istnieje w słowniku:
                                                                                    # Jeśli istnieje → zwraca jego wartość
                                                                                    # Jeśli nie istnieje → zwraca wartość domyślną, tutaj 0
    new_dict[category] = current_total + sale["quantity"] # w nowym słowniku zapisuję wartość sprzedaży dla danej kategorii

for category, total in new_dict.items(): # .items() zwraca wszystkie pary klucz–wartość ze słownika, dzięki czemu od razu mogę dostać klucz i wartość w jednej iteracji
                                         # .keys() ➡ zwraca tylko klucze: for key in category_totals.keys(): print(key)
                                         # .values() ➡ zwraca tylko wartości: for value in category_totals.values(): print(value)
    print(f"Total sales in {category} category: {total}")


# 2. wypisać kategorię, która ma najwyższą łączna sprzedać
best_sale_category = max(new_dict, key=new_dict.get)
print(f"\nBest sale category: {best_sale_category}, with sales: {new_dict[best_sale_category]}")


# 3. produkty, których sprzedaż jest większa niż średnia sprzedaż w ich kategorii
category_counts = {} # tworzę słownik, którego key jest nazwa kategorii, a value ilość produktów w danej kategorii
for sale in sales:
    category = sale["category"]
    current_count = category_counts.get(category, 0)
    category_counts[category] = current_count + 1

category_averages = {} # tworzę słownik, którego key jest nazwa kategorii, a value średnia sprzedaż w tej kategorii
for cat in new_dict:
    average = new_dict[cat] / category_counts[cat]
    category_averages[cat] = average

print("\nProducts with sales higher than the average in their category:")
for sale in sales:
    if sale["quantity"] > category_averages[sale["category"]]:
        print(f"{sale['product']} ({sale['category']}) - {sale['quantity']}")


# 4. czy istnieją produkty ze sprzedażą 0
zero_sales = [sale["product"] for sale in sales if sale["quantity"] == 0]

if zero_sales:
    for product in zero_sales:
        print(f"\nProducts with sales 0: {product}")
else:
    print("\nNo products with sales 0.")