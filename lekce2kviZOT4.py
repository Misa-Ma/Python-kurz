#Následující funkce má vrátit počet e-mailů, kde chybí zavináč. Co je pravda?
#Funkce funguje správně a vrátí číslo 1. - SPRÁVNÁ ODPOVĚĎ
#V podmínce má být pouze "in", nikoli "not in".
#V podmínce má být "in radek", nikoli "in data".
#Cyklus musí být uvnitř podmínky, nikoli obráceně.
#A konči řádků chybí středníky

def kontrola_emailu (data):
    chyby = 0
    for radek in data:
        if "@" not in radek:
            chyby = chyby + 1
    return chyby
emaily =  ["misa@czechitas.cz",
          "kuba@czechitas.cz",
          "soustruh@czechitas.cz",
          "jirkaczechitas.cz"]
print (kontrola_emailu(emaily))