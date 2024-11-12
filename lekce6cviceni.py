class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    def get_info(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."

class ValuablePackage(Package):
    def __init__(self, address, weight, value, state="nedoručen"):
        super().__init__(address, weight, state)
        self.value = value

    def __str__(self):
        return super().__str__() +  f"Balík má hodnotu hodnotu {self.value} Kč."
    
package_1 = ValuablePackage("Grimmauldovo náměstí 11", 1.9, 5500, "nedoručen")
package_2 = Package("Godrikův důl 47", 1.9, "nedoručen")
package_3 = ValuablePackage("Vydrník svatého Drába 13", 1.9, 5500, 'nedoručen')
package_4 = ValuablePackage ('Gringotova banka 23', 2.5, 500, 'doručen')
package_list = [package_1, package_2, package_3]

total_value = 0

for item in package_list:
   
    if hasattr(item, 'value') and getattr(item, 'state') == 'nedoručen':
        total_value += item.value

    #if isinstance(item, ValuablePackage) and getattr(item, 'state', 'NA') == 'nedoručen': na3tím místě je nějaká defaultní hodnota, na prvním je fce, na druhém je název třídy a poslední je vše ostatní
        #total_value = total_value + item.value 

    #if getattr(item, 'state', 'NA') == 'nedoručen':
    #   if hasattr (item, 'value):
    #   total_value += item.value    

print("Celková hodnota všech nedoručených balíků činí:", total_value)

#možnost vyuzít hasattr, getattr i isinstance





