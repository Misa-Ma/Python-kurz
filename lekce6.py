#FUNKCE ISINSTANCE(): Když potřebujeme zkontrolovat, zda objekt patří do určité třídy nebo skupiny tříd. Používá se takto:
#isinstance (objekt, třída)
#objekt = třída(údaje), např. frantisek = Employee("František Novák", "konstruktér", 25)
#if isinstance (frantisek, manager):
#print ( 'Objekt pochází ze třídy Manager')
#else:
#print('Objekt nepochází ze třídy Manager')
#vlastně napíše True or False

class Employee:
    def __init__(self, name, position, holiday_entlitlement): 
        self.position = position
        self.holiday_entlitlement = holiday_entlitlement

    def __str__(self):   
        return f"{self.name} pracuje na pozici {self.position}"

class Manager(Employee):
    def __init__(self, name, position, holiday_entlitlement, subordinates, car):
        super().__init__(name, position, holiday_entlitlement)
        self.subordinates = subordinates
        self.car = car

    def __str__(self):
        return super().__str__() + f'Má {self.subordinates} podřízených' 
    
class Salesman(Employee):
    def __init__(self, name, position, holiday_entitlement, car):
        super().__init__(name, position, holiday_entitlement)
        self.car = car

marian = Manager ('Marian Přísný', 'vedoucí konstrukčního oddělení', 25, 5, 'Škoda Octavia 1.5 TSI')
marketa = Manager("Markéta Polková", "teamleader", 25, 12, "Škoda Octavia RS")
frantisek = Employee ( 'František Novák', 'konstruktér', 25)
jakub = Salesman("Jakub Čmelák", "business development manager", 25, "Škoda Octavia Scout")
nazev_atributu = input ('zadej název atributu:')
hodnota_atributu = getattr (marketa, nazev_atributu, 'u atributu není žádná hodnota')
#if isinstance (frantisek, Manager):
    #print ('Objekt pochází ze třídy Manager.')
#else:
    #print ('Objekt nepochází ze třídy Manager.')

# Kolik máme ve firmě manažerů, kdybychom např. dělali školení:    
employee_list = [marian, marketa, frantisek, jakub]
expected_people = 0
for item in employee_list:
   # if isinstance (item, Manager):
    #    print (f'Posílám pozvánku pro:{item.name} na školení, které se bude konat v Hasičárně Plotiště nad Labem, HK')
    #      expected_people = expected_people +1
    #   print (expected_people)   

# Zkontrolujeme si, kolik osob má auto:
# u Františka to skončilo chybou, protože nemá auto, a dál už python nejel, takže Jakuba už mi nevyjel
    #print (item.car) 

    #if hasattr(item, 'car'): #(has attribute), 'car' musí být v uvozovkách nebo si vytvořím attr_name = car, a pak tam dám místo car attr_name
        #print (item.car)

# FCE která umí přečíst atribut bezpečně - GET ATTR (get attribute)        

    print (hodnota_atributu)