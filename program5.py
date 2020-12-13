#Zad.4. Policz ile kilometrow przejechaly samochody:

koszyk = [
    {'produkt': 'kia', 'ilosc': 1, 'km': 23.5},
    {'produkt': 'porsche', 'ilosc': 3, 'km': 22.5},
    {'produkt': 'fiat126p', 'ilosc': 4, 'km': 31.5}
]

suma = 0
for poz in koszyk:
    il = poz['ilosc']
    c = poz['km']
    suma = suma + (c * il)
    # print(c)
    # print(suma)
    # print(poz)
print(suma)
