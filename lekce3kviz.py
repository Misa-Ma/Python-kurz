hospoda_u_krajty = [
    {"nazev": "Smažený sýr", "nazev_en": "Fried Cheese", "cena": 220},
    {"nazev": "Hovězí guláš", "nazev_en": "Beef Gouhlash", "cena": 180},
    {"nazev": "Kuřecí řízek", "nazev_en":"Chicken Schnitzel", "cena":160},
    {"nazev": "Vepřo knedlo zelo", "nazev_en":"Pork with Dumpligs and Sauerkraut", "cena":190},
    {"nazev": "Bramborák", "nazev_en":"Potato Pancake", "cena":150},
    {"nazev": "Svíčková na smetaně", "nazev_en":"Sirloin in Cream Sauce", "cena":210}
]    

import statistics
ceny = []
for radek in hospoda_u_krajty:
    ceny.append (radek ["cena"])
print (statistics.mean(ceny))    
  

