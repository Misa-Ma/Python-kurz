#DATUM A ČAS:
#python pro to má modul datetime 07.11.2024 18:01
#timedelta - časový úsek - když si objednáme třeba jídlo tak uvidíme datum objednávky, a pak uvidíme za jak dlouho to jídlo dovezou = time delta, když vezmem datetime+timedelta=kdy jídlo dovezou
from datetime import datetime, timedelta
aktualni = datetime.now()
print (datetime.now())
apollo_start = datetime(1969,7,16,14,32)
print(apollo_start.weekday())
#když nedám čas, nastaví se mi dnešní půlnoc
#IZO formát/mezinárodní formát data je 2024-11-07 (výhoda pro řazení, od nejstaršího po nejmladší a dá se to použít ve všech programech)
print(aktualni.isoweekday()) #to počítá od nuly
#pozor američani začínají den od neděle, ale python jede podle eu, v javascriptu čísluje měsíce od 0

print(apollo_start) #když chci vypsat ten datum nebo:
print (apollo_start.isoformat())

#FORMÁTOVÁNÍ DATUMU A ČASU:
#%d	den
#%m	měsíc
#%Y	rok (nezkrácený)
#%H	hodina (rozsah 0-23)
#%M	minuta
#%S	sekunda
#from datetime import datetime, timedelta
#aktualni = datetime.now()
#apollo_start = datetime(1969,7,16,14,32)
#print(aktualni.strftime("%d. %m %Y, %H:%M")) #POZOR JE TO CITLIVÉ NA VELIKOST PÍSMEN, VELKÉ Y JE CELÝ ROK, VELKÉ M je minuta atd

#ČTENÍ DATA Z VÝSTUPU:
from datetime import datetime
aktualni = datetime.now()
print(aktualni.strftime("%d. %m %Y, %H:%M"))
apollo_start = datetime(1969, 7, 16, 14, 32)
apollo_pristani = datetime.strptime("21. 7. 1969, 18:54", "%d. %m. %Y, %H:%M")
delka_mise = apollo_pristani - apollo_start
print(delka_mise)


planovany_prijezd = datetime(2024, 3, 13, 19, 59)
zpozdeni = timedelta(minutes=10) 
skutecny_prijezd = planovany_prijezd + zpozdeni
print (skutecny_prijezd)

#BALÍČKY Z INTERNETU:
#když tvořím program, můžu vše naprogramovat sama a využívat python moduly, ale nejspíš budu řešit, co už někdo řešil, tak na to můžu využít nějaký balíček, co už někdo udělal
#instalace balíčků lze pomocí aplikace .pip
#do vyhledávače zadám: python exchange rate
#mezi prvníma bude nejspíš forex-python - čerpá kurzy z kurzu s měnami Forex
#stránka balíčku pro pip je: https://pypi.org/project/forex-python/ zde najdeme základní info o balíčku, co umí a využití
# pokud je zdrojový kód uložen na GitHubu, vidíme počet hvězdiček *, počet forků - počet lidí, kteří si vytvořili kopii repozitáře
# zdrojový kód balíčku forex-python můžem najít na GitHubu, obsahuje příklady, použití, dokumentaci: https://forex-python.readthedocs.io/en/latest/usage.html (podrobnější než na GitHubu)
# # Generování náhodného textu
#https://github.com/psf/black




