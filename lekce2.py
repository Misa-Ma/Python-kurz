#MODULY - jsou k programování základních funkcí, když si vytvořím modul - třeba math, tak si tam vytvořim funkci, která se nějak pojmenuje, a když někdo bude chtít svou math, tak si ji naprogramuje ve svém modulu, proto si nejdřív každý otevře ten modul a pak si tam funkci najde#
#Pokud byste pojmenovali svůj skript math.py, uvnitř napsali import math a používali nějakou funkci z tohoto modulu, Python ji bohužel nenajde.#
import math #když chci importovat ten modul, napíšu toto a když je to zašedlé, tak to znamená, že jsme ten modul math ještě nepoužili#
import statistics #pro přehlednost je dobré psát moduly nahoru, i když se ty moduly používají později#

#Zaokrouhlování nahoru#
vysledek = math.ceil(3.1)
#Zaokrouhlování dolů#
vysledek = math.floor(3.9)
print(vysledek)

prumer = statistics.mean([2,3,4,5]) #když dám F, tak se mi objeví vyhledávání, tak tam zadám toogle, a on zakomentářuje vše#
print (prumer)

#CVIČENÍ 1 - moduly - Přijímačky a moduly#CYKLY
school_report = [
    ["Český jazyk", 1],
    ["Anglický jazyk", 1],
    ["Matematika", 1],
    ["Přírodopis", 2],
    ["Dějepis", 1],
    ["Fyzika", 2],
    ["Hudební výchova", 4],
    ["Výtvarná výchova", 2],
    ["Tělesná výchova", 3],
    ["Chemie", 4],
] #mohli bychom si to naprogramovat, kde naprogramujem sečtení těch známek, ale když bude 20 vysvědčení, tak je dobrý si spočíst průměr známek, ale z určitých předmětů#
znamky = [] #do tohoto seznamu si budu postupně odkládat ty známky#
muj_prazdny_seznam = ["Český jazyk","Anglický jazyk","Matematika","Fyzika"]

for row in school_report:
    if row[0] in muj_prazdny_seznam: #při prvním běhu, tj od 1 předmětu ve school reportu (druhý běh je od angličtiny, třetí běh...atd, pokud ho tam nenajde python tak ho prostě nezobrazí) mi načte do proměnné "row" první dvojici takže název předmětu a známka, ty cykly jdou řádky po řádku
        #já chci uložit jen předměty v seznamu můj prázdný seznam - důležité předměty, podívej se, jestli je ten předmět v tom mém seznamu, tj. KDYŽ ten předmět v té ROW JE V SEZNAMU#
        znamky.append(row[1]) #apppend mi vloží na konec toho seznamu novou hodnotu, na pozici row 0 je český jazyk, na pozici row 1 je jednička,
print (znamky)
prumer = statistics.mean(znamky)
print(prumer)


#Uvažuj, že student se hlásí na školu, která vybírá studenty podle průměru. 
# Pro školu jsou ale důležité pouze předměty český jazyk, anglický jazyk, matematika a fyzika. 
# Vypočítej průměr studenta z daných předmětů s využitím modulu statistics. Na začátku vytvoř prázdný seznam a 
# následně pomocí cyklu vlož do nového seznamu známky ze čtyř vyjmenovaných předmětů.
# Nakonec použij metodu statistics.mean() k výpočtu průměru. Dále zkus využít funkce, které jsou zmíněné v textu, k výpočtu nejlepší a nejhorší známky z daných předmětů.#


# cvičení - Vánoční párty#
import statistics
votes = [
    "curling", 
    "vánoční svařák na trzích", 
    "vánoční svařák na trzích", 
    "curling", 
    "zážitková první pomoc",
    "curling", 
    "zážitková první pomoc",
    "curling",
    "zážitková první pomoc",
    ]
print (statistics.mode(votes))


# Ve statistice existuje ukazatel zvaný modus, který vrátí nejčastější hodnotu v datech. V modulu statistics existuje funkce mode(), která umí modus spočítat. 
# Funkce mode() má navíc vychytávku, umí pracovat i s řetězci.
#Uvažuj data v seznamu votes, což je hlasování zaměstnanců malé firmy o tom, jakou akci podniknou během jejich vánočního večírku. Použij funkce mode() ke zjištění, 
# pro jakou aktivitu hlasovalo nejvíce zaměstnanců. Funkce má jeden parametr - seznam, ze kterého má určit nejčastější prvek.#

#VLASTNÍ FUNKCE#
#funkci vytváříme neboli definujeme, takže použíjeme slovíčko k vytvoření funkce ,,def"#
def greet_user ():#def pak napíšu jak by se mohla fce jmenovat, bez mezer max využiju podtržítko, zde vytvářím fci pozdrav uživatele#
    print ("Ahojky")
greet_user() #musím napsat volání té fce, aby se to propsalo#
#můžem poslat takhle newsletter že je nové zboží, když si lidi koupí, tak chci poslat email s díky, nebo že je to na poště atd. Fce pošli email, kde bude shrnutí objednávky,
#nebo pošli email kde bude ten newsletter, nebo pošli email, že jsme naskladnili trička#
greet_user()

#funkce potřebuje přijímat nějaké vstupy, parametry, když budem mít fci na posílání emailu, potřebuje fci na ten text#

def greet_user (name):
    print (f"Ahojky{name}")
greet_user("Marťásku")
greet_user("Mikulášku")


#FUNKCE SUM TWO NUMBERS - sečtení dvou čísel
def sum_two_numbers (a,b):
    result = a+b #result je proměnná, která může existovat uvnitř fce, proměnná lze změnit tisíckrát, takže záleží na pořadí, jak jdou proměnné po sobě#
    return result #to co je napravo ode mě, vrať jako výsledek, jakmile napíšu return, tak ta fce skončí, return se v žádném jazyce nepoužívá s rovná se#
print (sum_two_numbers (3,4))


#CVIČENÍ 2 - Násobení
#Napiš funkci mult, která bude mít dva číselné parametry. Funkce oba parametry vynásobí a vrátí výsledek.

def mult (a,b):
    result = a*b
    return result
print (mult(3,4))


#CVIČENÍ 2 - Převody jednotek
#Převod kilometrů na míle a zpět

def prevod_km_mile (a):
    result = a
    return result
print (prevod_km_mile)

#Napište dvě funkce: kilometry_na_mile(kilometry) a mily_na_kilometry(mile), které provedou převod mezi kilometry a mílemi.
#Převod metrů na stopy a zpět

#Napište funkce: metry_na_stopy(metry) a stopy_na_metry(stopy), které umožňují převod mezi metry a stopami.
#Převod centimetrů na palce a zpět

#Vytvořte dvě funkce: centimetry_na_palec(centimetry) a palce_na_centimetry(palce), které umožní převod mezi centimetry a palci.

#Převod hmotnosti kilogramů na libry a zpět
#Napište funkce: kilogramy_na_libry(kilogramy) a libry_na_kilogramy(libry), které provedou převod mezi kilogramy a librami.

#Převod objemu litrů na galony a zpět
#Vytvořte dvě funkce: litry_na_galony(litry) a galony_na_litry(galony), které umožní převod mezi litry a galony.

#Převod rychlosti kilometrů za hodinu na míle za hodinu a zpět
#Napište funkce: kmh_na_mph(kmh) a mph_na_kmh(mph), které umožní převod rychlosti mezi kilometry za hodinu a míli za hodinu.

#Převod teploty ze stupňů Celsia na Fahrenheit a zpět
#Vytvořte dvě funkce: celsia_na_fahrenheit(teplota) a fahrenheit_na_celsia(teplota), které umožňují převod teploty mezi stupni Celsia a stupni Fahrenheit.#

#CVIČENÍ 2 - Rámeček
#Napiš funkci, která jako parametr převezme řetězec a vytiskne jej obalen hvězdičkami.

def ramecek(slovo):
    delka_slova = len(slovo)
    delka_radku = delka_slova + 4

    print(delka_radku * '*')
    print(f'* {slovo} *')
    print(delka_radku * '*')

def ramecek_2(slovo, znak):
    delka_slova = len(slovo)
    delka_radku = delka_slova + 4

    ramecek = delka_radku * znak
    slovo_s_rameckem = f"{ramecek}\n{znak} {slovo} {znak}\n{ramecek}"

    print(slovo_s_rameckem)

ramecek("ahoj")
ramecek_2("czechitas", "+")

#Zadej slovo: ahoj
#********
#* ahoj *
#********
#Nápověda: 8 * '*' == '********'

#Bonus: Znak, kterým se má text obalit, bude zadán také jako parametr.

#CVIČENÍ 2 - Měsíc narození
#Napiš funkci month_of_birth, která bude mít jeden parametr - rodné číslo. Funkce ze zadaného rodného čísla určí měsíc narození, 
# které vrátí jako výstup. Nezapomeň, že pro ženy je k měsíci připočtena hodnota 50.

#Příklad: Pro hodnotu 9207054439 vrátí 7. Pro hodnotu 9555125899 vrátí 5.


#Slovníky
item = {"title": "Čajová konvička s hrnky", "price": 899, "in_stock": True}
# Název předmětu je Čajová konvička s hrnky
# Funguje ve verzi 3.12
print(f"Název předmětu je {item["title"]}")
# Funguje od verze 3.6
print(f"Název předmětu je {item['title']}")
item["weight"] = 0.8
key = "price"
item[key] = 929
# Má item klíč weight?
if "weight" in item:
    print(item["weight"])
else:
    print("Hmotnost není udána")






