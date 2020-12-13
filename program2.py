# Napisz funkcje zmieniajaca klucz name na nazwa
#1 rozwiazanie
def print_dict(d):
    for key in samolot:
        print("{0}:{1}".format(key, d[key]))

if __name__ == "__main__":
    samolot = {'name': 'boeing',
        'przebieg': 1000,
        'type': 'pasazerski'}

new_key = 'nazwa'
old_key = 'name'
new_key2 = 'typ'
old_key2 = 'type'

samolot[new_key] = samolot.pop(old_key)
samolot[new_key2] = samolot.pop(old_key2)

print(samolot)

#2 rozwiazanie

def print_dict(d):
    for key in samolot:
        print("{0}:{1}".format(key, d[key]))

if __name__ == "__main__":
    samolot = {'name': 'boeing',
        'przebieg': 1000,
        'type': 'pasazerski'}

samolot['nazwa'] = samolot['name']
samolot.pop('name')
samolot['typ'] = samolot['type']
samolot.pop('type')

print_dict(samolot)
