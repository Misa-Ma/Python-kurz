#SLOVNÍKY A CYKLY
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
#název té proměnné key si určuji sám, tím že si to dám mezi for a in, nejdřív tam vloží 1 klíč, pak 2, pak 3tí klíč, ten kód uvnitř cyklu se zopakuje 3x a pokaždé s jiným key
total_sales = 0 #chci abys prošel ty values a přišti nulu
for key, value in sales.items(): #tím item mu říkám, že chci přečíst i ty hodnoty k těm key, pokud dám for key, value in sales.item...a přehodila bych value a key, tak python nebude řešit název,a le po key dá hodnotu a pod value dá klíč
    print(f"Knihy {key} bylo prodáno {value} kusů.")
    total_sales = total_sales + value
print(f"Celkem bylo prodáno {total_sales} kusů.")   
     #pokud napíšu total_sales+=value je to stejné pokud bych tam měla jen total_sales=value, tak by mi to vypsalo pouze tu value
#print je tam pouze 1x, ale zapíše 3 proměnné, protože ten cyklus se opakuje (když reálně projdu seznam všech pacientů a každému zavolám, tak pokud dostanu tento pokyn, tak si to nenechám u každého pacienta takto zadat zvlášť)
# v javě se to píše print(sales[key]) - tento zápis není typický pro python, občas to takto vyhodí i chatGBT   
# 
# #DVOUROZMĚRNÉ TABULKY V PYTHONU
#máme klíč a hodnotu, 2 sloupečky, ale teď bychom mohli přidat další hodnoty, další sloupce, proto máme možnost využívat dvourozměrné struktury
#book = {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018} #k jedné knížce evidujeme více informací

#my si do jednoho seznamu můžeme vložit více knih:
books = [
    {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
    {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
    {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]
#cyklus funguje tak, že rozbalí tu nejvrchnější strukturu, vypíše ty celé slovníky a ne ty informace jednotlivě, to nechá na nás
#Chci celkové tržby v korunách
total_sales = 0
for item in books:
    total_sales=total_sales + item ["sold"] * item ["price"]
print (total_sales)

#prodeje za knížky za 2019
total_sales = 0
for item in books:
    if item ["year"] == 2019:
        total_sales=total_sales + item ["sold"] * item ["price"] #pokud máme podmínku if a cyklus, tak máme další odsazení, jinak nám to podtrhne
print (total_sales)

#Uvažujme vysvědčení, které máme zapsané jako slovník.
#Napiš program, který spočte průměrnou známku ze všech předmětů.
#Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1.
school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}

import statistics
total_znamky = school_report.values()
school_report.values()# tohle mi vyvolá, vytáhne ty hodnoty
for item in school_report.items():
     prumer = statistics.mean(value)
print (total_znamky)     


#Gustav je vášnivým čtenářem detektivek z našeho nakladatelství a navíc si zapisuje knihy, které přečetl. Níže ve slovníku vidíme, jaké informace si eviduje - název knihy, počet stran a hodnocení od 0 do 10.
#Napiš program, který spočte celkový počet stran, které Gustav přečetl.
#Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8.
books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

total_pages = 0
for item in books:
        total_pages = total_pages + item ["pages"]
print(f"Celkem bylo přečteno {total_pages} stran.")  


#V následujícím slovníků je evidence automobilů. Klíčem jsou státní poznávací značky (SPZ) a hodnotou je jméno majitele vozu. Napiš program, 
# který vypíše všechny majitele, jejichž vozidlo je registrováno v Plzeňském kraji, tj. na druhém místě (index 1!) řetězce v klíči je písmeno P.

plates = {"4A2 3000": "František Novák",
    "6P5 4747": "Jana Pilná",
    "3B7 3652": "Jaroslav Sečkár",
    "1P5 5269": "Marta Nováková",
    "37E 1252": "Martina Matušková",
    "2A5 2241": "Jan Král"}

#ÚVOD DO GITU version control system, verzovací systém, pokud bychom psali kód s více lidma, rozdělili bychom si úkoly (scram)
#existuje tzv. depozitář, kam se můžou posílat části kódů od různých lidí a kód se spojuje dohromady, občas se nějaké změny překrývají
#commit se používá a zadá za ten kód - initialize repository- má verzování a můžem tam něco napsat a označit to za commit

#Kviz 3:
#otázka 1
#obedy = {"Jirka":"salát", "Kuba": "nudle", "Míša": "nudle"}
#for key, value in obedy.items():
    #print (f"{key} měl (a) k obědu {value}.")
#komentář test 1