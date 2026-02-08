from random import random, randint


class Postac:

    def __init__(self, imie, atak, zdrowie):
        self.imie = imie
        self._atak = atak
        self.zdrowie = zdrowie
        self.max_zdrowie = zdrowie
        self.ekwipunek = []
        self.pozycja = None

    def otrzymaj_obrazenia(self, ilosc):
        self.zdrowie -= ilosc
        if self.zdrowie < 0:
            self.zdrowie = 0

    def czy_zyje(self):
        return self.zdrowie > 0

    def wylecz(self):
        if self.czy_zyje():
            self.zdrowie = self.max_zdrowie

    def daj_przedmiot(self, przedmiot):
        self.ekwipunek.append(przedmiot)

    def zabierz_przedmiot(self, przedmiot):
        if przedmiot in self.ekwipunek:
            self.ekwipunek.remove(przedmiot)

    @property
    def moc_ataku(self):
        """bazowa moc ataku postaci wyrazona jako liczba całkowita"""
        return int(self._atak * random())

    @property
    def atak(self):
        return self.moc_ataku + sum(p.bonus_ataku for p in self.ekwipunek)

    def __str__(self):
        if not self.czy_zyje():
            return f"Jestem {self.imie}, miałem {self.max_zdrowie} i nie żyję."

        result = f"Jestem {self.imie}, mam {self._atak} ataku i {self.zdrowie}/{self.max_zdrowie} życia."

        if self.pozycja:
            result += f"\nPozycja: {self.pozycja}"

        if self.ekwipunek:
            result += "\nEKWIPUNEK:\n"
            for przedmiot in self.ekwipunek:
                result += f"{przedmiot}\n"
        return result


class Przedmiot:
    def __init__(self, nazwa, bonus_ataku):
        self.nazwa = nazwa
        self.bonus_ataku = bonus_ataku

    def __str__(self):
        return f"{self.nazwa}, {self.bonus_ataku} do ataku"


def _cios(p1, p2):
    if p2.czy_zyje() and p1.czy_zyje():
        moc_ataku_p1 = p1.atak
        print(f"{p1.imie} uderza {p2.imie} za {moc_ataku_p1} obrażeń.")
        p2.otrzymaj_obrazenia(moc_ataku_p1)
        print(f"{p2.imie} oberwał za {moc_ataku_p1} obrażeń.")
    else:
        print("KONIEC WALKI")
        print(p1)
        print(p2)


def _runda(p1, p2):
    print(p1)
    print()
    print(p2)
    _cios(p1, p2)
    _cios(p2, p1)


def walka(p1: Postac, p2: Postac):
    while p1.czy_zyje() and p2.czy_zyje():
        _runda(p1, p2)

# ----------------- SZUKANIE SKARBU -----------------

def losuj_pole():
    return (randint(1, 10), randint(1, 10))


def odleglosc(pozycja_gracza, pozycja_skarbu):
    return abs(pozycja_gracza[0] - pozycja_skarbu[0]) + abs(pozycja_gracza[1] - pozycja_skarbu[1])


def podpowiedz(dist):
    if dist == 0:
        return
    elif dist <= 3:
        print("🔥 Bardzo blisko skarbu!")
    elif dist <= 6:
        print("🙂 Blisko skarbu...")
    else:
        print("🥶 Daleko od skarbu...")


def ruch_gracza(p: Postac):
    print(f"\nTura gracza: {p.imie}")

    while True:
        try:
            x = int(input("Podaj X (z zakresu 1-10): "))
            if 1 <= x <= 10:
                break
        except ValueError:
            pass
        print("Błędna wartość, powinna być z zakresu 1-10.")

    while True:
        try:
            y = int(input("Podaj Y (z zakresu 1-10): "))
            if 1 <= y <= 10:
                break
        except ValueError:
            pass
        print("Błędna wartość, powinna być z zakresu 1-10.")

    p.pozycja = (x, y)


def sprawdz_skarb(p: Postac, skarb):
    d = odleglosc(p.pozycja, skarb)
    podpowiedz(d)
    return d == 0


def spotkanie(p1, p2):
    return p1.pozycja == p2.pozycja


def gra(p1, p2):
    skarb = losuj_pole()
    print("Skarb został ukryty!")

    while True:
        ruch_gracza(p1)

        if sprawdz_skarb(p1, skarb):
            print(f"{p1.imie} znalazł skarb!")
            break

        if spotkanie(p1, p2):
            walka(p1, p2)
            break

        ruch_gracza(p2)

        if sprawdz_skarb(p2, skarb):
            print(f"{p2.imie} znalazł skarb!")
            break

        if spotkanie(p1, p2):
            walka(p1, p2)
            break


# ----------------- START GRY -----------------

def main():
    p1 = Postac("Gracz 1", 20, 100)
    p2 = Postac("Gracz 2", 20, 100)

    gra(p1, p2)


if __name__ == "__main__":
        main()