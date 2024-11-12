class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state
        
    #def get_info(self):   
     #   price = self.delivery_price()
      #  return f"Balík na adresu {self.address}, má hmotnost {self.weight}, kg, a je ve stavu {self.state}, cena balíku činí {price} Kč."
    
    def delivery_price(self):
        if self.weight < 10:
            price = 129
        elif self.weight <= 20:
            price = 159
        elif self.weight >20:
            price = 359
                    
        return price
    
    def __str__(self):
        price = self.delivery_price()
        return f"Balík na adresu {self.address}, má hmotnost {self.weight} kg, je ve stavu {self.state}, cena balíku činí {price} Kč."
    
class ValuablePackage(Package):  

    def __init__(self, address, weight, state, value=0):
        super().__init__(address, weight, state)
        self.value = value

    def valuable_delivery_price(self):
        if self.weight < 10:
            base_price = 149
        elif self.weight <= 20:
            base_price = 179
        elif self.weight > 20:
            base_price = 399
        insurance = self.value * 0.05
        total_price = base_price + insurance
        return total_price
    
    def __str__(self):
        base_price = self.valuable_delivery_price()
        total_price = self.valuable_delivery_price() + (base_price * 0.05)
        return f"Cenný balík na adresu {self.address}, má hmotnost {self.weight} kg, je ve stavu {self.state}, cena cenného balíku činí {base_price} Kč, cena s pojištěním činí {total_price} Kč."
    
    #def get_info(self):
     #   price = self.delivery_price()
      #  return f"Cenný balík na adresu {self.address}, má hmotnost {self.weight} kg, je ve stavu {self.state}, cena balíku činí {price} Kč."
    
   
balik1 = Package("Václavské náměstí 12", 0.25, "nedoručen")               
balik2 = Package("Petra Jilemnického 382", 11, "doručen")   
balik3 = Package("Gebauerova 1422", 25, "doručen")
Cenny_balik = ValuablePackage("Harry Potterova 913 Londýn", 20, "doručen")
#print(balik1.get_info())
#print(balik2.get_info())
#print(balik3.get_info())
print(balik1.__str__())
print(balik2.__str__())
print(balik3.__str__())
print(Cenny_balik)

