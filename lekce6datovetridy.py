#DATOVÉ TŘÍDY - obsah metody __init__ je příklad boilerplate code (odkazuje na štítky na bojleru), ten štítek je všude stejný, ten kód je dlouhej, ve kterém není moc zajímavého,
#je to hlavně to, co píšeme do toho init

#from dataclasses import dataclass - v datových třídách se moc ta dědičnost nepoužívá, pokud ji tam přidám

from dataclasses import dataclass
@dataclass
class Employee:
    name: str
    position: str
    holiday_entitlement: int = 25 #jakmile začnu s výchozí hodnotou, tak nemůžu používat něco kde výchozí hodnota není určena, leda bych napsala holiday_entitlement: int

    def take_holiday(self, days):
        if self.holiday_entitlement >= days:
            self.holiday_entitlement -= days
            return f"Užij si to."
        else:
            return f"Bohužel už máš nárok jen na {self.holiday_entitlement} dní."

    def __str__(self):
        return f"{self.name} pracuje na pozici {self.position}."
    
#@dataclass
# class Manager(Employee):
# car: str = ''
# frantisek = Manager ("František Novák", "konstruktér", 25,'Škoda Octavia')
# print(frantisek.car)

frantisek = Employee("František Novák", "konstruktér")
print (frantisek)