#OBJEKTOVĚ ORIENTOVANÉ PROGRAMOVÁNÍ 2 Dědičnost
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
#vytvořim novou třídu a do závorky dám třídu, která je jako mateřská, ta původní        
class Manager(Employee):
    def __init__(self, name, position, holiday_entlitlement, subordinates):
        super().__init__(name, position, holiday_entlitlement)
        self.subordinates = subordinates
class TopManager(Manager):
    def __init__(self, name, position, holiday_entlitlement, subordinates, car):
        super().__init__(name, position, holiday_entlitlement, subordinates)
        self.car = car
    def take_holiday(self, days):
        return "Užij si to."
    def __str__(self):
        return super().__str__() + f" Má {self.subordinates} podřízené."
frantisek = Employee("František Novák", "konstruktér", 25)
klara = Employee("Klára Nová", "konstruktérka", 35)
marian = TopManager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, 2, "Peugeot 403")
print(marian)