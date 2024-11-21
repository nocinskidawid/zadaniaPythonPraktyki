lancuch = "Ala ma psa"

def liczZnaki(lancuch) -> dict:
    slownik = {}

    # Sprawdzanie wielkich liter
    for i in range(65, 91):  # Wielkie litery od 'A' do 'Z'
        znak = chr(i)
        liczba = lancuch.count(znak)
        if liczba != 0:
            slownik[znak] = liczba

    # Sprawdzanie małych liter
    for i in range(97, 123):  # Małe litery od 'a' do 'z'
        znak = chr(i)
        liczba = lancuch.count(znak)
        if liczba != 0:
            slownik[znak] = liczba

    return slownik

print(liczZnaki(lancuch))
