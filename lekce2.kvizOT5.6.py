#Co platí o slovníku
#Jeho délka je 3 - SPRÁVNÁ ODPOVĚĎ
#Jeho délka je 2 (hodnota musí být unikátní, pro se uloží pouze dvojice "Míša": "nudle" a dvojice "Kuba": "nudle" se neuloží.
#Nejedná se o slovník, ale o seznam.
#V zápisu slovníku je syntaktická chyba.

obedy = {"Jirka": "salát" , "Kuba": "nudle" , "Míša": "nudle"}
novy_obedy = "Míša"
obedy[novy_obedy] = "řéiek"

print (obedy)


#Jak zjistíme, co měl k obědu Jirka?
#print(obedy[0])
#print(obedy["Jirka"]) - SPRÁVNÁ ODPOVĚĎ
#print("Jirka")
#print(obedy["salát"])