class Package:

    def __init__(self, address, weight, state) -> None:
        
        self.address = address
        self.weight = weight
        self.state = state

class ValuablePackage (Package):
    def __init__(self, address, weight, state, value):
        super().__init__(address, weight, state)
        self.value = value               

    def get_info(self) -> str:

        info = f"Package to address {self.address}, has weight = {self.weight} kg and is {self.state}, {self.value} Kč."
        return info
    
    def delivery_price(self) -> int:

        if self.weight < 10:
            price = 129
        elif self.weight < 20:
            price = 159
        else:
            price = 359

        return price
    

balicek_do_prahy = Package("Vodickova 15, Praha", 2, "not delivered")

balik_do_brna = Package("Moravske namesti 1, Brno", 52, "delivered")

print(balicek_do_prahy.get_info())
print(balik_do_brna.get_info()) 
