#Zad.4. Policz ile kilometrow przejechaly samochody:

koszyk = [
    {'samochod': 'kia', 'ilosc': 1, 'km': 23.5},
    {'samochod': 'porsche', 'ilosc': 3, 'km': 22.5},
    {'samochod': 'fiat126p', 'ilosc': 4, 'km': 31.5}
]

suma = 0
for poz in koszyk:
    il = poz['ilosc']
    km = poz['km']
    suma = suma + (km * il)
    # print(c)
    # print(suma)
    # print(poz)
print(suma)
