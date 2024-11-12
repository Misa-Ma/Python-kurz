#V reálných aplikacích často potřebujeme objekty mezi sebou provázat. V našem personálním systému by bylo užitečné provázat podřízené s jejich manažerem. 
# To by usnadnilo některé procesy, například vytváření pracovní smlouvy a jejích dodatků, usnadní plánování meetingů atd. 
# Nejprve přidejme třídě Employee atribut manager a nastavme ho v metodě __init__.
#Manažera pak můžeme přidat do výpisu, který poskytuje metoda __str__().

class Employee:
    def __init__(self, name, position, holiday_entitlement, manager):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
        self.manager = manager
    def __str__(self):
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}. Nadřízeným je {self.manager.name}." #když sem přidám větu se self.manager.name, tak to vyjede po třetí stejné
class Manager(Employee):
    def __init__(self, name, position, holiday_entitlement, manager, subordinates, car):
        super().__init__(name, position, holiday_entitlement, manager)
        self.subordinates = subordinates
        self.car = car
    def __str__(self):
        return super().__str__() + f" Má {self.subordinates} podřízených."
marian = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, None, 2, "Škoda Octavia")
klara = Employee("Klára Nová", "konstruktérka", 25, marian)   
#Chci zjistit manažera Kláry - nejdřív chci zjistit navázaný objekt Manager, a pak jeho jméno Name
print(klara.manager.name) #odkáže na managera kláry
print(marian.name) #odkáže na managera kláry
print(klara) #přidáním věty se self.manager.name do str
