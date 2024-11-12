class Postava:
    def __init__(self, jmeno):
        self.jmeno = jmeno

class Kolej(Postava):
   def __init__(self, jmeno, kolej):
       super().__init__(jmeno)
       self.kolej = kolej

    
class Ucitel(Postava):
    def __init__(self, jmeno, predmet):
        super().__init__(jmeno)
        self.predmet = predmet

def zkontroluj_postavu (postava):

    if isinstance (postava,Kolej):
        print(f'Jmenuji se {postava.jmeno} a moje bradavická kolej je {postava.kolej}.')

    elif isinstance (postava,Ucitel):
        print(f'Jmenuji se {postava.jmeno} a předmět, který vyučuji se jmenuje {postava.predmet}.')    



harry = Kolej ("Harry Potter",'Nebelvír')
snape = Ucitel ('Severus Snape', 'Lektvary')
draco = Kolej ("Draco Malfoy", 'Zmijozel')
lenka = Kolej ('Lenka Láskorádová', 'Havraspár')
mcgonagall = Ucitel ('Minerva McGonagallová', 'Přeměňování')

zkontroluj_postavu (harry)
zkontroluj_postavu (snape)
zkontroluj_postavu (draco)
zkontroluj_postavu (lenka)
zkontroluj_postavu (mcgonagall)
