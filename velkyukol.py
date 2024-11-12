from abc import ABC, abstractmethod
from math import ceil
from enum import Enum

class EstateType (Enum):
    zemedelsky_pozemek = "zemědělský pozemek"
    stavebni_pozemek = "stavební pozemek"
    les = "les"
    zahrada = "zahrada"

estate_type_coefficients = {
    EstateType.zemedelsky_pozemek:0.85, 
    EstateType.stavebni_pozemek:9,
    EstateType.les:0.35,
    EstateType.zahrada:2}  

class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

class Property(ABC):
    def __init__(self, locality):
        self.locality = locality

    @abstractmethod
    def calculate_tax(self):
        pass   

class Estate (Property):
    def __init__(self, locality, estate_type, area):
        super().__init__(locality) 
        if not isinstance(estate_type,EstateType):
            raise ValueError("Neexistující typ pozemku")
        self.estate_type = estate_type
        self.area = area

    def calculate_tax(self):
        estate_coefficient = estate_type_coefficients[self.estate_type]
        tax = self.area * estate_coefficient * self.locality.locality_coefficient
        zaokrouhlena_dan = ceil(tax)
        return zaokrouhlena_dan
    
    def __str__(self):
        tax = self.calculate_tax()
        return f"Typ pozemku je: {self.estate_type.value.capitalize()}, lokalita {self.locality.name} (koeficient {self.locality.locality_coefficient}), {self.area} metrů čtverečných, daň {tax} Kč."
        
class Residence(Property):
    def __init__(self, locality, area, commercial):
        super().__init__(locality)    
        self.area = area
        self.commercial = commercial

    def calculate_tax(self):
        tax = self.area * self.locality.locality_coefficient *15
        if self.commercial:
            tax *= 2
        zaokrouhlena_dan = ceil(tax)
        return zaokrouhlena_dan
    
    def __str__(self):
        tax = self.calculate_tax()
        property_type = "komerční prostory" if self.commercial else "rezidenční prostory"
        return f"Typ pozemku je:{property_type.capitalize()}, lokalita {self.locality.name} (koeficient {self.locality.locality_coefficient}), {self.area} metrů čtverečných, daň {tax} Kč."

class TaxReport:
    def __init__(self,name):
        self.name = name
        self.property_list = []

    def add_property(self, property):
        self.property_list.append(property)

    def calculate_tax(self):
        total_tax = sum(property.calculate_tax() for property in self.property_list)  
        return f"Celková daň pro {self.name} činí {total_tax} Kč."  


locality0 = Locality ('Hradec Králové', 2)
locality1 = Locality ('Manětín', 0.8)
locality2 = Locality ('Brno', 3)   

estate0 = Estate(locality0, EstateType.les, 500)
print (estate0)

estate1 = Estate(locality1, EstateType.zemedelsky_pozemek, 900)
print (estate1)

rezidence1 = Residence (locality1,120,False)
print (rezidence1)

rezidence2 = Residence(locality2,90,True)
print (rezidence2)

tax_report = TaxReport ("Michaela Macháčková")
tax_report.add_property(estate0)
tax_report.add_property(estate1)
tax_report.add_property(rezidence1)
tax_report.add_property(rezidence2)

print (tax_report.calculate_tax())


