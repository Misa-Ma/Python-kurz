class Postava:
    def __init__(self, jmeno):
        self.jmeno = jmeno

class Smrtijed(Postava):
    def kouzli(self):
        return "Avada Kedavra!"

class Profesor(Postava):
    def uci(self):
        return "Dnes se naučíme nové kouzlo."
    
class Student(Postava):
    def studuj(self):
        return "Studuji na Bradavické škole čar a kouzel."

def zkontroluj_postavu (Postava):
    # Tady doplň funkci isinstance
    if isinstance (Postava, Smrtijed):
        print (f'{Postava.jmeno} je Smrtijed a říká: Avada Kedavra!')

    elif isinstance (Postava, Profesor):
        print (f'{Postava.jmeno} je Profesor Bradavické školy a říká: Dnes se naučíme nové kouzlo.')

    elif isinstance (Postava, Student):
        print (f'{Postava.jmeno} je studentem Bradavické školy čar a kouzel a říká: Studuji na Bradavické škole čar a kouzel.')        

# Vytvoření objektů
voldemort = Smrtijed("Lord Voldemort")
snape = Profesor("Severus Snape")
harry = Student("Harry Potter")
draco = Student("Draco Malfoy")

# Testování funkce zkontroluj_postavu
zkontroluj_postavu(voldemort)  # Očekávaný výstup: Lord Voldemort je smrtijed a říká: Avada Kedavra!
zkontroluj_postavu(snape)      # Očekávaný výstup: Severus Snape je profesor a říká: Dnes se naučíme nové kouzlo.   
zkontroluj_postavu(harry)      # Očekávaný výstup: Harry Potter je student a říká: Studuji na Bradavické škole čar a kouzel.
zkontroluj_postavu(draco)      # Očekávaný výstup: Draco Malfoy je student a říká: Studuji na Bradavické škole čar a kouzel.