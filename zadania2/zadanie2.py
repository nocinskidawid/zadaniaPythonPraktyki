def liczba_na_slowo(liczba: int) -> str:
    if liczba < 0 or liczba >= 1_000_000:
        raise ValueError("Liczba musi być z zakresu 0-999999")

    # Słowniki przechowujące nazwy liczb
    jednosci = {
        0: "zero", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery",
        5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem", 9: "dziewięć"
    }
    nascie = {
        10: "dziesięć", 11: "jedenaście", 12: "dwanaście", 13: "trzynaście",
        14: "czternaście", 15: "piętnaście", 16: "szesnaście",
        17: "siedemnaście", 18: "osiemnaście", 19: "dziewiętnaście"
    }
    dziesiatki = {
        2: "dwadzieścia", 3: "trzydzieści", 4: "czterdzieści",
        5: "pięćdziesiąt", 6: "sześćdziesiąt", 7: "siedemdziesiąt",
        8: "osiemdziesiąt", 9: "dziewięćdziesiąt"
    }
    setki = {
        1: "sto", 2: "dwieście", 3: "trzysta", 4: "czterysta",
        5: "pięćset", 6: "sześćset", 7: "siedemset",
        8: "osiemset", 9: "dziewięćset"
    }

    def liczba_do_999(liczba):
        """Konwertuje liczby od 0 do 999 na zapis słowny."""
        wynik = []
        if liczba >= 100:
            wynik.append(setki[liczba // 100])
            liczba %= 100
        if 10 <= liczba <= 19:
            wynik.append(nascie[liczba])
        else:
            if liczba >= 20:
                wynik.append(dziesiatki[liczba // 10])
                liczba %= 10
            if liczba > 0:
                wynik.append(jednosci[liczba])
        return " ".join(wynik) if wynik else "zero"

    # Obsługa zakresu 0 - 999999
    tysiac = liczba // 1000
    reszta = liczba % 1000

    slowa = []
    if tysiac > 0:
        if tysiac == 1:
            slowa.append("tysiąc")
        else:
            slowa.append(liczba_do_999(tysiac))
            slowa.append("tysiące" if 2 <= tysiac % 10 <= 4 and (tysiac % 100 < 10 or tysiac % 100 >= 20) else "tysięcy")
    if reszta > 0 or liczba == 0:
        slowa.append(liczba_do_999(reszta))

    return " ".join(slowa)


while True:
    liczba = input("podaj liczbe: ")

    if liczba == "q":
        break

    print(liczba_na_slowo(int(liczba)))