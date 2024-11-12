#Co je potřeba doplnit do programu,
pozice = {"Lenka": "testerka", "Lucka": "analyzička"}
if "Petra" in pozice:
    print (pozice ["Petra"])
else:
    print ("Petra v seznamu nemáme")      

#"Petra" == pozice
#pozice in "Petra"
#"Petra" in pozice - SPRÁVNÁ ODPOVĚĎ
#"Petra" > pozice
#"Petra" < pozice
#"Petra": pozice     
# 
# Jaký bude výsledek programu níže?
pozice = {"Lenka": "testerka", "Lucka": "analyzička"}
print (pozice ["Petra"])  

#Nevypíše nic a skončí
#Skončí chybou KeyError - SPRÁVNÁ ODPOVĚĎ
#Vypíše "None"
#Vypíše náhodný řetězec
#Požádá uživatele o zadání hodnoty v terminálu