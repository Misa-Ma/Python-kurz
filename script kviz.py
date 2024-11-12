venecky = [1, 2, 4, 1, 6, 5, 1] 
print(venecky[1])
print (venecky[:3])


jen_cisla = "1ppp0"
print(jen_cisla.isdecimal())

filmy = ["Čtyři svatby a jeden Python",
         "Pán Pythonů: Návrat Soustruha",
         "Rychle a Python","Harry Potter a Kámen Pythonů",
         "Forrest Python"
        ]
cislo_filmu = int(input("Zadej číslo filmu:"))
if cislo_filmu < len(filmy):
    print (filmy[cislo_filmu])
else:
    print ("Tolik filmů nemáme")