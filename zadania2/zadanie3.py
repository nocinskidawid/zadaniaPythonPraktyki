def wyswietlanie():
    fiszki = {}
    try:
        with open("fiszki.txt", "r") as plik:
            for linia in plik:
                linia = linia.strip()

        print("Zawartość słownika fiszki:")
        for klucz, wartosc in fiszki.items():
            print(f"{klucz} -> {wartosc}")
    except FileNotFoundError:
        print("Plik fiszki.txt nie został znaleziony.")

def dodawanie():
    pass

def pytanie():
    pass



print("Dodawanie fiszek - d \n pytanie - p \n wyswietlanie - w ")
coRobic = input(":")

if coRobic == "d":
    dodawanie()
elif coRobic == "p":
    pytanie()
elif coRobic == "w":
    wyswietlanie()