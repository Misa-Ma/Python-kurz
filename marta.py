def kontrola_emailu(data):
    vystup = []  # Inicializujeme prázdný seznam pro výstup
    for radek in data:  # Procházíme každý řádek v datech
        if "kuba" in radek:  # Kontrolujeme, zda "kuba" je v aktuálním řádku
            vystup.append(radek)  # Přidáme aktuální řádek do výstupu
    return vystup  # Vrátíme seznam nalezených řádků

emaily = ["misa@czechitas.cz",
          "kuba@czechitas.cz",
          "soustruh@czechitas.cz",
          "jirkaczechitas.cz"]
print(kontrola_emailu(emaily))  # Vytiskneme výsledek funkce