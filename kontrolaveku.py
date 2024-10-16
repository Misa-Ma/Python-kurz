kosik = [
    {"produkt":"jablka", "mnozstvi": 4, "kontrola_veku": False},
    {"produkt":"banány", "mnozstvi": 6, "kontrola_veku": False},
    {"produkt":"mléko", "mnozstvi": 2, "kontrola_veku": False},
    {"produkt":"víno", "mnozstvi": 1, "kontrola_veku": True},
    {"produkt":"chléb", "mnozstvi": 1, "kontrola_veku": False},
    {"produkt":"pivo", "mnozstvi": 3, "kontrola_veku": True},
]
kontrola_veku = 0
for polozka in kosik:
    if polozka ["kontrola_veku"] == True:
        kontrola_veku = kontrola_veku+1
print (kontrola_veku)   
  