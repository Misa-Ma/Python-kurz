class Postava:
    def __init__(self, jmeno):
        self.jmeno = jmeno

class Carodej(Postava):
    def kouzli(self):
        return "Expelliarmus!"

class Mudla(Postava):
    def pracuj(self):
        return "Pracuji jako obyčejný člověk."
    
class Madla(Postava):
    def caruj(self):
        return 'Jsem tvůj přítel, můžeš se na mě spolehnout.'    
    
def zkontroluj_postavu(postava):

    if isinstance (postava,Carodej):
        print (f'{postava.jmeno} je čaroděj/ka na Bradavické škole čar a kouzel.')

    elif isinstance (postava, Mudla):
        print (f'{postava.jmeno} není čarodějem, pošlete ho Bradavickým expresem zpět do Londýna!')

    elif isinstance (postava,Madla):
        print (f'{postava.jmeno} je určitě nějaký nastrčený žert Voldemorta')  
     
# Vytvoření objektů
harry = Carodej ("Harry Potter")
hermiona = Carodej ("Hermiona Grangerová")
vernon = Mudla ("Vernon Dursley")
shehrezada = Madla ('Shehrezada Madlalová')

# Testování funkce zkontroluj_postavu
zkontroluj_postavu(harry)    # Očekávaný výstup: Harry Potter je čaroděj a říká: Expelliarmus!
zkontroluj_postavu(hermiona) # Očekávaný výstup: Hermiona Grangerová je čaroděj a říká: Expelliarmus!
zkontroluj_postavu(vernon)   # Očekávaný výstup: Vernon Dursley je mudla a říká: Pracuji jako obyčejný člověk.
zkontroluj_postavu (shehrezada) #Očekávaný výstup: Shehrezada Madlalová je určitě nějaký nastrčený žert Voldemorta.
