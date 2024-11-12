class Postava:
    def __init__(self, jmeno, kolej):
        self.jmeno = jmeno
        self.kolej = kolej

jmeno = input ('Zadej své jméno:')
print (f'Ahoj {jmeno}') 
kolej = input ('Zadej svou kolej:')
print (f'Ahoj {jmeno} jenž máš kolej {kolej}') 

harry = Postava ('Harry Potter', 'Nebelvír')
# Použití hasattr pro kontrolu existence atributu
if hasattr(harry, 'jmeno'):
    print(f"Postava má atribut 'jmeno' s hodnotou: {getattr(harry, 'jmeno')}")

# Použití getattr pro získání hodnoty atributu s výchozí hodnotou
kolej_harryho = getattr(harry, 'kolej', 'Neznámá kolej')
print(f"Kolej Harryho je: {kolej_harryho}")