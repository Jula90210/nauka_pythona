#Zad.5.

koszyk = [
    {'produkt': 'mleko', 'ilosc': 1, 'cena': 1.5, 'alergeny': 'kazeina'},
    {'produkt': 'czekolada', 'ilosc': 2, 'cena': 2.5, 'alergeny': 'bialko'},
    {'produkt': 'bulka', 'ilosc': 4, 'cena': 3.5, 'alergeny': 'gluten'}
]


p = koszyk [2]
alergen = p['alergeny']

if 'kazeina' == alergen:
    print('Nie kupuj!')
elif 'bialko' in alergen:
    print('Nie dotykaj!')
elif 'gluten' in alergen:
    print('Nie bierz!')
else:
    print('Mozesz kupic')


#suma = 0
#for poz in koszyk:
    #il = poz['ilosc']
    #c = poz['cena']
    #suma = suma + (c * il)
    # print(c)
    # print(suma)
    # print(poz)
#print(suma)
