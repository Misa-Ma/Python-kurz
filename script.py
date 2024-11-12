print("Hello world!")
jmena = ["Michal", "Jana", "Martina"]
teploty = [23.3, 21.2, 10, 14, 2, 3]
kniha = ["Kniha 1", 300, 500, True, True]

#VÝBĚR HODNOT, POČET HODNOT
print(jmena[1])
print(teploty[3:6])
print(teploty[2:])
print(teploty[:3])
print(len(kniha))
print(len("SuperTajneHeslo123"))



inzerat = "Na této pracovní pozici budete využívat Python a SQL"

if "SQL" in inzerat:
    print("SQL se v inzeratu nachazi")
else:
    print("SQL se v inzeratu nenachazi")


email = "michal.kuceraczechitas.cz"

if "@" not in email:
    print("spatny email")
else:
    print("spravny e-mail")

#CVIČENÍ 1
cisla = [1, 2, 3, 1, 2, 132, 123, 43, 55, 12, 2, 3, 4, 5, 12, 1435, 93]

print(min(cisla))
print(max(cisla))
print(sorted(cisla))
print(sum(cisla))


pohyby = [1200, -250, -800, 540, 721, -613, -222]
print(pohyby[2])
print(pohyby[2:])
print(len(pohyby))
print(max(pohyby))
print(min(pohyby))
print(max(pohyby), min(pohyby))
print(sum(pohyby))

seznam = [27, 8, 19, 88, 4, 10, 2024]
def prumer(seznam):
    return sum(seznam) / len(seznam)
print(prumer(seznam))

cisla = [27, 8, 19, 88, 4, 10, 2024]
def rozpeti(cisla):
    return max(cisla) - min(cisla)
print(rozpeti(cisla))

produkt = input("Zadej produkt: ")
produkt = produkt.lower() # VINO na vino

if produkt == "vino":
    print("vitej v kategorii vina")
elif produkt == "pivo":
    print("vitej v kategorii piva")
else:
    print("spatne zvolena hodnota")

#funkce STRIP
#pokud uživatel vyplní políčko a omylem napíše před nebo za mezeru navíc, tak se používá na to fce strip, která to podchytí, aby mu ten výraz uživateli fungoval i když tam omylem napíše tu mezeru
#strip umi odstranit i jine veci nez whitespaces, muzeme je dat do zavorek jako parametr :)

#SPLIT - rozdělení různými znaky
#velký datový textový řetězec a budem to chtít oddělit, tak použijem fci SPLIT

#JOIN - spojení různými symboly
#pokud chceme spojit řetězec, použijeme JOIN

#NAHRAZOVÁNÍ textu za jiný - REPLACE
#co hledám a čím to chci nahradit, 2 parametry a oddělím je čárkou

print("michal".upper())
print("JANA".lower())
print("$$$text$$$".strip("$").upper())
print("jana martina michal pavel".split(" "))
print("jana,martina,michal,pavel".split(","))

jmena = "jana,martina,michal,pavel".split(",")

print("$".join(jmena))
print(",".join(jmena))

text = "Jirka Pesik je nejhorsi lektor Pythonu"
new_text = text.replace("nejhorsi", "nejlepsi")

print(new_text)

#CVIČENÍ 2
#Uložte si do proměnné jmeno svoje jméno. Pomocí volání vhodných metod jej převeďte nejdříve na malá písmena a poté na velká písmena.

name = "Michaela"
print(name.upper())
print(name.lower())
#print(name.capitalize())

# Čísla jako text
#Mějme seznam celých čísel zadaných jako text

#hodnoty = ['12', '1', '7', '-11']
#Potřebujeme k třetímu číslu v seznamu přičíst 4, aby výsledek vypadal takto:

#int(hodnoty [2]) + 4) možná by to šlo i takto, převede se na to na číslo, k tomu číslu přičteme 4, a poté se to zase převede na string, tj. textový řetězec

hodnoty[2] = str(int(hodnoty[2])+4)
print (hodnoty)

#hodnoty = ['12', '1', '11', '-11']

#Čísla v textu
#Máme obdobné zadání jako v předchozím cvičení, avšak tentokrát máme čísla zadána nikoliv v seznamu, ale v řetězci oddělená mezerou:

#hodnoty = '12.1 1.68 7.45 -11.51'
#K poslednímu číslu v seznamu chceme přičíst 0.25 tak, aby výsledek vypadal takto

#hodnoty = '12.1 1.68 7.45 -11.26'
#Určitě se vám budou hodit metody split a join.

hodnoty = '12.1 1.68 7.45 -11.51'.split(' ')
hodnoty[3] = str(float(hodnoty[3])+0.25)
hodnoty = ' '.join(hodnoty)





