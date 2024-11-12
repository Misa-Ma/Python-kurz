class Employee:
    def __init__(self, name, position, holiday_entlitlement):
        self.name = name
        self.position = position
        self.holiday_entlitlement = holiday_entlitlement
    def __str__(self):
        return f"{self.name} pracuje na pozici {self.position}."
    def take_holiday(self, days):
        if days <= self.holiday_entlitlement:
            self.holiday_entlitlement = self.holiday_entlitlement - days
            return "Užij si to"
        else:
            return "Na tolik dní nemáš nárok."
klara = Employee("Klára Nová", "konstruktérka", 35)
print(klara.take_holiday(25))
print(klara.take_holiday(15))
print(klara.holiday_entlitlement)
print(klara.__str__())