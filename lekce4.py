#OBJEKTOVĚ ORIENTOVANÉ PROGRAMOVÁNÍ - budem je měnit jen na 1 místě. Kód který už máme a jen ho potřebujeme pozměnit, abychom ho využili na něco jiného a nepsali ho celý znovu.
#začnu tim, že si vytvořim třídu - class, využívají se třídy a objekty, např formulář - předvyplněné kolonky, třída je struktura s daty např ten formulář.
#Ve chvíli, kdy ten formulář vyplním, tak to jsou ty hodnoty vložené, data - neboli objekty.
#Typický je, že máme objekty na sobě nezávislé v jedné třídě. 2 formuláře, ale vyplněné různými jmény, adresou atd.

class Employee: #vytvořím si třídu
    def __init__(self, name, position, holiday_entlitlement): #podtržítkem začínají metody co mají speciální význam - magic method, __init__ je speciální v tom, že se volá sama narozdíl od get_info
        self.name = name #uložení hodnoty name do atributu self.name (v jave se používá this.name)
        self.position = position
        self.holiday_entlitlement = holiday_entlitlement
    def __str__(self):   
    #def get_info(self): #metoda init má všechny třídy, ale get info je námi vytvořená třída. Nezáleží na tom, v jakém pořadí píšu ty metody, jestli začnu init nebo ne
        return f"{self.name} pracuje na pozici {self.position}" #pokud bych tam nenapsala self.name, ale jen name tak to hodí chybu, ono to umí pracovat jen s atributem,tj. s tím self.něco
    def take_holiday(self,days):
        if days <= self.holiday_entlitlement:
            self.holiday_entlitlement = self.holiday_entlitlement - days
            return "Užij si to"
        else:
            return "Na tolik dní nemáš nárok kočičko"
#frantisek = Employee("František Novák", "konstruktér", 25)               
klara = Employee("Klára Nová", "konstruktérka", 35)     
print(klara.take_holiday(25))
print(klara.take_holiday(15)) #KLÁRA SI VZALA VÍC NEŽ MOHLA, TAK PŘIDÁME PODMÍNKU, ZDA TEN ČLOVĚK MÁ NA TO NÁROK VZÍT SI TO
#print(klara.get_info())#když tu metodu get_info chci zavolat, musím tam dopsat prázdné závorky, jinak ji to nezavolá
print(klara.holiday_entlitlement)
    
# teď musim vytvořit metodu, kdyby tam nebyla, tak by to bylo vlastně jako slovník. Vytvořím si metodu, která nám umožní s těmi objekty pracovat, 
#skoro jako fci. stejně jako u fce začínám def. využiju fci init a do závorek dám s čím má pracovat, u fcí jsme to nepsali, nepotřebují to, ale u metody to píšeme.
#v jave se self psát nemusí, ale python to vyžaduje, v jave se asi píše něco jiného. Nevíme proč to python chce.
#píšu dál dovnitř té metody, napíšu něco co mi umožní uložit věci natrvalo
#můžeme nastavit atribut objektu, ten bude existovat pořád a můžeme ho používat ve více metodách např name, atribut self.name
#potřebuji uložit hodnoty parametru name do atributu name - chci udělat to aby atribut name = parametru name
#název třídy, tam se používá CamelCase bez mezer, velká první písmeno, kdežto u objektů se píše snake_case, malými viz výše: Employee je třída, frantisek je objekt,
#do objektu si můžu uložit klasický seznam, jako jsme měli v předchozích lekcích


#CVIČENÍ 1 - BALÍK
#Uvažuj, že navrhuješ software pro zásilkovou společnost.
#Vytvoř třídu Package, která bude mít tři atributy - address, weight a state. Vytvoř metodu __init__, která uloží hodnoty parametrů metody do atributů.
#Přidej metodu get_info(), která vrátí informace o balíku jako řetězec. Uvažuj například větu "Balík na adresu Václavské Náměstí 12,
#Praha má hmotnost 0.25 kg je ve stavu nedoručen".
#Zkus si vytvořit alespoň dva objekty ze třídy Balik. U address uvažujeme typ řetězec (str), u weight desetinné číslo. 
#U atributu state zadávej pro zjednodušení pouze dva stavy: doručen a nedoručen.
#Vypiš informace, které generuje metoda get_info(), na obrazovku, a ověř, že je vše v pořádku.
#Vytvoř metodu delivery_price(), která vypočítá cenu přepravy balíku. Cena přepravy je daná hmotností balíku. 
# Cena přepravy balíku do 10 kg je 129 Kč, cena přepravy balíku od 10 kg do 20 kg je 159 Kč a cena přepravy balíků těžších než 20 kg je 359 Kč. 
#Metoda spočítá cenu a vrátí ji jako číslo.

class Package: 
    def __init__(self, address, weight, state): 
        self.address = address
        self.weight = weight
        self.state = state
    def get_info(self): 
        return f"Balík na adresu {self.address} má hmotnost {self.weight} je ve stavu {self.state}" 
    def delivery_price(self):
        if self.weight <10:
            price = 129
        elif self.weight < 20:
            price = 159
        else:
            price = 359    
        return f"Cena balíku je {price} Kč"      
    def delivery_state(self):
        return info
balik1 = Package ("Václavské náměstí 12", 0.25, "nedoručen")               
balik2= Package ("Petra Jilemnického 382", 11, "doručen")   
balik3 = Package ("Gebauerova 1422", 22, "doručen")
print(balik1.get_info())
print(balik2.get_info())
print(balik3.get_info())

#CVIČENÍ 2 - KNIHA
#Zkus pro nakladatelství vytvořit software s využitím tříd a objektů. Vytvoř tedy třídu Book, která reprezentuje knihu. 
# Každá kniha bude mít atributy title, pages a price. Hodnoty nastav ve funkci __init__.
#Přidej knize funkci get_info(), která vypíše informace o knize v nějakém pěkném formátu.
#Přidej metodu get_time_to_read(). Metoda vrátí čas potřebný na přečtení knihy v hodinách. 
# S využitím atributu pages vypočítej čas na přečtení knihy. Metoda bude mít nepovinný parametr, který udává počet minut potřebných pro přečtení jedné stránky knihy. 
# Dobu potřebnou na přečtení knihy získáš jako násobek doby potřebné na přečtení jedné stránky knihy a počet stránek knihy. Výchozí hodnota nepovinného parametru je 4.

#CVIČENÍ 3 - BALÍK PODRUHÉ
#Vrať se k návrhu software pro zásilkovou společnost.
#U třídy Package přejmenuj metodu get_info() na __str__() a vyzkoušej, jestli nyní stačí k získání informací o balíku funkce print().
#Přidej metodu deliver(). Půjde o obdobu tlačítka, které řidič nebo řidička zmáčkne při doručení balíku a zaznamená tak jeho doručení. 
# Metoda nejprve zkontroluje, zda balík náhodou již není ve stavu doručen. Pokud ano, metoda vrátí zprávu "Balík již byl doručen". 
# Tím bude řidič (řidička) informován(a) o tom, že se pravděpodobně spletl(a) a snaží se zaznamenat doručení u špatného balíku. Pokud balík není ve stavu doručen, 
# změň jeho stav právě na doručen a vrať zprávu "Doručení uloženo".
#Vyzkoušej metodu deliver(). Co se stane, pokud ji u jednoho balíku zavoláš dvakrát?

class Package: 
    def __init__(self, address, weight, state) -> None: 
        self.address = address
        self.weight = weight
        self.state = state

    def get_info(self) -> str: 
        info = f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}" 
        return info

    def delivery_price(self) -> int:
        if self.weight <10:
            price = 129
        elif self.weight < 20:
            price = 159
        else:
            price = 359        
        return price    
    
balik1 = Package ("Václavské náměstí 12", "0.25 kg", "nedoručen")               
balik2= Package ("Petra Jilemnického 382", "11 kg", "doručen")   
balik3 = Package ("Gebauerova 1422", "22 kg", "doručen")
print(balik1.get_info())
print(balik2.get_info())
print(balik3.get_info())