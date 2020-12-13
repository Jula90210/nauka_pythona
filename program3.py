#zad.2. Uzupelnij funckje liczaca VAT
def calculate_vat(netto):
    return (netto * 23)/100

if __name__ == "__main__":
    vat = calculate_vat(1000)
    print("{0}".format(vat))
