#Máme funkci, která ze zadaného seznamu emailů vrátí ty, které obsahují zavináč. Co je potřeba doplnit na místo tří teček?
#vystup.append(data) - vypíšou se všechny email s @ i ten jeden bez
#vystup.append(radek) - vypíše se jen míša
#vystup = radek - vypíše se JEN míša bez hranatých závorek
#vystup = vystup + radek - hodí to type error
#print(radek)

def kontrola_emailu(data):
    vystup = []
    for radek in data:
        if "@" not in radek:
            vystup.append(radek)
    return vystup
    
emaily = ["misa@czechitas.cz",
          "kuba@czechitas.cz",
          "soustruh@czechitas.cz",
          "jirkaczechitas.cz"]
print(kontrola_emailu(emaily))  