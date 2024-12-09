import requests
import json

ICO = input ("Prosím zadejte IČO hledaného subjektu:")

url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ICO}"

vystup = requests.get(url)

if vystup.status_code == 200:
    data = vystup.json()

    obchodni_jmeno = data.get ('obchodniJmeno', 'N/A')
    adresa = data.get ('sidlo',{}).get('textovaAdresa','N/A')

    print (obchodni_jmeno)
    print (adresa)

else:
    print ("Bohužel se nám nepodařilo získat data. Prosím, zkontrolujte zadané IČO a zkuste to znovu.")




import requests
import json

nazev_subjektu = input ("Prosím zadejte název hledaného subjektu:")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

data = json.dumps ({"obchodniJmeno":nazev_subjektu})

res = requests.post ("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data)

if res.status_code == 200:
    data = res.json()

    pocet_celkem = data.get('pocetCelkem', 0)
    print (f"Počet nalezených subjektů:{pocet_celkem}")

    subjekty = data.get('ekonomickeSubjekty', [])

    for subjekt in subjekty:
        obchodni_jmeno = subjekt.get('obchodniJmeno', 'N/A')
        ico = subjekt.get('ico', 'N/A')
        print(f"{obchodni_jmeno}, {ico}")

else:
    print (f"Bohužel se nám nepodařilo získat požadovaná data. Prosím, zkuste to znovu.")   


import requests
import json

def ziskani_pravni_forma(kod, polozky_ciselniku):
    for polozka in polozky_ciselniku:
        if polozka['kod'] == kod:
            return polozka ['nazev'] [0] ['nazev']
    return 'N/A'

nazev_subjektu = input ("Prosím, zadejte název subjektu, který hledáte:")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

data = '{"obchodniJmeno": "' + nazev_subjektu + '"}'
data = data.encode ("utf-8")

res = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data)

if res.status_code == 200:
    data = res.json()

    pocet_celkem = data.get('pocetCelkem', 0)
    print(f"Počet nalezených subjektů:{pocet_celkem}")

    subjekty = data.get ('ekonomickeSubjekty', [])

    ciselnik_data = json.dumps({"kodCiselniku": "PravniForma", "zdrojCiselniku": "res"})
    ciselnik_res = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ciselniky-nazevniky/vyhledat", headers=headers, data=ciselnik_data)

    if ciselnik_res.status_code == 200:
        ciselnik = ciselnik_res.json()
        polozky_ciselniku =ciselnik ['ciselniky'] [0] ['polozkyCiselniku']

        for subjekt in subjekty:
            obchodni_jmeno = subjekt.get ('obchodniJmeno', 'N/A')
            ico = subjekt.get ('ico', 'N/A')
            pravni_forma_kod = subjekt.get ('pravniForma', 'N/A')
            pravni_forma = ziskani_pravni_forma(pravni_forma_kod, polozky_ciselniku)
            print(f"{obchodni_jmeno},{ico}, {pravni_forma}")

    else:
        print("Bohužel se nám nepodařilo získat číselník právních forem.")

else:
    print("Bohužel se nám nepodařilo získat požadované informace. Prosím, zkuste to znovu.")


