class Driver:
    def __init__ (self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

class Package:
    def __init__(self, address, weight, state, driver):
        self.address = address
        self.weight = weight
        self.state = state
        self.driver = driver

    def get_info(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."
    
    def send_message (self):
        return f'Dnes budeme doručovat Váš balíček. V případě potřeby kontaktujte prosím řidiče na čísle:{self.driver.phone_number}'
    
class ValuablePackage(Package):
    def __init__(self, address, weight, value, driver, state="nedoručen"):
        super().__init__(address, weight, state, driver)
        self.value = value

    def __str__(self):
        return super().__str__() +  f"Balík má hodnotu hodnotu {self.value} Kč."    
    
řidič = Driver ('Anča Hajná', '+420123456789')    
       
package_1 = ValuablePackage("Grimmauldovo náměstí 11", 1.9, 5500, řidič, "nedoručen")
package_2 = Package("Godrikův důl 47", 1.9, "nedoručen", řidič)
package_3 = ValuablePackage("Vydrník svatého Drába 13", 1.9, 5500, řidič, 'nedoručen')
package_4 = ValuablePackage ('Gringotova banka 23', 2.5, 500, řidič, 'doručen')
package_list = [package_1, package_2, package_3]

total_value = 0

for item in package_list:
   
    if hasattr(item, 'value') and getattr(item, 'state') == 'nedoručen':
        total_value += item.value

print("Celková hodnota všech nedoručených balíků činí:", total_value)  

for item in package_list:
    print (item.send_message())
